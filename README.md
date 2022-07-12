# Kenton Killamix Mini

This is an Ableton Live MIDI controller script for use with the [Kenton Killamix Mini](https://kentonuk.com/product/killamix-mini/) controller.

## Installation

Follow [Ableton's instructions](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts) to install.

## Device Configuration

- This control script expects the Killamix Mini to be configured with encoders in **absolute** mode. "Relative Signed Bit" technically works, and it [seems like](https://github.com/gluon/AbletonLive11_MIDIRemoteScripts/blob/b28d806ee359002b9d0f1cd58ea55a869e42371a/ableton/v3/control_surface/elements/encoder.py#L9) there's an [encoder sensitivity parameter](https://github.com/gluon/AbletonLive11_MIDIRemoteScripts/blob/b28d806ee359002b9d0f1cd58ea55a869e42371a/ableton/v2/control_surface/elements/encoder.py#L86) that should make this work. In my testing, the parameter didn't seem to do anything.
- Buttons are in "toggle" mode (send 127 on push and 0 on release)
- Encoder buttons are set to send CC rather than change channel. They aren't used yet.

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
