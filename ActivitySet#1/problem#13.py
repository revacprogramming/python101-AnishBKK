#netprog_ex-req-resp-cycle
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "www.data.pr4e.org"
PORT = 80
sock.connect((HOST, PORT))
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n".encode()
sock.send(cmd)

while True:
    data = sock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

sock.close()
