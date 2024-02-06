from pathlib import Path
FILENAME = "Sequences/U5.txt"
file_contents = Path(FILENAME).read_text()

lines = file_contents.split("\n")
lines.pop(0)
print("Body of the U5.txt file:\n" + str("\n".join(lines)))


