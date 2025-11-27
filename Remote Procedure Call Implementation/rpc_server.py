import socket

HOST = "127.0.0.1"
PORT = 9000

print(f"RPC Server running on port {PORT}...")

# Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

while True:
    # Receive two numbers from client
    data = conn.recv(1024).decode()
    if not data:
        break

    a, b = map(int, data.split())

    # Perform operations
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else 0

    # Prepare response
    response = (
        f"Addition : {addition}\n"
        f"Substraction : {subtraction}\n"
        f"Multiplication : {multiplication}\n"
        f"Division : {division}"
    )

    conn.send(response.encode())

conn.close()
s.close()
