from client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.99" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)
