import http.client
import json
import termcolor

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000207552"
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
print("MIR633")
termcolor.cprint("Description: ", color="green", end="")
print(person["desc"])
termcolor.cprint("Bases: ", color="green", end="")
print(person["seq"])

