# src/max102/audio.py

import pyaudiowpatch as pyaudio
import numpy as np


class AudioCapture:

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.device_index = None
        self.stream = None

    def find_loopback_device(self):

        for i in range(self.p.get_device_count()):

            device = self.p.get_device_info_by_index(i)

            if "[Loopback]" in device["name"]:

                if "NVIDIA" in device["name"]:
                    self.device_index = i
                    return device

        raise RuntimeError("No loopback device found")

    def start(
        self,
        chunk_size=4096,
    ):

        device = self.find_loopback_device()

        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            channels=2,
            rate=int(device["defaultSampleRate"]),
            input=True,
            frames_per_buffer=chunk_size,
            input_device_index=self.device_index,
        )

    def read_audio(self):

        data = self.stream.read(
            4096,
            exception_on_overflow=False,
        )

        return np.frombuffer(
            data,
            dtype=np.float32,
        )
