# kalliope-SoundTouch
Kalliope neurons to control Bose sound touch player


## Synopsis

Make kalliope play songs / playlist via a Bose Sound Touch

## Installation

  ```
  kalliope install --git-url https://github.com/sebcaps/kalliope-soundtouch.git
  ```


## Options

| parameter    | required | default   | choices | comment                                                                                    |
|--------------|----------|-----------|---------|--------------------------------------------------------------------------------------------|
|  action   | yes      |           | string  | The action to fire with  neuron (see below)                                             |
| url      | no       | localhost | string  | The url of the bose player                                                                 |
| port     | no      |8090| Int  | The port of the Bose  Player                                                       |
| name     | no       |           | string  | The name of the Bose player to handle                                                             |

Available actions are fow now:

- play - *requires preset parameter*
- stop
- set_volume - *requires volume parameter*

## Return Values

| Name         | Description                                                                           | Type     | sample   |
| ------------ | ------------------------------------------------------------------------------------- | -------- | -------- |
|              |                                                                                       |          |          |

## Synapses example

TODO
