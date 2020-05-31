
# -*- coding: utf-8 -*-
import logging

from kalliope.core.NeuronModule import NeuronModule, MissingParameterException
logging.basicConfig()
logger = logging.getLogger("kalliope")

class Soundtouch(NeuronModule):
    def __init__(self,**kwargs):
        super(Soundtouch,self).__init__(**kwargs)

        self.configuration ={
            self.sound_host=kwargs.get('sound_host', None)
            self.sound_port=kwargs.get('sound_port', None)
            self.sound_action=kwargs.get('sound_action', None)
            self.sound_volume=kwargs.get('sound_volume', None)
            self.sound_preset=kwargs.get('sound_preset', 1)
        }
        self._initSoundTouch()

        if self._is_parameters_ok() and self.device:
            if self.configuration.['sound_action']=="play_preset":
                logger.debug("Turn on and play preset")
                self._play_preset(self)
            elif selt.configuration.['sound_action']=="stop_device":
                self._stop_device(self)

    def _initSoundTouch():
        if (self.sound_port) is not None
            device = soundtouch(self.sound_host,self.sound_port)
        else
            device = soundtouch(self.sound_host)

        if device is None:
            logger.error('Device not found')
            raise RuntimeError("Device not found")
        else:
            self.device=device
            
    def _play_preset(self):
        logger.debug("in _play_preset")
        self.device.power_on()
        self.device.select_preset(self,self.sound_preset)
    
    def _stop_device(self):
        logger.debug("in _stop_device")
        self.device.power_off()

    def _is_parameters_ok(self):
                """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: MissingParameterException
        """
        if self.configuration['host'] is None:
            raise MissingParameterException("Host parameter required")
        if self.configuration['sound_action'] is None:
            raise InvalidParameterException("Soundtouch needs an action")
        elif self.configuration['sound_action'] not in ['play_preset'] 
            raise InvalidParameterException("Soundtouch does not support action :")+self.configuration['sound_action']


        return True