class Seq:
    def __init__(self, strbases):
        bases = ["A", "C", "T", "G"]
        for i in strbases:
            if i not in bases:
                strbases = "ERROR!!"

        if strbases == "ERROR!!":
            print("ERROR!!")
        else:
            print("New sequence created!")
        self.strbases = strbases
    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)
def generate_seqs(seq, number):
    list = []
    for i in range(1, number + 1):
        seq1 = seq * i
        list.append(Seq(seq1))

    return list

def printing_sets(seq_list):
    for index, i in enumerate(seq_list):
        print(f"Sequence {index}: (Len {i.len()}) {i}")


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
printing_sets(seq_list1)

print()
print("List 2:")
printing_sets(seq_list2)
