# Kenton Killamix Mini

This is an Ableton Live MIDI controller script for use with the [Kenton Killamix Mini](https://kentonuk.com/product/killamix-mini/) controller.

## Installation

~~Follow [Ableton's instructions](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts) to install~~

The "third party remote scripts" installation instructions don't seem to work. Maybe I did something wrong? Instead, unzip the release into Ableton's scripts in its system directory. Eg. `C:\ProgramData\Ableton\Live 11 Suite\Resources\MIDI Remote Scripts\Killamix_Mini` on Windows.

## Device Configuration

- This control script expects the Killamix Mini to be configured with encoders in **absolute** mode. "Relative Signed Bit" technically works, but the encoder sensitivity is at about 50% of what you'd expect. It [seems like](https://github.com/gluon/AbletonLive11_MIDIRemoteScripts/blob/b28d806ee359002b9d0f1cd58ea55a869e42371a/ableton/v3/control_surface/elements/encoder.py#L9) there's an [encoder sensitivity parameter](https://github.com/gluon/AbletonLive11_MIDIRemoteScripts/blob/b28d806ee359002b9d0f1cd58ea55a869e42371a/ableton/v2/control_surface/elements/encoder.py#L86) that should make this work. In my testing, the parameter didn't seem to do anything.
- Buttons are in "toggle" mode (send 127 on push and 0 on release)
- Encoder buttons are set to send CC rather than change channel.

## Mapping


### Device Mode

- **Encoders 1-8**: Automatically-mapped Device Parameters
- **Buttons 1 + 2**: Select prev/next device
- **Buttons 3 + 4**: Select prev/next device parameter bank
- **Buttons 5 + 6**: Mute/solo current track
- **Buttons 7 + 8**: Prev/next track
- **Button 9**: unmapped
- **X/Y**: unmapped
- **Encoder Buttons 1-8**: unmapped
- **Encoder Button 9**: cycle mode

### Mixer Mode

Today this mode is only partially-mapped:

- **Encoders 1-8**: Track volumes (1-8)
- **Buttons 1 + 2**: unmapped
- **Buttons 3 + 4**: unmapped
- **Buttons 5 + 6**: unmapped
- **Buttons 7 + 8**: Prev/next track
- **Button 9**: unmapped
- **X/Y**: unmapped
- **Encoder Buttons 1-8**: unmapped
- **Encoder Button 9**: cycle mode

![Killamix-Obl-2](https://user-images.githubusercontent.com/4128043/178559553-e2f46b23-c7c6-4ed0-be80-a2f36c2bd0a7.png)
