import socket
import termcolor
from Seq1 import Seq
class Client:
    def __init__(self, IP, PORT):
        self.ip = IP
        self.port = PORT
        pass

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def ping(self):
        print(termcolor.colored("PING Command!", "green"))

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response

    def get(self):
        print(termcolor.colored("GET!", "green"))

    def info(self):
        print(termcolor.colored("INFO", "green") + "\nNew sequence created!")

    def comp(self):
        print(termcolor.colored("COMP", "green") + "\nNew sequence created!")

    def rev(self):
        print(termcolor.colored("REV", "green") + "\nNew sequence created!")

    def gene(self):
        print(termcolor.colored("GENE", "green") + "\nNul sequence created!")