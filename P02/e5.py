from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.99" # your IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

s = Seq()

...
# -- Send a message to the server
sender = c.talk("Sending a FRAT1 Gene to the server...")
print(f"To server: Sending a FRAT1 Gene to the server...")
response = c.talk(s.read_fasta("../Sequences/FRAT1.txt"))
print(f"From server:\n{response}")

sections = s.first_n_str(5, "../Sequences/FRAT1.txt", 10)

for index, section in enumerate(sections):
    sec = c.talk(f"Fragment {index + 1}: {section}")
    print(f"Fragment {index}: {section}")
...