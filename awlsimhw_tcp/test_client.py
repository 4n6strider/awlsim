import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 5000))

while True:
    try:
        received = sock.recv(1024)
        print repr(received)
        time.sleep(0.5)
    except KeyboardInterrupt:
        pass