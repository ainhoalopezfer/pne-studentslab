def dna_counter_from_file(filename):
    with open(filename, "r") as f:
        total_num_bases = 0
        dict = {"A": 0, "C": 0, "T": 0, "G": 0}
        for line in f:
            total_num_bases += len(line)
            for i in line:
                if i in dict:
                    dict[i] += 1

    print(f"Total number of bases: {total_num_bases}")
    for k, v in dict.items():
        print(k + ":", v)

dna_counter_from_file("dna")
