class Seq:
    """A class for representing sequences"""

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


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
def printing_sets(seq_list):
    for index, i in enumerate(seq_list):
        print(f"Sequence {index}: (Len {i.len()}) {i}")

printing_sets(seq_list)