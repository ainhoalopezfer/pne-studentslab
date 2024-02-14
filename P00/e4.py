from Seq0 import *

seq = ["U5", "ADA", "FRAT1", "FXN"]
base = ["A", "C", "T", "G"]

for i in seq:
    print("\nGene " + i + ":")
    for bases in base:
        count = seq_count_base(i, bases)
        print(bases + ": " + str(count))