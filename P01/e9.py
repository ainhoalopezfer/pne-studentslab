from Seq1 import Seq
# -- Create a Null sequence
s = Seq()
FILENAME = "../Sequences/ADA"
# -- Initialize the null seq with the given file in fasta format
s.read_fasta(FILENAME)

print(f"Sequence 1: (Length: {s.len()}) {s}\n    Bases: {s.count()}\n    Reverse: {s.reverse()}\n    Complement: {s.seq_complement()}")
