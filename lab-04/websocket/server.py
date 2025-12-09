import tornado.ioloop
import tornado.web
import tornado.websocket
import random
import asyncio

clients = set()
fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Strawberry', 'Grape', 'Watermelon', 'Pineapple']

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    
    def open(self):
        clients.add(self)
        print(f"[SERVER] New client connected. Total clients: {len(clients)}")
    
    def on_close(self):
        clients.remove(self)
        print(f"[SERVER] Client disconnected. Total clients: {len(clients)}")

async def send_fruit():
    while True:
        await asyncio.sleep(3)
        # Don't broadcast if there are no clients
        if not clients:
            continue

        fruit = random.choice(fruits)
        print(f"[SERVER] Broadcasting: {fruit}")
        # Iterate over a copy to avoid issues with a changing set during iteration
        for client in list(clients):
            try:
                client.write_message(fruit)
            except tornado.websocket.WebSocketClosedError:
                # The on_close handler will be called, which removes the client.
                print(f"[SERVER] A client connection was closed. It will be removed.")

def make_app():
    return tornado.web.Application([
        (r"/ws", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("[SERVER] WebSocket server started on ws://localhost:8888/ws")
    
    # Start the fruit broadcasting task
    tornado.ioloop.IOLoop.current().spawn_callback(send_fruit)
    tornado.ioloop.IOLoop.current().start()