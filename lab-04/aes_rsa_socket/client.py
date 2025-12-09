import socket
import threading
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from crypto_utils import encrypt_aes, decrypt_aes
aes_key = get_random_bytes(16)

HOST = 'localhost'
PORT = 5556
BUFFER_SIZE = 4096

def receive_messages(client_socket, stop_event):
    while not stop_event.is_set():
        try:
            encrypted_msg = client_socket.recv(BUFFER_SIZE).decode()
            if encrypted_msg:
                message = decrypt_aes(encrypted_msg, aes_key)
                print(f"\n{message}\n> ", end="")
            else:  # Server closed connection gracefully
                print("\n[INFO] Server has closed the connection. Press Enter to exit.")
                stop_event.set()
        except (ConnectionResetError, ConnectionAbortedError):
            print("\n[DISCONNECTED] Connection to server lost.")
            stop_event.set()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    # Nhận public key từ server
    public_key = RSA.import_key(client.recv(BUFFER_SIZE))
    
    # Mã hóa AES key bằng RSA public key và gửi cho server
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client.send(encrypted_aes_key)
    
    stop_event = threading.Event()
    # Tạo thread để nhận tin nhắn
    thread = threading.Thread(target=receive_messages, args=(client, stop_event))
    thread.start()
    
    # Gửi tin nhắn
    try:
        while not stop_event.is_set():
            message = input("> ")
            if message.lower() == 'quit':
                break
            if message:  # Only send non-empty messages
                encrypted_msg = encrypt_aes(message, aes_key)
                client.send(encrypted_msg.encode())
    finally:
        stop_event.set()
        client.close()
        print("Exiting...")

if __name__ == "__main__":
    start_client()