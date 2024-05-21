import socket
import threading

# Constants
BLOCK_SIZE = 20 * 1024  # Replace with the actual last two digits of your registration number, here 20KB for example

# Server function to handle each client
def handle_client(client_socket):
    try:
        while True:
            # Receive the command from the client
            command = client_socket.recv(1024).decode()
            print(f"Received command: {command}")

            if not command:
                break

            command = command.split()
            if command[0] == 'UPLOAD':
                filename = command[1]
                receive_file(client_socket, filename)
            elif command[0] == 'DOWNLOAD':
                filename = command[1]
                send_file(client_socket, filename)
            else:
                client_socket.sendall(b"Invalid command\n")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def receive_file(client_socket, filename):
    print(f"Starting file upload: {filename}")
    total_bytes_received = 0
    with open(filename, 'wb') as f:
        while True:
            data = client_socket.recv(BLOCK_SIZE)
            if not data:
                break
            f.write(data)
            total_bytes_received += len(data)
    print(f"Finished receiving file: {filename}, total bytes received: {total_bytes_received}")

def send_file(client_socket, filename):
    print(f"Starting file download: {filename}")
    try:
        total_bytes_sent = 0
        with open(filename, 'rb') as f:
            while (block := f.read(BLOCK_SIZE)):
                client_socket.sendall(block)
                total_bytes_sent += len(block)
        print(f"Finished sending file: {filename}, total bytes sent: {total_bytes_sent}")
    except FileNotFoundError:
        client_socket.sendall(b"File not found\n")
    except Exception as e:
        print(f"Error sending file: {e}")

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Localhost
    PORT = 12345        # Port number
    start_server(HOST, PORT)
