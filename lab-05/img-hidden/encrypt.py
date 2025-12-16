from PIL import Image

def encode_message(image_path, message, output_path):
    """
    Giấu tin nhắn vào ảnh
    :param image_path: Đường dẫn ảnh gốc
    :param message: Tin nhắn cần giấu
    :param output_path: Đường dẫn ảnh output
    """
    # Mở ảnh
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    
    # Thêm ký tự kết thúc
    message += chr(0)
    
    # Chuyển message thành binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    if len(binary_message) > width * height * 3:
        raise ValueError("Tin nhắn quá dài cho ảnh này!")
    
    data_index = 0
    
    # Giấu tin vào LSB của mỗi pixel
    for y in range(height):
        for x in range(width):
            if data_index < len(binary_message):
                pixel = list(img.getpixel((x, y)))
                
                # Giấu vào từng kênh màu (R, G, B)
                for i in range(3):
                    if data_index < len(binary_message):
                        # Thay đổi LSB
                        pixel[i] = (pixel[i] & 0xFE) | int(binary_message[data_index])
                        data_index += 1
                
                encoded.putpixel((x, y), tuple(pixel))
            else:
                break
        if data_index >= len(binary_message):
            break
    
    # Lưu ảnh đã mã hóa
    encoded.save(output_path)
    print(f"Đã giấu tin thành công vào: {output_path}")

if __name__ == "__main__":
    try:
        image_path = input("Nhập đường dẫn ảnh gốc: ")
        message = input("Nhập tin nhắn cần giấu: ")
        output_path = input("Nhập đường dẫn ảnh output (ví dụ: encoded_image.png): ")

        if not output_path.lower().endswith('.png'):
            print("Cảnh báo: Nên lưu ảnh ở định dạng lossless (như .png) để tránh làm hỏng tin nhắn đã giấu.")

        encode_message(image_path, message, output_path)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file ảnh '{image_path}'.")
    except PermissionError:
        print(f"Lỗi: Không có quyền truy cập. '{image_path}' có thể là một thư mục, không phải file ảnh.")
    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Đã xảy ra lỗi không mong muốn: {e}")