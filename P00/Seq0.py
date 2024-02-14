def seq_ping():
    print("OK")

from pathlib import Path
def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    lines = file_contents.split("\n")[1:]
    lines = "".join(lines)
    return lines

def seq_len(filename):
    lines = seq_read_fasta(filename)
    return len(lines)
def seq_count_base(seq, base):
    lines = seq_read_fasta("../Sequences/" + seq + ".txt")
    return lines.count(base)

def seq_count(seq):
    bases = {"A": 0, "C": 0, "T": 0, "G": 0}

    for base in bases:
        count = seq_count_base(seq, base)
        bases.update({base:count})

    return bases

def seq_reverse(seq, n):
    lines = seq_read_fasta("../Sequences/" + seq + ".txt")[::-1]

    return lines[:n]

def seq_complement(seq):
    dict_of_bases = {"A": "T", "C": "G", "T": "A", "G": "C"}

    for i in seq:
        if i in dict_of_bases:
            print(dict_of_bases[i], end = "")

def most_frequent_base(seq):
    from operator import itemgetter
    dict = seq_count(seq)
    bases = sorted(dict, key = itemgetter())



