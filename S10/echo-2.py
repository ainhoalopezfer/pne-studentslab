import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.255.104" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
i = 1
while True: # always running and accepting client
    (rs, address) = ls.accept()  #creates specific socket for the client, accepting only one client

    print(f"Connection {i}. Client IP, PORT {address}")

    msg = rs.recv(2048).decode("utf-8")
    print("The client says..." + msg)

    newMsg = "Message received:" + msg + "\n"
    rs.send(newMsg.encode())

    rs.close()
    i += 1

ls.close()
