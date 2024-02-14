from Seq0 import *

seq, n = "U5", 20
print("Gene " + seq + "\nFragment: " + seq_read_fasta("../Sequences/" + seq + ".txt")[:n] + "\nReverse: " + seq_reverse(seq, n))