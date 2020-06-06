# kalliope-SoundTouch
Kalliope neurons to control Bose sound touch player


## Synopsis

Make kalliope play songs / playlist via a Bose Sound Touch device

## Installation

  ``` sh
  kalliope install --git-url https://github.com/sebcaps/kalliope-soundtouch.git
  ```


## Options

| parameter | required | default   |  Type   | comment                                                          |
|-----------|----------|-----------|---------|------------------------------------------------------------------|
|  action   | yes      |           | String  | The action to fire with  neuron (see below)                      |
|  url      | no       |           | String  | The url of the Bose player (exclusive with name)                 |
|  port     | no       |   8090    |   Int   | The port of the Bose  Player                                     |
|  name     | no       |           | String  | The name of the Bose player to handle (exclusive with host)      |
|  preset   | no       |           |   Int   | The id (1-6) of device preset to select                          |
|  volume   | no       |           |   Int   | The value of volume (0-100) to set                               |


Available actions are fow now:

- play - Switch on Bose device. If preset or volume set, select according preset and adjust volume
- stop - Switch off teh device
- set_preset - Set the channel to specified preset (1-6)
- set_volume - Set the volume to the corresponding levl (0-100)
- mute - Mute/Unmute the device

### Important

Device can be reached either by name or IP adress.
Search by name is not very performant (in terms of duration and reliability) thus use of IP adress is recommended.
In case of use of IP, **fixed IP configruation** for the device(s) is necessary to reliably connect to the device.

## Return Values

| Name         | Description                                                                           | Type     | sample   |
| ------------ | ------------------------------------------------------------------------------------- | -------- | -------- |
|              |                                                                                       |          |          |

## Synapses example

Switch on the device (with IP 192.168.0.45 on port 8091), with volume 30 at preset 5

``` yaml
- name: "allume"
  signals:
    - order: "Met le son"
    - order: "mets le son"
  neurons:
    - say:
        message: 
          - "Je vais allumer l'enceinte"
    - soundtouch:
       host: 192.168.0.45
       port : 8091
       volume: 30
       preset: 5
       action: play
```

Stop the device with IP 192.168.0.45 (on default port 8090)

```yaml
- name: "stop"
  signals:
  - order: "arrête l'enceinte"
  neurons:
    - soundtouch:
        host: 192.168.0.45
        action: stop
```

Set volume to 15 (on 0-100 range)

```yaml
- name: "son15"
  signals:
  - order: "Met le son à 15"
  neurons:
    - say:
       message: 
          - "Je met le son à 15"
    - soundtouch:
        host: 192.168.0.45
        action: set_volume
        volume: 15
```

Broadcast preset 3 content

```yaml
- name: "preset"
  signals:
    - order: "sélection 3"
  neurons:
    - soundtouch:
        host: 192.168.0.45
        action: set_preset
        preset: 3
```

Mute the device, if called a second time device is unmuted

```yaml
- name: "mute"
  signals:
  - order: "Mute device"
  neurons:
    - soundtouch:
        host: 192.168.0.45
        action: mute
```

Switch on device by name from captured order 

```yaml
- name: "deviceByName"
  signals:
  - order: "Allume {{ enceinte }}"
  neurons:
    - say:
       message: 
          - "J'allume l'enceinte {{ enceinte }}"
    - soundtouch:
        name: "{{ enceinte }}"
        action: play
```

## External lib used

- [libsoundtouch](https://github.com/CharlesBlonde/libsoundtouch)