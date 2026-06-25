import hid

from .constants import (
    VENDOR_ID,
    PRODUCT_ID,
    USAGE_PAGE,
)

from .protocol import (
    key_packet,
    commit_packet,
    brightness_packet,
    global_commit_packet,
)

from .keymap import KEY_MAP

from .exceptions import DeviceNotFound


class Max102:

    def __init__(self):
        self.dev = None

    def connect(self):

        for d in hid.enumerate():

            if d["vendor_id"] == VENDOR_ID and d.get("usage_page") == USAGE_PAGE:

                self.dev = hid.device()
                self.dev.open_path(d["path"])

                return

        raise DeviceNotFound("MAX102 not found")

    def write(self, packet):

        self.dev.write(packet)

    def set_key(self, key: str, hue: int, saturation: int = 255):

        row, col = KEY_MAP[key]

        self.write(key_packet(row, col, hue, saturation))

    def commit(self):

        self.write(commit_packet())

    def set_brightness(self, value: int):

        self.write(brightness_packet(value))

        self.write(global_commit_packet())
