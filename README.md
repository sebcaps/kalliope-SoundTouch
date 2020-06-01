# kalliope-SoundTouch
Kalliope neurons to control Bose sound touch player


## Synopsis

Make kalliope play songs / playlist via a Bose Sound Touch

## Installation

  ```
  kalliope install --git-url https://github.com/sebcaps/kalliope-soundtouch.git
  ```


## Options

| parameter | required | default   |  Type   | comment                                                          |
|-----------|----------|-----------|---------|------------------------------------------------------------------|
|  action   | yes      |           | String  | The action to fire with  neuron (see below)                      |
|  url      | no       |           | String  | The url of the Bose player (exclusive with name)                 |
|  port     | no       |   8090    |   Int   | The port of the Bose  Player                                     |
|  name     | no       |           | string  | The name of the Bose player to handle (exclusive with host)      |
|  preset   | no       |           |   Int   | The id (1-6) of device preset to select                          |
|  volume   | no       |           |   Int   | The value of volume (0-100) to set                               |


Available actions are fow now:

- play - Switch on Bose device. If preset or volume set select according preset and adjust volume
- stop - Switch off teh device
- set_preset - Set the channel to specified preset (1-6)
- volume - Set the volume to the corresponding levl (0-100)
- mute - Mute/Unmute the device

## Return Values

| Name         | Description                                                                           | Type     | sample   |
| ------------ | ------------------------------------------------------------------------------------- | -------- | -------- |
|              |                                                                                       |          |          |

## Synapses example

Switch on the device (with IP 192.168.0.46 on port 8091), with volume 30 at preset 5

``` yaml
- name: "deviceOn"
  signals:
    - order: "Start device"
  neurons:
    - soundtouch:
       host: 192.168.0.46
       port: 8091
       volume: 30
       preset: 5
       action: play
```

Stop the device with IP 192.168.0.46 (on default port 8090)

```yaml
- name: "deviceOff"
  signals:
  - order: "Stop device"
  neurons:
    - soundtouch:
        host: 192.168.0.46
        action: stop
```

Set volume to 15 (on 0-100 range)

```yaml
- name: "sundLevel15"
  signals:
  - order: "Sound at 15"
  neurons:
    - soundtouch:
        host: 192.168.0.46
        action: set_volume
        volume: 15
```

Broadcast preset 1 content

```yaml
- name: "preset1"
  signals:
  - order: "Preset one"
  neurons:
    - soundtouch:
        host: 192.168.0.46
        action: preset
        volume: 1
```

Mute the device, if called a second time device is unmuted

```yaml
- name: "mute"
  signals:
  - order: "Mute device"
  neurons:
    - soundtouch:
        host: 192.168.0.46
        action: mute
```

```yaml
- name: "radionom"
  signals:
  - order: "Allume l'enceinte {{name}}"
  neurons:
    - say:
       message: 
          - "J'allume l'enceinte {{name}}"
    - soundtouch:
        name: {{name}}
        action: play
```
