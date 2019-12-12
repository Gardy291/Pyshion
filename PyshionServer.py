import socket
from Lex import parser
HEADERSIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    while True:
        var =clientsocket.recv(4096).decode('utf-8')
        print(f"Received {var} from Client")
    clientsocket.close()
    print("Disconnect")