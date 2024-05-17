import http.client
import json
import socketserver
import termcolor

PORT = 8080
SERVER = "localhost"

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)
def connection(ENDPOINT):
    try:
        conn.request("GET", ENDPOINT)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    if "json=1" in ENDPOINT:
        data1 = r1.read().decode("utf-8")
        person = json.loads(data1)

    return person

print(connection("/listSpecies?limit=12?json=1"))

