import http.client
import http.server
import json
from pathlib import Path
import termcolor
import socketserver
import jinja2 as j

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class Seq:
    def __init__(self, gene):
        self.gene = gene

    def getting_seq(self):
        f = Files("")
        person = f.data("/lookup/symbol/homo_sapiens/" + self.gene)
        name = person["id"]
        person1 = f.data("sequence/id/" + name)
        seq = person1["seq"]
        return seq
    def length(self):
        seq = self.getting_seq()
        return len(seq)

    def count(self, b):
        seq = self.getting_seq()
        base = seq.count(b)
        percentage = round((base/len(seq) * 100), 2)

        return b + ": " + str(base) + " (" + str(percentage) + "%)"

    def sci_name(self, specie):
        specie = specie.replace("+", " ").strip().lower()
        sci_specie = ""
        f = Files("")
        person = f.data("/info/species")
        for i in person["species"]:
            if i["display_name"].lower() == specie.lower():
                sci_specie = i["name"]
        return sci_specie

class Files():
    def __init__(self, filename):
        self.filename = filename

    def data(self, ENDPOINT):
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
    def read_html_file(self):
        contents = Path("html/" + self.filename).read_text()
        contents = j.Template(contents)
        return contents

    def json_file(self, name):
        json_dict = {}
        if type(name) == list:
            for index, content in enumerate(name):
                json_dict[index] = content
        elif type(name) == str or type(name) == int:
            json_dict["1"] = name
        elif type(name) == dict:
            json_dict = name
        with open(self.filename, "w") as f:
            json.dump(json_dict, f)
            f.close()
        contents = Path(self.filename).read_text()

        return contents
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        request = self.requestline.split(" ")
        status_line = 200
        action = request[1]
        application_type, content_type, instruction, contents, s, gene = "", "html", "", "", "", ""
        if "?" in request[1]:
            separate = request[1].split("?")
            action, instruction = separate[0], separate[1]
            if "json=1" in request[1]:
                content_type = "application/json"
                application_type = separate[2]

        f = Files(action[1:] + "." + content_type.removeprefix("application/"))
        if "=" in instruction:
            gene = instruction.split("=")
            s = Seq(gene[1])
        if action == "/" or action == "/index.html":
            content_type = "html"
            contents = open("../Final project/html/index.html").read()
        elif action == "/listSpecies":
            person = f.data("/info/species")
            total = len(person["species"])
            number = total
            if instruction != "limit=":
                number = instruction[6:]
                number = int(number)
            names = []
            for i in range(number):
                name = person["species"][i]["common_name"].capitalize()
                names.append(name)
            names = sorted(names)

            if application_type == "json=1":
               contents = f.json_file(names)
            else:
                contents = f.read_html_file().render(context={"total": total, "number": number, "list": names})
        elif action == "/karyotype":
            specie = instruction[8:]
            chromosomes = []
            sci_specie = s.sci_name(specie)
            if sci_specie:
                person1 = f.data("/info/assembly/" + sci_specie)
                if person1["karyotype"]:
                    for chrom in person1["karyotype"]:
                        chromosomes.append(chrom)
                else:
                    chromosomes = "No karyotype found"
                if application_type == "json=1":
                    contents = f.json_file(chromosomes)
                else:
                    contents = f.read_html_file().render(context={"chromosomes": chromosomes})
            else:
                contents = open("../Final project/html/error.html").read()
                status_line = 404
        elif action == "/chromosomeLength":
            chromrequest = instruction.split("&")
            specie = chromrequest[0][8:]
            number = chromrequest[1][7:]
            sci_specie = s.sci_name(specie)
            if sci_specie:
                person1 = f.data("/info/assembly/" + sci_specie)
                length = person1["top_level_region"][int(number)]["length"]
                if application_type == "json=1":
                    contents = f.json_file(length)
                else:
                    contents = f.read_html_file().render(context={"length": length})
            else:
                contents = open("../Final project/html/error.html").read()
                status_line = 404

        elif action == "/geneSeq":
            gene = instruction[5:]
            s = Seq(gene)
            sequence = s.getting_seq()
            gene_dict = {"gene": gene, "sequence": sequence}
            if application_type == "json=1":
                contents = f.json_file(gene_dict)
            else:
                contents = f.read_html_file().render(context=gene_dict)
        elif action == "/geneInfo":
            person = f.data("/lookup/symbol/homo_sapiens/" + gene[1])
            start, end, name = person["start"], person["end"], person["id"]
            length = s.length()
            chromosomes_dict = {"gene": gene, "start": start, "end": end, "length": length, "id": name}
            if application_type == "json=1":
                contents = f.json_file(chromosomes_dict)
            else:
                contents = f.read_html_file().render(context=chromosomes_dict)
        elif action == "/geneCalc":
            length = s.length()
            bases = ["A", "G", "T", "C"]
            results = []
            for i in bases:
                base = s.count(i)
                results.append(base)
            calc_dict = {"gene": gene[1], "length": length, "results": results}
            if application_type == "json=1":
                contents = f.json_file(calc_dict)
            else:
                contents = f.read_html_file().render(context=calc_dict)
        elif action == "/geneList":
            information = instruction.split("&")
            chromo = information[0][7:]
            start = information[1][6:]
            end = information[2][4:]
            person = f.data("/phenotype/region/homo_sapiens/" + chromo + ":" + start + "-" + end)
            names = []
            for i in range(len(person)):
                names.append(person[i]["id"])
            list_dict = {"chromosome": chromo, "start": start, "end": end, "names": names}
            if application_type == "json=1":
                contents = f.json_file(list_dict)
            else:
                contents = f.read_html_file().render(context=list_dict)
        else:
            contents = open("../Final project/html/error.html").read()
            status_line = 404


        self.send_response(status_line)  # -- Status line: OK!
        termcolor.cprint("Status line: " + str(status_line), "blue")

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

