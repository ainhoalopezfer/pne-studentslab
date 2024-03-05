import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True: # always running and accepting client
    (rs, address) = ls.accept()  #creates specific socket for the client, accepting only one client

    print(f"Client {address}")

    msg = rs.recv(2048).decode("utf-8")
    print("The client says..." + msg)

    newMsg = "I'm a happy server"
    rs.send(newMsg.encode())

    rs.close()


# -- Close the socket
ls.close()
