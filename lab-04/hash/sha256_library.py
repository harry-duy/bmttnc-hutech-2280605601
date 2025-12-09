import hashlib

def sha256_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

if __name__ == "__main__":
    message = input("Enter message to hash: ").strip()
    hash_result = sha256_hash(message)
    print(f"SHA-256 Hash: {hash_result}")