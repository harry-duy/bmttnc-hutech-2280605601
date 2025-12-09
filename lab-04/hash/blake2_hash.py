import hashlib

def blake2_hash(message):
    return hashlib.blake2b(message.encode()).hexdigest()

if __name__ == "__main__":
    message = input("Enter message to hash: ").strip()
    hash_result = blake2_hash(message)
    print(f"BLAKE2 Hash: {hash_result}")