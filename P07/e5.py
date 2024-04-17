from e2 import genes
import http.client
import json
import termcolor
from Seq2 import Seq


for name in genes.keys():
    code = genes[name]

    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/" + code
    PARAMS = "?content-type=application/json"
    URL = SERVER + ENDPOINT + PARAMS

    print()
    print(f"Server {SERVER}")
    print(f"URL {URL}")

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT+PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")

    person = json.loads(data1)

    termcolor.cprint("Gene: ", color="green", end="")
    print(name)
    termcolor.cprint("Description: ", color="green", end="")
    print(person["desc"])
    seq = person["seq"]

    s = Seq(seq)
    termcolor.cprint("Total length of the sequence: ", color="green", end="")
    print(s.len())
    bases = {"A": 0, "G": 0, "T": 0, "C": 0}
    for i in bases.keys():
        termcolor.cprint(i + ": ", color="blue", end="")
        print(s.count(i))
        count = s.count(i).split(" ")
        bases[i] += int(count[0])

    termcolor.cprint("Most frequent base: ", color="green", end="")
    sort = sorted(bases.items(), key=lambda x: x[1], reverse=True)
    print(sort[0][0])

