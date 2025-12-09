from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
import socket

# 1. Set up socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 2. Connect to the server
    client_socket.connect(('localhost', 6666))
    print("[CLIENT] Connected to server.")

    with client_socket:
        # 3. Receive the server's public key
        server_public_key_bytes = client_socket.recv(4096)
        if not server_public_key_bytes:
            print("[CLIENT] Did not receive server public key. Server may have closed connection.")
        else:
            server_public_key = serialization.load_pem_public_key(server_public_key_bytes)
            print("[CLIENT] Received server public key.")

            # 4. Generate client keys using server's parameters
            parameters = server_public_key.parameters()
            client_private_key = parameters.generate_private_key()
            client_public_key = client_private_key.public_key()

            # 5. Send client's public key to the server
            client_public_key_pem = client_public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            client_socket.sendall(client_public_key_pem)
            print("[CLIENT] Sent public key to server.")

            # 6. Generate shared key
            shared_key = client_private_key.exchange(server_public_key)

            # 7. Derive a final key from the shared secret
            derived_key = HKDF(
                algorithm=hashes.SHA256(),
                length=32,
                salt=None,
                info=b'handshake data',
            ).derive(shared_key)

            print(f"[CLIENT] Shared key derived: {derived_key.hex()}")
            print("[CLIENT] Key exchange completed. A secure channel can now be established.")
            print("[CLIENT] Example secure message: This is a secure communication!")

except ConnectionRefusedError:
    print("[CLIENT] Connection failed. Is the server running on localhost:6666?")
except Exception as e:
    print(f"[CLIENT] An error occurred: {e}")

print("[CLIENT] Client shutting down.")