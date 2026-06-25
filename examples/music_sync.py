# examples/music_sync.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from max102.effects.music_sync import MusicSyncEffect

MusicSyncEffect().run()
