from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.99" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

s = Seq()

...
# -- Send a message to the server
sender = c.talk(f"Sending a FRAT1 Gene to the server...")
print(f"To server: {sender}")
response = c.talk(s.read_fasta("../Sequences/FRAT1.txt"))
print(f"From server:\n{response}")
...