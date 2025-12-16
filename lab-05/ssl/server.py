import socket
import ssl

def start_server():
    # Tạo socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind và listen
    server_socket.bind(('localhost', 8443))
    server_socket.listen(5)
    
    # Wrap với SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('certificates/server-cert.crt', 'certificates/server-key.key')
    
    ssl_server = context.wrap_socket(server_socket, server_side=True)
    
    print("SSL Server đang chạy trên port 8443...")
    print("Đợi kết nối từ client...\n")
    
    while True:
        try:
            client_socket, address = ssl_server.accept()
            print(f"Kết nối từ: {address}")
            
            # Nhận dữ liệu
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Client gửi: {data}")
            
            # Gửi phản hồi
            response = f"Server đã nhận: {data}"
            client_socket.send(response.encode('utf-8'))
            
            client_socket.close()
            print("Đã đóng kết nối\n")
            
        except KeyboardInterrupt:
            print("\nĐang dừng server...")
            break
        except Exception as e:
            print(f"Lỗi: {e}")
    
    ssl_server.close()

if __name__ == "__main__":
    start_server()