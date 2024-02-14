from Seq1 import Seq

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")
def printing_dict(seq):
    list = ["A", "G", "T", "C"]
    for i in list:
        print(i, ":", seq.count_base(i), end = "    ")


print(f"Sequence 1: (Length: {s1.len()}) {s1}")
printing_dict(s1)

print(f"\nSequence 2: (Length: {s2.len()}) {s2}")
printing_dict(s2)

print(f"\nSequence 3: (Length: {s3.len()}) {s3}")
printing_dict(s3)
