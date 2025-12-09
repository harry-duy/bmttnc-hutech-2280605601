from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import socket

# 1. Generate DH parameters and server keys
print("[SERVER] Generating DH parameters and keys...")
parameters = dh.generate_parameters(generator=2, key_size=2048)
server_private_key = parameters.generate_private_key()
server_public_key = server_private_key.public_key()

# Serialize server public key to send to client
server_public_key_pem = server_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# 2. Set up socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 6666))
server_socket.listen(1)
print("[SERVER] Waiting for client connection on localhost:6666...")

try:
    client_socket, address = server_socket.accept()
    with client_socket:
        print(f"[SERVER] Client {address} connected")

        # 3. Send server's public key to the client
        client_socket.sendall(server_public_key_pem)
        print("[SERVER] Sent public key to client.")

        # 4. Receive client's public key
        client_public_key_bytes = client_socket.recv(4096)
        if not client_public_key_bytes:
            print("[SERVER] Client disconnected before sending its key.")
        else:
            client_public_key = serialization.load_pem_public_key(client_public_key_bytes)
            print("[SERVER] Received public key from client.")

            # 5. Generate shared key
            shared_key = server_private_key.exchange(client_public_key)

            # 6. Derive a final key from the shared secret
            derived_key = HKDF(
                algorithm=hashes.SHA256(),
                length=32,
                salt=None,
                info=b'handshake data',
            ).derive(shared_key)

            print(f"[SERVER] Shared key derived: {derived_key.hex()}")
            print("[SERVER] Key exchange completed successfully!")

except Exception as e:
    print(f"[SERVER] An error occurred: {e}")
finally:
    server_socket.close()
    print("[SERVER] Server socket closed.")