import http.client
import http.server
import json
from pathlib import Path
import termcolor
import socketserver
import jinja2 as j

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
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



class Seq:
    def __init__(self, gene):
        self.gene = gene

    def getting_seq(self):
        person = data("/lookup/symbol/homo_sapiens/" + self.gene)
        name = person["id"]
        person1 = data("sequence/id/" + name)
        seq = person1["seq"]
        return seq
    def length(self):
        seq = self.getting_seq()
        return len(seq)

    def count(self, b):
        seq = self.getting_seq()
        base = seq.count(b)
        percentage = (base/len(seq) * 100)

        return b + ": " + str(base) + " (" + str(percentage) + "%)"


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        request = self.requestline.split(" ")
        action = request[1]
        instruction = ""
        if "?" in request[1]:
            separate = request[1].split("?")
            action, instruction = separate[0], separate[1]
        print(action, instruction)
        def read_html_file(filename):
            contents = Path("html/" + filename).read_text()
            contents = j.Template(contents)
            return contents

        def sci_name(specie):
            specie = specie.replace("+", " ").strip().lower()
            sci_specie = ""
            person = data("/info/species")
            for i in person["species"]:
                if i["display_name"].lower() == specie.lower():
                    sci_specie = i["name"]
            return sci_specie



        if action == "/" or action == "/index.html":
            contents = open("../Final project/html/index.html").read()
        elif action == "/listSpecies":
            person = data("/info/species")
            total = len(person["species"])
            number = total
            if instruction:
                number = instruction[6:]
                number = int(number)
            names = []
            for i in range(number):
                name = person["species"][i]["common_name"].capitalize()
                names.append(name)
            contents = read_html_file("listSpecies.html").render(context={"total": total, "number": number, "list": names})
        elif action == "/karyotype":
            specie = instruction[8:]
            chromosomes = []
            sci_specie = sci_name(specie)
            if sci_specie:
                person1 = data("/info/assembly/" + sci_specie)
                if person1["karyotype"]:
                    for chrom in person1["karyotype"]:
                        chromosomes.append(chrom)
                else:
                    chromosomes = "No karyotype found"
                contents = read_html_file("karyotype.html").render(context={"chromosomes": chromosomes})
            else:
                contents = open("../Final project/html/error.html").read()
        elif action == "/chromosomeLength":
            chromrequest = instruction.split("&")
            specie = chromrequest[0][8:]
            number = chromrequest[1][7:]
            sci_specie = sci_name(specie)
            if sci_specie:
                person1 = data("/info/assembly/" + sci_specie)
                length = person1["top_level_region"][int(number)]["length"]
                contents = read_html_file("chromosomeLength.html").render(context={"length": length})
            else:
                contents = open("../Final project/html/error.html").read()

        elif action == "/geneSeq":
            gene = instruction[5:]
            s = Seq(gene)
            sequence = s.getting_seq()
            contents = read_html_file("geneSeq.html").render(context={"gene": gene, "sequence": sequence})
        elif action == "/geneInfo":
            gene = instruction[5:]
            s = Seq(gene)
            person = data("/lookup/symbol/homo_sapiens/" + gene)
            start, end, name = person["start"], person["end"], person["id"]
            length = s.length()
            contents = read_html_file("geneInfo.html").render(context={"gene": gene, "start": start, "end": end, "length": length, "id": name})
        elif action == "/geneCalc":
            gene = instruction[5:]
            s = Seq(gene)
            length = s.length()
            bases = ["A", "G", "T", "C"]
            results = []
            for i in bases:
                base = s.count(i)
                results.append(base)
            contents = read_html_file("geneCalc.html").render(context={"gene": gene, "length": length, "results": results})
        elif action == "/geneList":
            information = instruction.split("&")
            chromo = information[0][7:]
            start = information[1][6:]
            end = information[2][4:]
            person = data("/phenotype/region/homo_sapiens/" + chromo + ":" + start + "-" + end)
            names = []
            for i in range(len(person)):
                names.append(person[i]["id"])
            contents = read_html_file("geneList.html").render(context={"chromosome": chromo, "start": start, "end": end, "names": names})
        elif self.requestline.startswith("GET /favicon.ico"):
            contents = ""


        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()