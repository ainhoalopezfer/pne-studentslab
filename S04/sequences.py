from pathlib import Path
FILENAME = "Sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()

lines = file_contents.split("\n")[1:]
print("The number of bases in the sequence is: " + str(len("".join(lines))))