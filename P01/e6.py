from Seq1 import Seq

s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}) {s1}\n    Bases: {s1.count()}")
print(f"Sequence 2: (Length: {s2.len()}) {s2}\n    Bases: {s2.count()}")
print(f"Sequence 3: (Length: {s3.len()}) {s3}\n    Bases: {s3.count()}")