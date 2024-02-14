from Seq0 import *
FOLDER = "../Sequences/"
FILENAME = "U5.txt"
lines = seq_read_fasta(FOLDER+FILENAME)

print("DNA file: " + FILENAME)
print("The first 20 bases are:\n" + lines[:20])