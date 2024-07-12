import threading
from network.connection import Server

class GameServer:
    def __init__(self):
        self.server = Server()
        self.server_thread = threading.Thread(target=self.start_server)
        self.server_thread.start()
        self.player_list = []

    def start_server(self):
        self.server.run()

    def get_data(self):
        return self.server.get_queue()

    def pop_data(self):
        self.server.pop_queue()

    def get_clients(self):
        self.player_list = self.server.list_of_clients
        if len(self.player_list) >= 2:
            # player1 = self.player_list[0]
            # player2 = self.player_list[1]
            print(self.player_list)
            return True
        else:
            print("Not enough clients connected.")
            return False

    def broadcast_message(self, message):
        self.server.broadcast(message)

    def send_message(self, message, target_index):
        if not self.get_clients():
            return False

        if 0 <= target_index < len(self.player_list):
            self.server.send_message(message, self.player_list[target_index])
            return True
        else:
            print("Invalid target index.")
            return False


if __name__ == "__main__":
    server = GameServer()

    while True:
        user_input = input("> ")

        if user_input == "data":
            print(server.get_data())

        elif user_input == "pop":
            server.pop_data()

        elif user_input == "getClients":
            server.get_clients()

        elif user_input == "broadcast":
            message = input("message: ")
            server.broadcast_message(message)

        elif user_input == "send":
            message = input("message: ")
            client_target = int(input("select target (1 or 2): ")) - 1
            server.send_message(message, client_target)