from client0 import Client

IP = "212.128.255.104"
PORT = 8080
c = Client(IP, PORT)

for i in range(5):
    msg = "Message " + str(i)
    response = c.talk(msg)

    print(f"To server: {msg}")
    print(f"From server: {response}")
