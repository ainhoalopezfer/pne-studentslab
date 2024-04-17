import termcolor
genes = {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060", "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296", "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078", "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"}

if __name__ == "__main__":
    print("\nDictionary of genes!\nThere are 10 genes in the dictionary\n")

    for k, v in genes.items():
        termcolor.cprint(k, color="green", end="")
        print(": --> " + v)

