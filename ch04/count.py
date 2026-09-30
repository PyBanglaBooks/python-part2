import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: python count.py <file name>")
    sys.exit()

path = Path(sys.argv[1])
if not path.is_file():
    print(f"{path} is not a file")
    sys.exit()

text = path.read_text(encoding="utf-8")
print(f"Lines: {len(text.splitlines())}")
print(f"Words: {len(text.split())}")
print(f"Characters: {len(text)}")
