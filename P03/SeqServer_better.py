import socket
from client1 import Client
from Seq2 import Seq
def ping(client):
    client.ping()
    return "OK!\n"
def get(client, n):
    seq = ["ATGGGCTTA", "TTAGGCTA", "TAGGTTCGA", "GCCTAGCGAT", "GATTCGATC"]
    client.get()
    return seq[n] + "\n"
def info(client, seq_str):
    s = Seq(seq_str)
    client.info()
    return f"Sequence {seq_str}\nTotal Length: {s.len()}\nA: {s.count('A')}\nC: {s.count('C')}\nG: {s.count('G')}\nT: {s.count('T')}\n"
def comp(client, seq_str):
    s = Seq(seq_str)
    client.comp()
    return s.comp() + "\n"
def rev(client, seq_str):
    s = Seq(seq_str)
    client.rev()
    return s.rev() + "\n"

def read_fasta(client, file):
    client.gene()
    s = Seq(file)
    return s.read_fasta("../Sequences/" + file + ".txt") + "\n"


PORT = 8081
IP = "127.0.0.1"

c = Client(IP, PORT)
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.bind((IP, PORT))
ls.listen()

print("SEQ server configured!")

while True:
    print("Waiting for clients")
    (rs, address) = ls.accept()
    msg = rs.recv(2048).decode("utf-8")

    command, *args = msg.split()
    if command == "PING":
        nmsg = ping(c)
    elif command == "GET":
        nmsg = get(c, int(args[0]))
    elif command == "INFO":
        nmsg = info(c, args[0])
    elif command == "COMP":
        nmsg = comp(c, args[0])
    elif command == "REV":
        nmsg = rev(c, args[0])
    elif command == "GENE":
        nmsg = read_fasta(c, args[0])
    # Add other commands...
    else:
        nmsg = "Invalid command\n"

    print(nmsg)
    rs.send(nmsg.encode())

    rs.close()

ls.close()
