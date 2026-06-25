import hid
import time

dev = None

for d in hid.enumerate():
    if d["vendor_id"] == 0x342D and d.get("usage_page") == 65376:
        dev = hid.device()
        dev.open_path(d["path"])
        break


def send(data):
    packet = [0] + data

    while len(packet) < 33:
        packet.append(0)

    dev.write(packet)


# Brightness low

send([7, 3, 1, 72])

send([9, 3, 0, 0])

print("Brightness set")
