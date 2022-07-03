from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.capabilities import (
    CONTROLLER_ID_KEY,
    NOTES_CC,
    PORTS_KEY,
    REMOTE,
    SCRIPT,
    controller_id,
    inport,
    outport,
)

from .killamix_mini import KillamixMini


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(
            vendor_id=6842, product_ids=[11], model_name=["Kenton Killamix Mini"]
        ),
        PORTS_KEY: [
            inport(props=[NOTES_CC, SCRIPT, REMOTE]),
            outport(props=[SCRIPT]),
        ],
    }


def create_instance(c_instance):
    return KillamixMini(c_instance=c_instance)
