import socket

# Constants
BLOCK_SIZE = 20 * 1024  
def upload_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(f"UPLOAD {filename}".encode())
        with open(filename, 'rb') as f:
            while (block := f.read(BLOCK_SIZE)):
                client_socket.sendall(block)
        client_socket.shutdown(socket.SHUT_WR)  # Indicate that file upload is done
        print(f"Uploaded file: {filename}")

def download_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(f"DOWNLOAD {filename}".encode())
        with open(f"downloaded_{filename}", 'wb') as f:
            while True:
                data = client_socket.recv(BLOCK_SIZE)
                if not data:
                    break
                f.write(data)
        print(f"Downloaded file: {filename}")

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Server address
    PORT = 12345        # Server port

    # Example usage
    # Upload a file
    upload_file('cv.pdf')

    # Download the same file
    download_file('cv.pdf')
