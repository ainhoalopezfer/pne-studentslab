from Seq0 import *
folder = "../Sequences/"
filename = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]

for i in filename:
    length = seq_len(folder + i)
    print("Gene " + i.replace(".txt", "") + " -> Length: " + str(length))