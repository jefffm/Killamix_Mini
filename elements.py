from __future__ import absolute_import, print_function, unicode_literals

from ableton.v3.control_surface import ElementsBase, MapMode, PrioritizedResource


class Elements(ElementsBase):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)

        # Encoders 1-8
        self.add_encoder_matrix(
            [list(range(1, 10))],
            "encoders",
            map_mode=MapMode.Absolute,
        )
        self.add_submatrix(self.encoders, "Encoders_1_thru_8", columns=(0, 8))

        # Encoder 9
        self.add_encoder(9, "Encoder_9")

        # Buttons 1-9
        self.add_button_matrix(
            [list(range(9, 19))],
            "buttons",
        )
        self.add_submatrix(self.buttons, "Buttons_1_thru_8", columns=(9, 18))

        # Button 9
        self.add_modifier_button(18, "Button_9")
