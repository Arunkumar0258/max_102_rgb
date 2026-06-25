import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from max102 import Max102

kb = Max102()

kb.connect()

print("Connected")
