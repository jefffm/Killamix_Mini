# Kenton Killamix Mini

This is an Ableton Live MIDI controller script for use with the [Kenton Killamix Mini](https://kentonuk.com/product/killamix-mini/) controller.

## Installation

Follow [Ableton's instructions](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts) to install.

## Device Configuration

- This control script expects the Killamix Mini to be configured with encoders in **absolute** mode. "Relative Signed Bit" works fine, but I found the encoder speed was very slow for some reason.
- Buttons are in "toggle" mode (send 127 on push and 0 on release)
- Encoder buttons are set to send CC rather than change channel. They aren't used yet.

## Mapping

### Device Mode

- **Encoders 1-8**: Automatically-mapped Device Parameters
- **Buttons 1 + 2**: Select prev/next device
- **Buttons 3 + 4**: Select prev/next device parameter bank
- **Buttons 5 + 6**: Solo/mute current track
- **Buttons 7 + 8**: Prev/next track
- **Button 9**: Toggle mode
- **X/Y**: unmapped
- **Encoder Buttons 1-9**: unmapped

### Mixer Mode

Today this mode is only partially-mapped:

- **Encoders 1-8**: Track volumes (1-8)
- **Buttons 1 + 2**: unmapped
- **Buttons 3 + 4**: unmapped
- **Buttons 5 + 6**: unmapped
- **Buttons 7 + 8**: unmapped
- **Button 9**: Toggle mode
- **X/Y**: unmapped
- **Encoder Buttons 1-9**: unmapped