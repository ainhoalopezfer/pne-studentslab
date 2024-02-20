from Seq1 import *
s = Seq()
files = ["U5", "ADA", "FRAT1", "RNU6_269P", "FXN"]
for i in files:
    filename = "../Sequences/" + i + ".txt"
    s.read_fasta(filename)
    print(f"Gene {i}: Most frequent base: {s.most_frequent_base()}")