import asyncio
import websockets

async def receive_fruits():
    uri = "ws://localhost:8888/ws"
    while True:  # Outer loop for reconnection
        try:
            print(f"[CLIENT] Connecting to {uri}...")
            async with websockets.connect(uri) as websocket:
                print("[CLIENT] Connected! Waiting for fruits...")
                while True:
                    # This will wait for a message from the server
                    message = await websocket.recv()
                    print(f"[CLIENT] Received: {message}")
        except (websockets.exceptions.ConnectionClosed, websockets.exceptions.ConnectionClosedError):
            print("[CLIENT] Connection closed by server.")
        except (ConnectionRefusedError, OSError):
            print("[CLIENT] Connection failed. Server might be down.")
        except Exception as e:
            print(f"[CLIENT] An unexpected error occurred: {e}")
        
        print("[CLIENT] Attempting to reconnect in 5 seconds...")
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(receive_fruits())
