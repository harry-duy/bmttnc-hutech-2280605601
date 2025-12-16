import base64

def encrypt_base64(message):
    """Mã hóa chuỗi thành Base64"""
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message

if __name__ == "__main__":
    # Nhập thông điệp cần mã hóa
    message = input("Nhập thông điệp cần mã hóa: ")
    
    # Mã hóa
    encrypted = encrypt_base64(message)
    
    print(f"\nThông điệp gốc: {message}")
    print(f"Thông điệp đã mã hóa Base64: {encrypted}")