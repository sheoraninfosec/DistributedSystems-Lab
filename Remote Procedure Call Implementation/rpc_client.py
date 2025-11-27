import socket

HOST = "127.0.0.1"
PORT = 9000

print("Connected to RPC Server")

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Take input
a = input("Enter first Number : ")
b = input("Enter second Number : ")

# Send numbers to server
s.send(f"{a} {b}".encode())

# Receive response
data = s.recv(1024).decode()

print("\n" + data)

s.close()
