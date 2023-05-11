from socket import *

from ec import variable

client = socket(AF_INET, SOCK_STREAM)
client.connect(variable.ip_port)

while True:
    data = input(">>").strip()
    client.send(data.encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")
    print(msg)
