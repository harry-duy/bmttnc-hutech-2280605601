import hashlib

def md5_hash(message):
    return hashlib.md5(message.encode()).hexdigest()

if __name__ == "__main__":
    message = input("Enter message to hash: ").strip()
    hash_result = md5_hash(message)
    print(f"MD5 Hash: {hash_result}")