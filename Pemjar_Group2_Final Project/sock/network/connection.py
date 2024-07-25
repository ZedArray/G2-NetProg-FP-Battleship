import socket
import select
import sys
import time
from threading import Thread, Lock

class Server:
    def __init__(self, ip_address='127.0.0.1', port=5001):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ip_address = ip_address
        self.port = port
        self.server.bind((self.ip_address, self.port))
        self.server.listen(100)
        self.list_of_clients = []
        self.queue = []
        self.lock = Lock()
        self.running = True

    def client_thread(self, conn, addr):
        while True:
            try:
                message = conn.recv(2048).decode()
                if message:
                    print(str(addr[1]) + ' ' + message)
                    message_to_send = str(addr[1]) + ' ' + message
                    with self.lock:
                        self.queue.append(message)
                        # self.broadcast(message_to_send, conn)
                else:
                    self.remove_connection(conn)
                    break
            except:
                continue

    def broadcast(self, message):
        for client in self.list_of_clients:
            try:
                client.send(message.encode())
            except:
                client.close()
                self.remove_connection(client)

    def send_message(self, message, connection):
        for client in self.list_of_clients:
            if client == connection:
                try:
                    client.send(message.encode())
                except:
                    client.close()
                    self.remove_connection(client)

    def remove_connection(self, connection):
        if connection in self.list_of_clients:
            self.list_of_clients.remove(connection)

    def run(self):
        while self.running:
            conn, addr = self.server.accept()
            self.list_of_clients.append(conn)
            print(str(addr[1]) + ' connected')
            Thread(target=self.client_thread, args=(conn, addr)).start()

    def get_queue(self):
        with self.lock:
            return self.queue.copy()

    def pop_queue(self):
        with self.lock:
            if not self.queue:
                print("queue is empty")
                return False
            else:
                self.queue.pop(0)
    def num_of_client(self):
        return len(self.list_of_clients)

    def stop(self):
        self.running = False
        self.server.close()
        self.run



class Client:
    def __init__(self, ip_address='127.0.0.1', port=5001):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip_address = ip_address
        self.port = port
        self.queue = []
        self.lock = Lock()

        try:
            self.server.connect((self.ip_address, self.port))
        except ConnectionRefusedError:
            print(f"Unable to connect to the server at {self.ip_address}:{self.port}")
            sys.exit()

        self.running = True
        self.recv_thread = Thread(target=self.recv_msg)
        self.recv_thread.start()

    def send_msg(self, msg):
        self.server.send(msg.encode())

    def recv_msg(self):
        while self.running:
            data = self.server.recv(2048).decode()
            if not data:
                print("Server closed connection")
                self.running = False
                sys.exit()
            self.queue.append(data)

    def get_queue(self):
        with self.lock:
            return self.queue.copy()

    def pop_queue(self):
        with self.lock:
            if not self.queue:
                print("queue is empty")
            else:
                self.queue.pop(0)

    def stop(self):
        self.running = False
        self.server.close()
        self.recv_thread.join()



if __name__ == "__main__":
    server = Server()

    def start_server():
        server.run()

    server_thread = Thread(target=start_server)
    server_thread.start()

    player1 = Client()
    player2 = Client()

    time.sleep(1)
    player1.send_msg("Hello there!")
    time.sleep(2)
    player2.send_msg("Huzzah")
    time.sleep(2)
    player1.send_msg("Huh")
    time.sleep(2)
    player2.send_msg("HUZZAAAAHHHH!!!!")
    time.sleep(2)

    print(server.get_queue())