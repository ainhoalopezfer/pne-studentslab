from pathlib import Path
FILENAME = "Sequences/U5.txt"
file_contents = Path(FILENAME).read_text()

lines = file_contents.split("\n")
print("Body of the U5.txt file:")
for i in range(1, len(lines)):
    print(lines[i])

