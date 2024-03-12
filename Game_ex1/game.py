import socket
import random
from player import Player

class NumberGuesser:
    def __init__(self):
        number = random.randint(1, 100)
        self.number = number
        pass
    def guessing(self, num, attempt, attempts):
        if num == self.number:
            ans = f"You won after {attempt} attempts, Attempts list: {attempts}"
        elif num > self.number:
            ans = "Lower\n"
        elif num < self.number:
            ans = "Higher\n"
        return ans


PORT = 8081
IP = "127.0.0.1"

p = Player(IP, PORT)
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.bind((IP, PORT))
ls.listen()
n = NumberGuesser()

print("SEQ server configured!")

while True:
    print("Waiting for players")
    (rs, address) = ls.accept()
    attempt = 0
    attempts = []

    flag = True
    while flag:

        msg = rs.recv(2048).decode("utf-8")
        print(f"Number guessed: {msg}")

        try:
            msg = int(msg)
            attempt += 1
            attempts.append(msg)
            if 1 <= msg <= 100:
                nmsg = n.guessing(msg, attempt, attempts)
                if nmsg == f"You won after {attempt} attempts, Attempts list: {attempts}":
                    flag = False

                print(nmsg)
                rs.send(nmsg.encode())
        except ValueError:
            nmsg = "Try again"


    rs.close()

ls.close()
 #

