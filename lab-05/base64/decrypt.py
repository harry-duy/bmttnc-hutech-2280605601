import base64
from binascii import Error as BinasciiError

def decrypt_base64(base64_message):
    """Giải mã chuỗi Base64"""
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('utf-8')
    return message

if __name__ == "__main__":
    # Nhập thông điệp Base64 cần giải mã
    base64_message = input("Nhập thông điệp Base64 cần giải mã: ")
    
    try:
        # Giải mã
        decrypted = decrypt_base64(base64_message)
        
        print(f"\nThông điệp Base64: {base64_message}")
        print(f"Thông điệp đã giải mã: {decrypted}")
    except BinasciiError:
        print("Lỗi: Chuỗi nhập vào không phải là định dạng Base64 hợp lệ.")
    except Exception as e:
        print(f"Đã xảy ra lỗi không mong muốn: {e}")