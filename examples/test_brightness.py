import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import time
from max102 import Max102

kb = Max102()
kb.connect()

kb.set_brightness(36)

time.sleep(2)

kb.set_brightness(72)
