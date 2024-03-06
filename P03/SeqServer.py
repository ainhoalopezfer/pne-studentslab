import socket
from client1 import Client
from Seq2 import Seq

# Configure the Server's IP and PORT
PORT = 8082
IP = "127.0.0.1" # this IP address is local, so only requests from the same machine are possible

c = Client(IP, PORT)
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("SEQ server configured!")


def seq(n):
    seqs = ["AGCTAGCATGCT", "TCAGTCAGTCGAC", "CGATCGTAGTCAGC", "ACGTAGCTACTAGT", "AGCTGATAGCT"]
    return seqs[n]

while True: # always running and accepting client
    print("Waiting for clients")
    (rs, address) = ls.accept()  #creates specific socket for the client, accepting only one client

    msg = rs.recv(2048).decode("utf-8")

    if "PING" in msg:
        c.ping()
        nmsg = "OK! \n"

    elif "GET " in msg:
        n = msg[4:]
        n = int(n)
        c.get()
        nmsg = seq(n) + "\n"

    elif "INFO " in msg:
        seq = msg[5:]
        s = Seq(seq)
        c.info()
        nmsg = f"Sequence {seq}\nTotal Length: {s.len()}\nA: {s.count('A')}\nC: {s.count('C')}\nG: {s.count('G')}\nT: {s.count('T')}\n"

    elif "COMP " in msg:
        seq = msg[5:]
        s = Seq(seq)
        c.comp()
        nmsg = s.comp() + "\n"

    elif "REV " in msg:
        seq = msg[4:]
        s = Seq(seq)
        c.rev()
        nmsg = s.rev() + "\n"

    elif "GENE " in msg:
        filenames = ["U5", "ADA", "FXN", "FRAT1", "RNU6_269P"]
        c.gene()
        for file in filenames:
            if file in msg:
                s = Seq(seq)
                nmsg = s.read_fasta("../Sequences/" + file + ".txt") + "\n"

    print(nmsg)
    rs.send(nmsg.encode())


    rs.close()


# -- Close the socket
ls.close()

