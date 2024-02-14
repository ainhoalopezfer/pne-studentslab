def seq_ping():
    print("OK")

from pathlib import Path
def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    lines = file_contents.split("\n")[1:]
    lines = "".join(lines)
    return lines
def seq_len(seq):
    return len(seq)
def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    bases = {"A": 0, "C": 0, "T": 0, "G": 0}

    for base in bases:
        count = seq_count_base(seq, base)
        bases.update({base:count})

    return bases

def seq_reverse(seq):
    seq_1 = seq[::-1]

    return seq_1[:len(seq)]

def seq_complement(seq):
    dict_of_bases = {"A": "T", "C": "G", "T": "A", "G": "C"}
    seq1 = ""
    for i in seq:
        if i in dict_of_bases:
            seq1 += dict_of_bases[i]

    return seq1

def seq_check(seq):
    seq = seq.upper()
    bases = ["A", "C", "T", "G"]

    for i in seq:
        if i not in bases:
            return "Not valid"