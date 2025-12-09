import hashlib

def sha3_hash(message):
    return hashlib.sha3_256(message.encode()).hexdigest()

if __name__ == "__main__":
    message = input("Enter message to hash: ")
    hash_result = sha3_hash(message)
    print(f"SHA-3 Hash: {hash_result}")