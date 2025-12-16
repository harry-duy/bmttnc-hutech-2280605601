import socket
import ssl

def start_client():
    # Tạo socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrap với SSL, yêu cầu xác thực certificate của server
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    # Tải chứng chỉ của CA, hoặc trong trường hợp này là chứng chỉ tự ký của server
    context.load_verify_locations('certificates/server-cert.crt')
    
    ssl_client = context.wrap_socket(client_socket, server_hostname='localhost')
    
    try:
        # Kết nối đến server
        ssl_client.connect(('localhost', 8443))
        print("Đã kết nối đến SSL Server")
        
        # Nhập và gửi tin nhắn
        message = input("Nhập tin nhắn: ")
        ssl_client.send(message.encode('utf-8'))
        
        # Nhận phản hồi
        response = ssl_client.recv(1024).decode('utf-8')
        print(f"Server phản hồi: {response}")
        
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        ssl_client.close()

if __name__ == "__main__":
    start_client()