from Seq0 import *

gene = "U5"
lines = seq_read_fasta("../Sequences/" + gene + ".txt")[:20]

print("Gene " + gene + ":\nFragment: " + lines + "\nComplement: ", end = "")
seq_complement(lines)