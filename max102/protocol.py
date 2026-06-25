from .constants import REPORT_SIZE


def pad(packet: list[int]) -> list[int]:
    while len(packet) < REPORT_SIZE:
        packet.append(0)

    return packet


def key_packet(
    row: int,
    col: int,
    hue: int,
    saturation: int = 255,
):
    return pad(
        [
            0,
            7,
            0,
            3,
            0,
            row,
            col,
            saturation,
            hue,
        ]
    )


def commit_packet():

    return pad([0, 7, 0, 2, 0])


def brightness_packet(value: int):
    return pad([0, 7, 3, 1, value])


def global_commit_packet():

    return pad([0, 9, 3, 0, 0])
