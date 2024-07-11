from network.connection import Client

player = Client()

while True:
    message = input()
    if message == "DATA":
        print(player.get_queue)
    elif message == "POP":
        player.pop_queue()
    elif message == "EXIT":
        break
    else:
        player.send_msg(message)


