from network.connection import Server
import threading

def start_server():
    server.run()

server = Server()
server_thread = threading.Thread(target=start_server)
server_thread.start()

player_list = []

while True:
    user_input = input("> ")


    if user_input == "data":
        print(server.get_queue())

    elif user_input == "pop":
        server.pop_queue()

    elif user_input == "getClients":
        player_list = server.list_of_clients
        player1 = player_list[0]
        player2 = player_list[1]
        print(player_list)

    elif user_input == "broadcast":
        message = input("message: ")
        server.broadcast(message)

    elif user_input == "send":
        message = input("message: ")
        client_target = input("select target (1 or 2): ")
        server.send_message(message, player_list[int(client_target)-1])

    elif user_input == "stop":
        server_thread.join()
        break