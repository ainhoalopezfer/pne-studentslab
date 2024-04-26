import http.client
import json

#"https://rest.ensembl.org/info/assembly/homo_sapiens?content-type=application/json"
#http://rest.ensembl.org/info/species?content-type=application/json
SERVER = "rest.ensembl.org"
def data(ENDPOINT):
    SERVER = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"
    URL = SERVER + ENDPOINT + PARAMS

    print()
    print(f"Server {SERVER}")
    print(f"URL {URL}")

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")

    person = json.loads(data1)

    return person


requestline = "GET /geneCalc?chromosome=ADA HTTP/1.1"
request = requestline.split(" ")
gene = request[1][21:]
print(gene)


class Seq:
    def __init__(self, seq):
        self.seq = seq

    """def getting_seq(self):
        person = data("/lookup/symbol/homo_sapiens/" + self.gene)
        name = person["id"]
        person1 = data("sequence/id/" + name)
        seq = person1["seq"]
        return seq"""
    def length(self):
        #seq = self.getting_seq()
        return len(self.seq)

    def count(self, b):
        #seq = self.getting_seq()
        base = self.seq.count(b)
        percentage = (base/len(self.seq) * 100)

        return b + ": " + str(base) + " (" + str(percentage) + "%)"


bases = ["A", "G", "T", "C"]
gene = "ATGCTAGTCAGTA"
s = Seq(gene)
results = []
for i in bases:
    results.append(s.count(i))

print(results)