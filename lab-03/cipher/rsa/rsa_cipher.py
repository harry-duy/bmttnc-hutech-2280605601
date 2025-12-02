import rsa

class RSACipher:
    def __init__(self):
        pass
    
    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(2048)
        
        with open('cipher/rsa/keys/publicKey.pem', 'wb') as f:
            f.write(public_key.save_pkcs1())
        
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as f:
            f.write(private_key.save_pkcs1())
    
    def load_keys(self):
        with open('cipher/rsa/keys/publicKey.pem', 'rb') as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
        
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
        
        return public_key, private_key
    
    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('utf-8'), key)
    
    def decrypt(self, ciphertext, key):
        return rsa.decrypt(ciphertext, key).decode('utf-8')
    
    def sign(self, message, key):
        return rsa.sign(message.encode('utf-8'), key, 'SHA-256')
    
    def verify(self, message, signature, key):
        try:
            rsa.verify(message.encode('utf-8'), signature, key)
            return True
        except:
            return False