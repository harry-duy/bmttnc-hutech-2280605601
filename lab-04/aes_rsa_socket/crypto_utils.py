from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_aes(message: str, aes_key: bytes) -> str:
    """Encrypts a message using AES-CBC and returns a base64 encoded string."""
    cipher = AES.new(aes_key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return f"{iv}:{ct}"

def decrypt_aes(encrypted_message: str, aes_key: bytes) -> str:
    """Decrypts a base64 encoded AES-CBC message."""
    iv, ct = encrypted_message.split(':', 1)
    iv_bytes = base64.b64decode(iv)
    ct_bytes = base64.b64decode(ct)
    cipher = AES.new(aes_key, AES.MODE_CBC, iv_bytes)
    pt_bytes = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return pt_bytes.decode('utf-8')