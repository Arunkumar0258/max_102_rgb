import hid
import pyaudiowpatch as pyaudio
import numpy as np

# ====================================
# MAX102
# ====================================


class Max102RGB:

    def __init__(self):

        for d in hid.enumerate():

            if d["vendor_id"] == 0x342D and d.get("usage_page") == 65376:

                self.dev = hid.device()
                self.dev.open_path(d["path"])

                print("MAX102 Connected")

                return

        raise Exception("MAX102 Not Found")

    def set_color(self, color):

        packet = bytes([0, 7, 3, 4, color, 255] + [0] * 27)

        self.dev.write(packet)


# ====================================
# AUDIO
# ====================================

DEVICE_INDEX = 16
CHUNK = 4096

p = pyaudio.PyAudio()

device_info = p.get_device_info_by_index(DEVICE_INDEX)

stream = p.open(
    format=pyaudio.paFloat32,
    channels=2,
    rate=int(device_info["defaultSampleRate"]),
    input=True,
    frames_per_buffer=CHUNK,
    input_device_index=DEVICE_INDEX,
)

smoothed = 0

kb = Max102RGB()

print("Music Sync Started")

while True:

    data = stream.read(CHUNK)

    audio = np.frombuffer(data, dtype=np.float32)

    peak = np.max(np.abs(audio))

    smoothed = smoothed * 0.8 + peak * 0.2

    # Auto-scale

    scaled = min(180, int(smoothed * 500))

    kb.set_color(scaled)

    print(f"Peak={peak:.4f} Color={scaled}", end="\r")
