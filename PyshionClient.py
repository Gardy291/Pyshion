import socket
from Texts import *
from Lex import parser

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
Texts.intro()

while True:
    i = input('>>>')
    s.sendall(i.encode())
    parser.parse(i)
