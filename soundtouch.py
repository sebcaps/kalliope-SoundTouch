
# -*- coding: utf-8 -*-
import logging
from libsoundtouch import discover_devices
from libsoundtouch import soundtouch_device
from libsoundtouch.utils import Source, Type
from libsoundtouch.device import NoSlavesException, NoExistingZoneException,Preset, Config, SoundTouchDevice, SoundtouchInvalidUrlException

from kalliope.core.NeuronModule import NeuronModule, MissingParameterException, InvalidParameterException
logging.basicConfig()
logger = logging.getLogger("kalliope")

class Soundtouch(NeuronModule):
    def __init__(self,**kwargs):
        super(Soundtouch,self).__init__(**kwargs)

        self.configuration = {
            "host" : kwargs.get('host', None),
            "name" : kwargs.get('name',None),
            "port" : kwargs.get('port', None),
            "action" : kwargs.get('action', None),
            "volume" : kwargs.get('volume', None),
            "preset" : kwargs.get('preset', 1)
        }

        self._initSoundTouch()

        if self._is_parameters_ok() and self.device:
            if self.configuration['action']=="play":
                logger.debug("Turn on and play")
                self._play()
            elif self.configuration['action']=="stop":
                self._stop_device()
            elif self.configuration['action']=="set_volume":
                self._set_volume()
            elif self.configuration['action']=="mute":
                self._mute()
            elif self.configuration['action']=="set_preset":
                self._set_preset()


    def _initSoundTouch(self):
        if (self.configuration['name']) is not None:
            logger.debug("Searching device with name : "+self.configuration['name'])
            device = self._findByName()
        elif (self.configuration['port']) is not None:
            device = soundtouch_device(self.configuration['host'],self.configuration['port'])
        else:
            device = soundtouch_device(self.configuration['host'])

        if device is None:
            logger.error('Device not found')
            raise RuntimeError("Device not found")
        else:
            logger.debug("Got device :"+ device.config.name)
            self.device=device


    def _play(self):
        logger.debug("in _play")
        self.device.power_on()
        if self.configuration['preset'] is not None:
            self._set_preset()
        if self.configuration['volume'] is not None:
            self._set_volume()

    def _findByName(self):
        devices = discover_devices(timeout=5)
        logger.debug("Searching device...")
        logger.debug(devices)
        for deviceDiscovered in devices:
            logger.debug("Found device : "+deviceDiscovered.config.name)
            if deviceDiscovered.config.name.lower() == self.configuration['name'].lower():
                logger.debug("Target device "+self.configuration['name']+" found")
                return deviceDiscovered
                break

    def _stop_device(self):
        logger.debug("in _stop_device")
        self.device.power_off()

    def _set_volume(self):
        logger.debug("in _set_volume, with volume value : "+ str(self.configuration['volume']))
        self.device.set_volume(self.configuration['volume'])

    def _mute(self):
        logger.debug("in _mute")
        self.device.mute()
    
    def _set_preset(self):
        logger.debug("in _set_preset with value : "+str(self.configuration['preset']))
        pres = self.device.presets()[self.configuration['preset']-1]
        logger.debug ('Set preset to :' +pres.name)
        self.device.select_preset(pres)
    
    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: MissingParameterException
        """
        if self.configuration['host'] is None and self.configuration['name'] is None :
            raise MissingParameterException("Host or Name parameter required")
        if self.configuration['host'] is not None and self.configuration['name'] is not None:
            raise InvalidParameterException("Host and Name parameter can not be used simultaneously")
        if self.configuration['action'] is None:
            raise InvalidParameterException("Soundtouch needs an action")
        if self.configuration['volume'] is not None and (self.configuration['volume'] <0  or self.configuration['volume'] >100 ):
            raise InvalidParameterException("Volume must be greater than 0 and lower than 100")
        elif self.configuration['action'] not in ['play','stop','set_volume','mute','set_preset'] :
            raise InvalidParameterException("Soundtouch does not support action")
        elif self.configuration['preset'] is not None and not(isinstance(self.configuration['preset'],int)):
            raise InvalidParameterException("Preset must be set to an integer value")
        elif self.configuration['preset'] <= 0 or self.configuration['preset'] > 6 :
            raise InvalidParameterException("Preset must be greater than 0 and lower or equal to 6")
        return True