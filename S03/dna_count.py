dna_seq = input("Please enter a DNA sequence: ")
dict = {"A": 0, "C": 0, "T": 0, "G": 0}
for i in dna_seq:
    if i in dict:
        dict[i] += 1

print("The length of the sequence is: ", str(len(dna_seq)))
for k, v in dict.items():
    print(k + ":", v)
