from Seq1 import Seq

s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}) {s1}\n    Bases: {s1.count()}\n    Reverse: {s1.reverse()}\n    Complement: {s1.seq_complement()}")
print(f"Sequence 2: (Length: {s2.len()}) {s2}\n    Bases: {s2.count()}\n    Reverse: {s2.reverse()}\n    Complement: {s2.seq_complement()}")
print(f"Sequence 3: (Length: {s3.len()}) {s3}\n    Bases: {s3.count()}\n    Reverse: {s3.reverse()}\n    Complement: {s3.seq_complement()}")