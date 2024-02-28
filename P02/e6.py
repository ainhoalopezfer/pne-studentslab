from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.99" # your IP address
PORT1, PORT2 = 8080, 8081

# -- Create a client object
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

s = Seq()

...
# -- Send a message to the server
sender1 = c1.talk("Sending a FRAT1 Gene to the server...")
sender2 = c2.talk("Sending a FRAT1 Gene to the server...")
print(f"To server: Sending a FRAT1 Gene to the server...")

sections = s.first_n_str(10, "../Sequences/FRAT1.txt", 10)

for index, section in enumerate(sections):
    if (index+1)%2 == 0:
        sec = c2.talk(f"Fragment {index + 1}: {section}")
    else:
        sec = c1.talk(f"Fragment {index + 1}: {section}")

    print(f"Fragment {index+1}: {section}")
...