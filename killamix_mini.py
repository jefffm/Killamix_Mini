from __future__ import absolute_import, print_function, unicode_literals

from ableton.v3.base import listens
from ableton.v3.control_surface import (
    ControlSurface,
    ControlSurfaceSpecification,
    Layer,
)
from ableton.v3.control_surface.components import (
    MixerComponent,
    DeviceComponent,
    ViewControlComponent,
    SimpleDeviceNavigationComponent,
)
from ableton.v3.control_surface.mode import AddLayerMode, ModesComponent
from .elements import Elements


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    num_tracks = 8
    num_scenes = 1
    link_session_ring_to_track_selection = True


class KillamixMini(ControlSurface):
    def __init__(self, c_instance):
        super().__init__(c_instance=c_instance, specification=Specification)

    def _create_control_surface(self):
        self._create_device_parameters()
        self._create_view_control()
        self._create_device_navigation()
        self._create_mixer()
        self._create_modes()

        self.set_can_update_controlled_track(True)

        self.show_message("Kenton Killamix Mini Initialized Successfully")

    def _create_device_parameters(self):
        self._device = DeviceComponent(
            is_enabled=False,
            layer=Layer(
                prev_bank_button="buttons_raw[3]",
                next_bank_button="buttons_raw[4]",
                parameter_controls="encoders_1_thru_8",
            ),
        )
        self._device.set_enabled(True)

    def _create_view_control(self):
        self._view_control = ViewControlComponent(
            is_enabled=False,
            layer=Layer(
                prev_track_button="buttons_raw[7]", next_track_button="buttons_raw[8]"
            ),
        )

        self._view_control.set_enabled(True)

    def _create_device_navigation(self):
        self._device_navigation = SimpleDeviceNavigationComponent(
            is_enabled=False,
            layer=Layer(
                prev_button="buttons_raw[1]",
                next_button="buttons_raw[2]",
            ),
        )
        self._device_navigation.set_enabled(True)

    def _create_mixer(self):
        self._mixer = MixerComponent(
            is_enabled=False,
            layer=Layer(
                target_track_solo_button="buttons_raw[5]",
                target_track_mute_button="buttons_raw[6]",
            ),
        )
        self._mixer.set_enabled(True)

    def _create_modes(self):
        self._modes = ModesComponent(
            name="modes",
            is_enabled=False,
            layer=Layer(cycle_mode_button="button_9"),
        )
        self._modes.add_mode(
            "device",
            (),
        )
        self._modes.add_mode(
            "mixer",
            (
                AddLayerMode(
                    self._mixer,
                    Layer(
                        volume_controls="encoders",
                        master_track_volume_control="encoder_9",
                    ),
                )
            ),
        )
        self._modes.selected_mode = "device"
        self._modes.set_enabled(True)

        self._KillamixMini__on_modes_changed.subject = self._modes

    @listens("selected_mode")
    def __on_modes_changed(self, mode):
        self.show_message(f"Killamix Mini: Entering {mode} mode")
