from Seq0 import *

files = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "T", "G"]

for i in files:
    base = most_frequent_base(i)
    print("Gene " + i + ": Most frequent base: " + base)

    