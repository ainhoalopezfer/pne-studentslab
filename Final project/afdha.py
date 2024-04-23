import http.client
import json
"""
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

requestline = "GET /karyotype?specie=human HTTP/1.1"
request = requestline.split(" ")
specie = request[1][18:]
print(specie)
chromosomes = ""
person = data("/info/species")
for i in person["species"]:
    for n in i["aliases"]:
        if specie in n:
            sci_specie = i["name"]
            print(sci_specie)
            person1 = data("/info/assembly/" + sci_specie)
            print(person1["top_level_region"][1]["length"])

print(chromosomes)


def sci_name(specie):
    sci_specie = ""
    person = data("/info/species")
    for i in person["species"]:
        for n in i["aliases"]:
            if specie in n:
                sci_specie = i["name"]
    return sci_specie
"""

request = "GET /chromosomeLength?specie=human&chromosome=1 HTTP/1.1"
request = request.split(" ")
specie = request[1][25:-13]
number = request[1][42:]
print(specie, number)