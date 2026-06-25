import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from max102 import Max102, Color

kb = Max102()

kb.connect()

kb.set_key("A", Color.RED)

kb.set_key("S", Color.GREEN)

kb.set_key("D", Color.BLUE)

kb.commit()
