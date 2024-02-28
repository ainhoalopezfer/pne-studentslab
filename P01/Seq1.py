from pathlib import Path
class Seq:
    def __init__(self, strbases = "NULL"):
        if strbases == "NULL":
            print("NULL sequence created")
        else:
            bases = ["A", "C", "T", "G"]
            for i in strbases:
                if i not in bases:
                    strbases = "ERROR"

            if strbases == "ERROR":
                print("Invalid sequence")
            else:
                print("New sequence created!")


    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            length = 0
        else:
            length = len(self.strbases)

        return length

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        bases = {"A": 0, "G": 0, "C": 0, "T": 0}
        for key in bases.keys():
            bases[key] += self.count_base(key)

        return bases

    def reverse(self):
        seq = self.strbases

        if seq == "NULL" or seq == "ERROR":
            ans = seq
        else:
            seq1 = seq[::-1]
            ans = seq1[:self.len()]

        return ans

    def seq_complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            str = self.strbases
        else:
            dict_of_bases = {"A": "T", "C": "G", "T": "A", "G": "C"}
            str = ""
            for i in self.strbases:
                if i in dict_of_bases:
                    str += dict_of_bases[i]

        return str

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        lines = file_contents.split("\n")[1:]
        strbases = "".join(lines)
        self.strbases = strbases
        return self.strbases

    def most_frequent_base(self):
        dict = self.count()
        highest_value = 0
        key1 = ""
        for key, value in dict.items():
            if value > highest_value:
                highest_value = value
                key1 = key

        return key1

    #FOR PRACTICE 2

    def first_n_str(self, num_of_times, filename, num_of_bases):
        file = self.read_fasta(filename)
        file_new = []
        for i in range(num_of_times):
            file_new.append(file[:num_of_bases])
            file = file[num_of_bases:]

        return file_new


