# src/max102/effects/music_sync.py

import numpy as np

from max102 import Max102

from max102.audio import AudioCapture

from max102.colors import (
    volume_to_hue,
)


class MusicSyncEffect:

    def __init__(self):

        self.keyboard = Max102()
        self.audio = AudioCapture()

    def run(self):

        self.keyboard.connect()

        self.audio.start()

        print("Music Sync Started")

        smoothed = 0

        while True:

            audio = self.audio.read_audio()

            peak = np.max(np.abs(audio))

            smoothed = smoothed * 0.85 + peak * 0.15

            hue = volume_to_hue(smoothed)

            self.keyboard.set_key("A", hue)

            self.keyboard.set_key("S", hue)

            self.keyboard.set_key("D", hue)

            self.keyboard.commit()
