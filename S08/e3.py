import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.102" # depends on the computer the server is running

while True:
    # -- Ask the user for the message
    message = input("Write a message")

    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # -- Establish the connection to the Server
    s.connect((IP, PORT))
    # -- Send the user message
    s.send(str.encode(message))

    # Receive data from the server
    msg = s.recv(2048)
    print("MESSAGE FROM THE SERVER:\n")
    print(msg.decode("utf-8"))

    # -- Close the socket
    s.close()