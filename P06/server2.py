import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq2 import Seq
import os

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        seq = ""
        s = Seq(seq)
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        import jinja2 as j
        def read_html_file(filename):
            contents = Path("html/" + filename).read_text()
            contents = j.Template(contents)
            return contents

        # Message to send back to the client
        if self.requestline.startswith("GET / ") or self.requestline.startswith("GET /index"):
            contents = Path("../P06/html/index.html").read_text()
        elif self.requestline.startswith("GET /ping?"):
            contents = Path("../P06/html/ping.html").read_text()

        elif self.requestline.startswith("GET /actions?sequences"):
            dict = {"0": "ACGTAGTCAGTAGTAGCTAGC", "1": "GATCCCAGTTAAGA", "2": "ACTGTGGGCATATAATCAGCGAGCA", "3": "TCAGTAGCTAGCTAGCTAGTCAGCTAGC", "4": "CGGCTAGCTAGCTAGTCGATCGATCGATGCA"}
            num = self.requestline[23:]
            num = num[0]
            if num in dict:
                sequence = dict[num]
                contents = read_html_file("sequences.html").render(context={"name": num, "todisplay": sequence})

        elif self.requestline.startswith("GET /actions?genes"):
            list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
            name = self.requestline[19:]
            name = name[:-9]
            if name in list:
                text = s.read_fasta(f"../Sequences/{name}.txt")
                contents = read_html_file("genes.html").render(context={"name": name, "todisplay": text})

        elif self.requestline.startswith("GET /actions?msg"):
            new = self.requestline.split("&")
            msg = new[0]
            seq = msg[17:]
            op = new[1]
            op = op[9:-9]
            result = ""
            s = Seq(seq)
            if op == "info":
                result = f"""Length of sequence: {str(s.length())}<br>
A: {s.count("A")}<br>
C: {s.count("C")}<br>
T: {s.count("T")}<br>
G: {s.count("G")}"""
            elif op == "comp":
                result = s.comp()
            elif op == "rev":
                result = s.rev()
            contents = read_html_file("operation.html").render(context={"sequence": seq, "operation": op, "results": result})

        else:
            contents = Path("../S14/error.html").read_text()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
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
