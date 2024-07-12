from network.connection import Client

class playerClient:
    def __init__ (self):
        self.client = Client()

    def send_data(self, message):
        self.client.send_msg(message)

    def get_data(self):
        return self.client.get_queue()

    def pop_data(self):
        return self.client.pop_queue()

if __name__ == "__main__":
    player = playerClient()

    while True:
        user_input = input("> ")

        if user_input == "send":
            message = input("message: ")
            player.send_data(message)

        elif user_input == "data":
            print(player.get_data())

        elif user_input == "pop":
            player.pop_data()

