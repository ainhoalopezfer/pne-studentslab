from pathlib import Path
class Seq:
    def __init__(self, seq):
        self.seq = seq

    def length(self):
        return len(self.seq)

    def count(self, b):
        base = self.seq.count(b)
        percentage = round((base/len(self.seq) * 100), 1)

        return str(base) + " (" + str(percentage) + "%)"

    def comp(self):
        dict_of_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
        r_seq = ""
        for i in self.seq:
            if i in dict_of_bases:
                r_seq += dict_of_bases[i]

        return r_seq

    def rev(self):
        seq1 = self.seq[::-1]
        rev_seq = seq1[:self.length()]

        return rev_seq

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        lines = file_contents.split("\n")[1:]
        seq = "".join(lines)
        self.seq = seq
        return self.seq