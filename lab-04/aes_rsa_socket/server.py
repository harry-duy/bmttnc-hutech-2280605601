import socket
import threading
import os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from crypto_utils import encrypt_aes, decrypt_aes

PRIVATE_KEY_FILE = "server_private.pem"
PUBLIC_KEY_FILE = "server_public.pem"

def load_or_generate_rsa_keys():
    """Loads RSA keys from files, or generates and saves them if they don't exist."""
    if os.path.exists(PRIVATE_KEY_FILE) and os.path.exists(PUBLIC_KEY_FILE):
        print("[INFO] Loading existing RSA keys...")
        with open(PRIVATE_KEY_FILE, 'rb') as f:
            private_key = RSA.import_key(f.read())
        with open(PUBLIC_KEY_FILE, 'rb') as f:
            public_key = RSA.import_key(f.read())
    else:
        print("[INFO] Generating new RSA keys...")
        key = RSA.generate(2048)
        private_key = key
        public_key = key.publickey()
        with open(PRIVATE_KEY_FILE, 'wb') as f:
            f.write(private_key.export_key())
        with open(PUBLIC_KEY_FILE, 'wb') as f:
            f.write(public_key.export_key())
    return private_key, public_key

clients = []
aes_keys = {}
lock = threading.Lock()

HOST = 'localhost'
PORT = 5556
BUFFER_SIZE = 4096

def remove_client(client_socket):
    """Safely removes a client from the lists and closes the socket."""
    with lock:
        if client_socket in clients:
            clients.remove(client_socket)
            print(f"[DISCONNECTED] Client removed. Active connections: {len(clients)}")
        if client_socket in aes_keys:
            del aes_keys[client_socket]
    client_socket.close()

def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")
    
    # Gửi public key cho client
    client_socket.send(public_key.export_key())
    
    # Nhận AES key đã mã hóa từ client
    encrypted_aes_key = client_socket.recv(BUFFER_SIZE)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)
    
    with lock:
        aes_keys[client_socket] = aes_key
        clients.append(client_socket)
    
    print(f"[ACTIVE CONNECTIONS] {len(clients)}")
    
    try:
        while True:
            try:
                encrypted_msg = client_socket.recv(BUFFER_SIZE).decode()
                if not encrypted_msg:
                    break # Client closed connection gracefully
                message = decrypt_aes(encrypted_msg, aes_key)
                print(f"[{address[0]}:{address[1]}] {message}")
                # Prepare message to be broadcasted
                broadcast_message = f"[{address[0]}:{address[1]}] {message}"
                broadcast(broadcast_message, client_socket)
            except (ConnectionResetError, ConnectionAbortedError):
                print(f"[ERROR] {address} disconnected abruptly while receiving.")
                break
            except Exception as e:
                print(f"[ERROR] An error occurred with {address}: {e}")
                break
    finally:
        # Ensure client is removed safely upon exit
        print(f"[CONNECTION CLOSING] {address}")
        remove_client(client_socket)

def broadcast(message, sender_socket):
    # Create a snapshot of clients to message, to avoid holding the lock during I/O
    with lock:
        # We need both the client socket and its AES key
        recipients = {client: aes_keys[client] for client in clients if client != sender_socket and client in aes_keys}

    clients_to_remove = []
    for client, key in recipients.items():
        try:
            encrypted_msg = encrypt_aes(message, key)
            client.send(encrypted_msg.encode())
        except (ConnectionResetError, BrokenPipeError, OSError): # OSError can happen if socket is closed
            print(f"[BROADCAST FAILED] Marking client for removal.")
            clients_to_remove.append(client)

    # Now, remove the clients that failed
    for client in clients_to_remove:
        remove_client(client)

def start_server():
    global private_key, public_key
    private_key, public_key = load_or_generate_rsa_keys()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow reusing the address to avoid "Address already in use" errors on quick restarts
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print("[STARTING] Server is starting...")
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    
    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    private_key, public_key = None, None # Initialize as globals
    start_server()