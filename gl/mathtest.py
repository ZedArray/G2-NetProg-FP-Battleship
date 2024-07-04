def delete():
    for ships in ship:
        for cell in ships[0]:
            if cell == hit:
                ships[1] -= 1
    print(ship)

def checkforsink():
    for ships in ship:
        if ships[1] == 0:
            ships[1] -= 1
            print("blud got sunk")

ship = [[[1, 2], 2], [[3, 4, 5], 3], [[5, 6, 7], 3], [[7, 8, 9, 10], 4]]

hit = 1
delete()

hit = 2
delete()

checkforsink()