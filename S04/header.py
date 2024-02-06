from pathlib import Path
FILENAME = "Sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()

first_line = file_contents.split("\n")
print("First line of the RNU6_269P.txt file: \n" + first_line[0])