from PIL import Image

def decode_message(image_path):
    """
    Giải mã tin nhắn từ ảnh
    :param image_path: Đường dẫn ảnh đã mã hóa
    :return: Tin nhắn đã giấu
    """
    img = Image.open(image_path)
    width, height = img.size
    
    binary_message = ""
    message = ""
    
    # Đọc LSB từ mỗi pixel
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            
            # Đọc từng kênh màu (R, G, B)
            for i in range(3): 
                binary_message += str(pixel[i] & 1)
                
                # Khi đủ 8 bit, chuyển thành ký tự
                if len(binary_message) == 8:
                    char_code = int(binary_message, 2)
                    if char_code == 0:  # Ký tự kết thúc (null)
                        return message # Kết thúc và trả về tin nhắn
                    message += chr(char_code)
                    binary_message = "" # Reset để đọc ký tự tiếp theo
    
    return message

if __name__ == "__main__":
    image_path = input("Nhập đường dẫn ảnh cần giải mã: ")

    try:
        decoded_message = decode_message(image_path)
        if decoded_message:
            print(f"\nTin nhắn đã giấu: {decoded_message}")
        else:
            print("\nKhông tìm thấy tin nhắn nào trong ảnh.")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file ảnh '{image_path}'.")
    except Exception as e:
        print(f"Đã xảy ra lỗi không mong muốn: {e}")