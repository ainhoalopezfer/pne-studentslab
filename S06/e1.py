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


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

