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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response