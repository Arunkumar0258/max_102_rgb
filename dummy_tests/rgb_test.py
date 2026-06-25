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


# A Red
send([7, 0, 3, 0, 3, 1, 255, 0])

# S Green
send([7, 0, 3, 0, 3, 2, 255, 85])

# D Blue
send([7, 0, 3, 0, 3, 3, 255, 170])

# Commit once
send([7, 0, 2, 0])

print("Done")
