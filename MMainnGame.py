import pygame
from sock.client import playerClient

darkgrey = (70,70,70)
WIN = pygame.display.set_mode((1280, 720))
BG = pygame.transform.scale(pygame.image.load("gl/image2.png"), (1280, 720))
# BGBattle = pygame.transform.scale(pygame.image.load("gl/image3.png"), (1280, 720))
ship1 = pygame.image.load("gl/ship1.png")
ship2 = pygame.transform.scale(pygame.image.load("gl/ship2.png"), (1280, 720))
ship3 = pygame.transform.scale(pygame.image.load("gl/ship3.png"), (1280, 720))
BG2 = pygame.transform.scale(pygame.image.load("gl/image3.png"), (1280, 720))
HomePage = pygame.transform.scale(pygame.image.load("gl/homepage.png"), (1280, 720))
enterName = pygame.transform.scale(pygame.image.load("gl/entername.png"), (1280, 720))
winScreen = pygame.transform.scale(pygame.image.load("ui/winscreen.png"), (1280, 720))
loseScreen = pygame.transform.scale(pygame.image.load("ui/losescreen.png"), (1280, 720))


shipLocs = [0] * 64
shipLeft = [1, 2, 1]
shipWholes = []
sunkShip = 0
states = 0
hitandSunk = 0

pc = playerClient()


def main():
    rotation = True
    run = True
    switch = False
    count_ship = 0
    test = [
        [pygame.Rect(61, 142.5, 70, 62.5), 0],  # [(x axis, y axis, width, height), color]
        [pygame.Rect(136, 142.5, 70, 62.5), 0],
        [pygame.Rect(211, 142.5, 70, 62.5), 0],
        [pygame.Rect(286, 142.5, 70, 62.5), 0],
        [pygame.Rect(361, 142.5, 70, 62.5), 0],
        [pygame.Rect(436, 142.5, 70, 62.5), 0],
        [pygame.Rect(511, 142.5, 70, 62.5), 0],
        [pygame.Rect(586, 142.5, 70, 62.5), 0],

        [pygame.Rect(61, 208, 70, 62.5), 0],
        [pygame.Rect(136, 208, 70, 62.5), 0],
        [pygame.Rect(211, 208, 70, 62.5), 0],
        [pygame.Rect(286, 208, 70, 62.5), 0],
        [pygame.Rect(361, 208, 70, 62.5), 0],
        [pygame.Rect(436, 208, 70, 62.5), 0],
        [pygame.Rect(511, 208, 70, 62.5), 0],
        [pygame.Rect(586, 208, 70, 62.5), 0],

        [pygame.Rect(61, 274, 70, 62.5), 0],
        [pygame.Rect(136, 274, 70, 62.5), 0],
        [pygame.Rect(211, 274, 70, 62.5), 0],
        [pygame.Rect(286, 274, 70, 62.5), 0],
        [pygame.Rect(361, 274, 70, 62.5), 0],
        [pygame.Rect(436, 274, 70, 62.5), 0],
        [pygame.Rect(511, 274, 70, 62.5), 0],
        [pygame.Rect(586, 274, 70, 62.5), 0],

        [pygame.Rect(61, 340, 70, 62.5), 0],
        [pygame.Rect(136, 340, 70, 62.5), 0],
        [pygame.Rect(211, 340, 70, 62.5), 0],
        [pygame.Rect(286, 340, 70, 62.5), 0],
        [pygame.Rect(361, 340, 70, 62.5), 0],
        [pygame.Rect(436, 340, 70, 62.5), 0],
        [pygame.Rect(511, 340, 70, 62.5), 0],
        [pygame.Rect(586, 340, 70, 62.5), 0],
        
        [pygame.Rect(61, 406, 70, 62.5), 0],
        [pygame.Rect(136, 406, 70, 62.5), 0],
        [pygame.Rect(211, 406, 70, 62.5), 0],
        [pygame.Rect(286, 406, 70, 62.5), 0],
        [pygame.Rect(361, 406, 70, 62.5), 0],
        [pygame.Rect(436, 406, 70, 62.5), 0],
        [pygame.Rect(511, 406, 70, 62.5), 0],
        [pygame.Rect(586, 406, 70, 62.5), 0],
        
        [pygame.Rect(61, 472, 70, 62.5), 0],
        [pygame.Rect(136, 472, 70, 62.5), 0],
        [pygame.Rect(211, 472, 70, 62.5), 0],
        [pygame.Rect(286, 472, 70, 62.5), 0],
        [pygame.Rect(361, 472, 70, 62.5), 0],
        [pygame.Rect(436, 472, 70, 62.5), 0],
        [pygame.Rect(511, 472, 70, 62.5), 0],
        [pygame.Rect(586, 472, 70, 62.5), 0],
        
        [pygame.Rect(61, 538, 70, 62.5), 0],
        [pygame.Rect(136, 538, 70, 62.5), 0],
        [pygame.Rect(211, 538, 70, 62.5), 0],
        [pygame.Rect(286, 538, 70, 62.5), 0],
        [pygame.Rect(361, 538, 70, 62.5), 0],
        [pygame.Rect(436, 538, 70, 62.5), 0],
        [pygame.Rect(511, 538, 70, 62.5), 0],
        [pygame.Rect(586, 538, 70, 62.5), 0],
        
        [pygame.Rect(61, 604, 70, 62.5), 0],
        [pygame.Rect(136, 604, 70, 62.5), 0],
        [pygame.Rect(211, 604, 70, 62.5), 0],
        [pygame.Rect(286, 604, 70, 62.5), 0],
        [pygame.Rect(361, 604, 70, 62.5), 0],
        [pygame.Rect(436, 604, 70, 62.5), 0],
        [pygame.Rect(511, 604, 70, 62.5), 0],
        [pygame.Rect(586, 604, 70, 62.5), 0]
    ]

    playerGrid = [
        [pygame.Rect(31, 130, 69.5, 60), 0],
        [pygame.Rect(104, 130, 69.5, 60), 0],
        [pygame.Rect(176, 130, 69.5, 60), 0],
        [pygame.Rect(248, 130, 69.5, 60), 0],
        [pygame.Rect(320, 130, 69.5, 60), 0],
        [pygame.Rect(392, 130, 69.5, 60), 0],
        [pygame.Rect(464, 130, 69.5, 60), 0],
        [pygame.Rect(536, 130, 69.5, 60), 0],

        [pygame.Rect(31, 192, 69.5, 60), 0],
        [pygame.Rect(104, 192, 69.5, 60), 0],
        [pygame.Rect(176, 192, 69.5, 60), 0],
        [pygame.Rect(248, 192, 69.5, 60), 0],
        [pygame.Rect(320, 192, 69.5, 60), 0],
        [pygame.Rect(392, 192, 69.5, 60), 0],
        [pygame.Rect(464, 192, 69.5, 60), 0],
        [pygame.Rect(536, 192, 69.5, 60), 0],

        [pygame.Rect(31, 254, 69.5, 60), 0],
        [pygame.Rect(104, 254, 69.5, 60), 0],
        [pygame.Rect(176, 254, 69.5, 60), 0],
        [pygame.Rect(248, 254, 69.5, 60), 0],
        [pygame.Rect(320, 254, 69.5, 60), 0],
        [pygame.Rect(392, 254, 69.5, 60), 0],
        [pygame.Rect(464, 254, 69.5, 60), 0],
        [pygame.Rect(536, 254, 69.5, 60), 0],

        [pygame.Rect(31, 316, 69.5, 60), 0],
        [pygame.Rect(104, 316, 69.5, 60), 0],
        [pygame.Rect(176, 316, 69.5, 60), 0],
        [pygame.Rect(248, 316, 69.5, 60), 0],
        [pygame.Rect(320, 316, 69.5, 60), 0],
        [pygame.Rect(392, 316, 69.5, 60), 0],
        [pygame.Rect(464, 316, 69.5, 60), 0],
        [pygame.Rect(536, 316, 69.5, 60), 0],

        [pygame.Rect(31, 378, 69.5, 60), 0],
        [pygame.Rect(104, 378, 69.5, 60), 0],
        [pygame.Rect(176, 378, 69.5, 60), 0],
        [pygame.Rect(248, 378, 69.5, 60), 0],
        [pygame.Rect(320, 378, 69.5, 60), 0],
        [pygame.Rect(392, 378, 69.5, 60), 0],
        [pygame.Rect(464, 378, 69.5, 60), 0],
        [pygame.Rect(536, 378, 69.5, 60), 0],

        [pygame.Rect(31, 440, 69.5, 60), 0],
        [pygame.Rect(104, 440, 69.5, 60), 0],
        [pygame.Rect(176, 440, 69.5, 60), 0],
        [pygame.Rect(248, 440, 69.5, 60), 0],
        [pygame.Rect(320, 440, 69.5, 60), 0],
        [pygame.Rect(392, 440, 69.5, 60), 0],
        [pygame.Rect(464, 440, 69.5, 60), 0],
        [pygame.Rect(536, 440, 69.5, 60), 0],

        [pygame.Rect(31, 503, 69.5, 60), 0],
        [pygame.Rect(104, 503, 69.5, 60), 0],
        [pygame.Rect(176, 503, 69.5, 60), 0],
        [pygame.Rect(248, 503, 69.5, 60), 0],
        [pygame.Rect(320, 503, 69.5, 60), 0],
        [pygame.Rect(392, 503, 69.5, 60), 0],
        [pygame.Rect(464, 503, 69.5, 60), 0],
        [pygame.Rect(536, 503, 69.5, 60), 0],

        [pygame.Rect(31, 566, 69.5, 60), 0],
        [pygame.Rect(104, 566, 69.5, 60), 0],
        [pygame.Rect(176, 566, 69.5, 60), 0],
        [pygame.Rect(248, 566, 69.5, 60), 0],
        [pygame.Rect(320, 566, 69.5, 60), 0],
        [pygame.Rect(392, 566, 69.5, 60), 0],
        [pygame.Rect(464, 566, 69.5, 60), 0],
        [pygame.Rect(536, 566, 69.5, 60), 0],
    ]
    
    targetGrid = [
        [pygame.Rect(678, 130, 69.5, 60), 0],
        [pygame.Rect(750, 130, 69.5, 60), 0],
        [pygame.Rect(822, 130, 69.5, 60), 0],
        [pygame.Rect(894, 130, 69.5, 60), 0],
        [pygame.Rect(966, 130, 69.5, 60), 0],
        [pygame.Rect(1038, 130, 69.5, 60), 0],
        [pygame.Rect(1110, 130, 69.5, 60), 0],
        [pygame.Rect(1182, 130, 69.5, 60), 0],

        [pygame.Rect(678, 192, 69.5, 60), 0],
        [pygame.Rect(750, 192, 69.5, 60), 0],
        [pygame.Rect(822, 192, 69.5, 60), 0],
        [pygame.Rect(894, 192, 69.5, 60), 0],
        [pygame.Rect(966, 192, 69.5, 60), 0],
        [pygame.Rect(1038, 192, 69.5, 60), 0],
        [pygame.Rect(1110, 192, 69.5, 60), 0],
        [pygame.Rect(1182, 192, 69.5, 60), 0],

        [pygame.Rect(678, 254, 69.5, 60), 0],
        [pygame.Rect(750, 254, 69.5, 60), 0],
        [pygame.Rect(822, 254, 69.5, 60), 0],
        [pygame.Rect(894, 254, 69.5, 60), 0],
        [pygame.Rect(966, 254, 69.5, 60), 0],
        [pygame.Rect(1038, 254, 69.5, 60), 0],
        [pygame.Rect(1110, 254, 69.5, 60), 0],
        [pygame.Rect(1182, 254, 69.5, 60), 0],

        [pygame.Rect(678, 316, 69.5, 60), 0],
        [pygame.Rect(750, 316, 69.5, 60), 0],
        [pygame.Rect(822, 316, 69.5, 60), 0],
        [pygame.Rect(894, 316, 69.5, 60), 0],
        [pygame.Rect(966, 316, 69.5, 60), 0],
        [pygame.Rect(1038, 316, 69.5, 60), 0],
        [pygame.Rect(1110, 316, 69.5, 60), 0],
        [pygame.Rect(1182, 316, 69.5, 60), 0],

        [pygame.Rect(678, 378, 69.5, 60), 0],
        [pygame.Rect(750, 378, 69.5, 60), 0],
        [pygame.Rect(822, 378, 69.5, 60), 0],
        [pygame.Rect(894, 378, 69.5, 60), 0],
        [pygame.Rect(966, 378, 69.5, 60), 0],
        [pygame.Rect(1038, 378, 69.5, 60), 0],
        [pygame.Rect(1110, 378, 69.5, 60), 0],
        [pygame.Rect(1182, 378, 69.5, 60), 0],

        [pygame.Rect(678, 440, 69.5, 60), 0],
        [pygame.Rect(750, 440, 69.5, 60), 0],
        [pygame.Rect(822, 440, 69.5, 60), 0],
        [pygame.Rect(894, 440, 69.5, 60), 0],
        [pygame.Rect(966, 440, 69.5, 60), 0],
        [pygame.Rect(1038, 440, 69.5, 60), 0],
        [pygame.Rect(1110, 440, 69.5, 60), 0],
        [pygame.Rect(1182, 440, 69.5, 60), 0],

        [pygame.Rect(678, 503, 69.5, 60), 0],
        [pygame.Rect(750, 503, 69.5, 60), 0],
        [pygame.Rect(822, 503, 69.5, 60), 0],
        [pygame.Rect(894, 503, 69.5, 60), 0],
        [pygame.Rect(966, 503, 69.5, 60), 0],
        [pygame.Rect(1038, 503, 69.5, 60), 0],
        [pygame.Rect(1110, 503, 69.5, 60), 0],
        [pygame.Rect(1182, 503, 69.5, 60), 0],

        [pygame.Rect(678, 566, 69.5, 60), 0],
        [pygame.Rect(750, 566, 69.5, 60), 0],
        [pygame.Rect(822, 566, 69.5, 60), 0],
        [pygame.Rect(894, 566, 69.5, 60), 0],
        [pygame.Rect(966, 566, 69.5, 60), 0],
        [pygame.Rect(1038, 566, 69.5, 60), 0],
        [pygame.Rect(1110, 566, 69.5, 60), 0],
        [pygame.Rect(1182, 566, 69.5, 60), 0],
    ]

    # ship selection buttons (colors are changed for length)
    ship = [
        [pygame.Rect(700, 153, 520, 85), 2],
        [pygame.Rect(700, 248.5, 520, 85), 3],
        [pygame.Rect(700, 344, 520, 85), 3],
        [pygame.Rect(700, 443, 520, 85), 4],
        # [pygame.Rect(770.5, 575, 383, 55), 5]
    ]

    buttonBeforeMain = [
        [pygame.Rect(343, 290, 584, 84), 0], #start
        [pygame.Rect(343, 400, 584, 84), 0], #Exit
        [pygame.Rect(445, 455, 385, 97), 0], #Confirm on entername
    ]

    count=0

    testprint = ""

    confirmButton = pygame.Rect(768, 573, 385, 60)

    global states

    global hitandSunk

    turn = True

    while run:
        match states:
            case 0: # homepage layout
                for event in pygame.event.get():
                    # game quit then break the loop
                    if event.type == pygame.QUIT:
                        run = False
                        break
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            print(pygame.mouse.get_pos())

                            if buttonBeforeMain[0][0].collidepoint(pygame.mouse.get_pos()):
                                states = 2
                            if buttonBeforeMain[1][0].collidepoint(pygame.mouse.get_pos()):
                                run = False
                                break
                WIN.blit(HomePage, (0, 0))

            case 1: # enter name layout
                for event in pygame.event.get():
                    # game quit then break the loop
                    if event.type == pygame.QUIT:
                        run = False
                        break
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            print(pygame.mouse.get_pos())
                            if buttonBeforeMain[2][0].collidepoint(pygame.mouse.get_pos()):
                                states = 2
                WIN.blit(enterName, (0, 0))

            # ship placement screen
            case 2: # view ship placement
                for event in pygame.event.get():
                    # game quit then break the loop
                    if event.type == pygame.QUIT:
                        run = False
                        break
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            print(pygame.mouse.get_pos())
                            # pressing the ship selection button
                            for i in range(len(ship)):
                                if ship[i][0].collidepoint(pygame.mouse.get_pos()):
                                    if i == 0 and shipLeft[0] > 0:
                                        count = 2
                                        count_ship += 1
                                        print("selected 2x1 tiles")
                                    elif i == 1 or i == 2:
                                        if shipLeft[1] > 0:
                                            count = 3
                                            count_ship += 1
                                            print("selected 3x1 tiles")
                                    elif i == 3 and shipLeft[2] > 0:
                                        count = 4
                                        count_ship += 1
                                        print("selected 4x1 tiles")

                            # placing ships
                            for i in range(len(test)):
                                if test[i][1] == 2:
                                    if test[i][0].collidepoint(pygame.mouse.get_pos()):
                                        selectedLoc(count, i, test, rotation)
                                        count = 0

                            # confirming placements
                            if confirmButton.collidepoint(pygame.mouse.get_pos()):
                                shipChecker = 0
                                for s in shipLeft:
                                    shipChecker += s
                                if shipChecker == 0:
                                    applyPlacement(playerGrid)
                                    states = 3
                        
                        # testing cell storing
                        if pygame.mouse.get_pressed()[1]:
                            for i in range(64):
                                testprint += str(shipLocs[i]) + " "
                                if i % 8 == 7:
                                    testprint += "\n"
                            print(testprint)
                            testprint = ""
                        
                        # rotate
                        if pygame.mouse.get_pressed()[2]:
                            if rotation:
                                rotation = False
                                print("Turned to False")
                            elif not rotation:
                                rotation = True
                                print("Turned to True")

                    # function call for hovering
                    for i in range(len(test)):
                        if test[i][1] == 1: continue
                        else:
                            hoverLoc(count, i, test, rotation)

                WIN.blit(BG, (0, 0))
                #color tiles
                for cell in test:
                    if cell[1] == 0:
                        pygame.draw.rect(WIN, "dark blue", cell[0])
                    elif cell[1] == 1:
                        pygame.draw.rect(WIN, darkgrey, cell[0])
                    elif cell[1] == 2:
                        pygame.draw.rect(WIN, "grey", cell[0])

            # gameplay screen
            case 3: #view gameplay layout
                for event in pygame.event.get():
                    # game quit then break the loop
                    if event.type == pygame.QUIT:
                        run = False
                        break
                    
                    if not turn:
                        # receive the hit from here
                        # send back a signal whether hit or not
                        # do hitShip() to check 
                        # after all that, turn = True to give turn back to this player
                        targeted = -1
                        receivedData = int(pc.get_data())
                        print(receivedData)
                        targeted = receivedData[0]
                        pc.pop_data()
                        # targeted = receive target location
                        if shipLocs[targeted] == 0:
                            playerGrid[targeted][1] = 2
                            pc.send_data(70)
                            # send a signal 70 indicating no hit
                        elif shipLocs[targeted] == 1:
                            playerGrid[targeted][1] = 3
                            hitShip(targeted)
                            ifSunk = checkforsink()
                            if ifSunk:
                                pc.send_data(90)
                                # send a signal 90 indicating hit and sunk
                                pass
                            elif not ifSunk:
                                pc.send_data(80)
                                # send a signal 80 indicating hit
                                pass
                            # send back a signal for hit and if sink
                            # return hit
                        if targeted != -1:
                            turn = True

                        continue

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            print(pygame.mouse.get_pos())
                            for i in range(64):
                                if targetGrid[i][0].collidepoint(pygame.mouse.get_pos()):
                                    
                                    # ask for the status of cell i (hit or no hit)
                                    pc.send_data(str(i))
                                    pc.get_data()
                                    pc.pop_data()

                                    returnSignal = 0
                                    hitOrNo = True

                                    if returnSignal == 70:
                                        targetGrid[i][1] = 2
                                        playerGrid[i][1] = 2
                                    elif returnSignal == 80:
                                        targetGrid[i][1] = 3
                                        playerGrid[i][1] = 3
                                    elif returnSignal == 90:
                                        targetGrid[i][1] = 3
                                        playerGrid[i][1] = 3
                                        hitandSunk += 1
                                        print("sunk")
                                    
                                    if hitandSunk == 4:
                                        states = 5
                                        
                                    # if hitOrNo:
                                    #     targetGrid[i][1] = 3
                                    # if not hitOrNo:
                                    #     targetGrid[i][1] = 2

                                    if shipLocs[i] == 0:
                                        targetGrid[i][1] = 2
                                        playerGrid[i][1] = 2
                                    elif shipLocs[i] == 1:
                                        targetGrid[i][1] = 3
                                        playerGrid[i][1] = 3
                                        hitShip(i)
                                        checkforsink()

                                        # keep checking for sink
                                    
                                    # after choosing target, give turn to other player
                                    # turn = False
                        if pygame.mouse.get_pressed()[1]:
                            print(shipWholes)
                            # states = 4
                        if pygame.mouse.get_pressed()[2]:
                            # states = 5
                            print(sunkShip)

                            # print(playerGrid)
                    
                    hoverTarget(targetGrid)

                WIN.blit(BG2, (0, 0))
                for cell in playerGrid:
                    if cell[1] == 0:
                        pygame.draw.rect(WIN, "dark blue", cell[0])
                    elif cell[1] == 1:
                        pygame.draw.rect(WIN, darkgrey, cell[0])
                    elif cell[1] == 2:
                        pygame.draw.rect(WIN, "white", cell[0])
                    elif cell[1] == 3:
                        pygame.draw.rect(WIN, "red", cell[0])
                for cell in targetGrid:
                    if cell[1] == 0:
                        pygame.draw.rect(WIN, "dark blue", cell[0])
                    elif cell[1] == 1:
                        pygame.draw.rect(WIN, "grey", cell[0])
                    elif cell[1] == 2:
                        pygame.draw.rect(WIN, "white", cell[0])
                    elif cell[1] == 3:
                        pygame.draw.rect(WIN, "red", cell[0]) 

            case 4:
                # winscreen
                for event in pygame.event.get():
                    # game quit then break the loop
                    if event.type == pygame.QUIT:
                        run = False
                        break
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        run = False
                        break
                WIN.blit(winScreen, (0, 0))

            case 5:
                # losescreen
                for event in pygame.event.get():
                    # game quit then break the loop
                    if event.type == pygame.QUIT:
                        run = False
                        break
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        run = False
                        break
                WIN.blit(loseScreen, (0, 0))

        pygame.display.update()
    
    pygame.quit()

def hitShip(target):
    for s in shipWholes:
        for cell in s[0]:
            if cell == target:
                s[1] -= 1
                print("hit")

def checkforsink():
    global sunkShip
    global states
    sunkOne = 0
    for s in shipWholes:
        if s[1] == 0:
            s[1] -= 1
            print("blud got sunk")
            sunkOne = 1
            sunkShip += 1
    # if sunkShip == 4, signal the other player and go to winscreen/losescreen
    if (sunkShip == 4):
        states = 5
    if sunkOne == 1:
        return sunkOne

def hoverTarget(tGrid):
    for cell in tGrid:
        if cell[1] == 2 or cell[1] == 3:
            continue
        if cell[0].collidepoint(pygame.mouse.get_pos()):
            cell[1] = 1
        else:
            cell[1] = 0

def applyPlacement(pGrid):
    for i in range(64):
        if shipLocs[i] == 1:
            pGrid[i][1] = 1

def selectedLoc(count, i, test, rotation):
    if count == 2: #counts = tiles
        if rotation:
            if i % 8 != 7:
                test[i][1] = 1
                test[i+1][1] = 1
                shipLocs[i] = 1
                shipLocs[i+1] = 1
                shipLeft[0] -= 1
                shipWholes.append([[i, i+1], 2])
        elif not rotation:
            if i <= 55:
                test[i][1] = 1
                test[i+8][1] = 1
                shipLocs[i] = 1
                shipLocs[i+8] = 1
                shipLeft[0] -= 1
                shipWholes.append([[i, i+8], 2])


    elif count == 3:
        if rotation:
            if (i % 8) < 6:
                test[i][1] = 1
                test[i+1][1] = 1
                test[i+2][1] = 1
                shipLocs[i] = 1
                shipLocs[i+1] = 1
                shipLocs[i+2] = 1
                shipLeft[1] -= 1
                shipWholes.append([[i, i+1, i+2], 3])
        elif not rotation:
            if i <= 55:
                test[i][1] = 1
                test[i+8][1] = 1
                test[i+16][1] = 1
                shipLocs[i] = 1
                shipLocs[i+8] = 1
                shipLocs[i+16] = 1
                shipLeft[1] -= 1
                shipWholes.append([[i, i+8, i+16], 3])

    elif count == 4:
        if rotation:
            if (i % 8) < 5:
                test[i][1] = 1
                test[i+1][1] = 1
                test[i+2][1] = 1
                test[i+3][1] = 1
                shipLocs[i] = 1
                shipLocs[i+1] = 1
                shipLocs[i+2] = 1
                shipLocs[i+3] = 1
                shipLeft[2] -= 1
                shipWholes.append([[i, i+1, i+2, i+3], 4])
        
        elif not rotation:
            if i <= 39:
                test[i][1] = 1
                test[i+8][1] = 1
                test[i+16][1] = 1
                test[i+24][1] = 1
                shipLocs[i] = 1
                shipLocs[i+8] = 1
                shipLocs[i+16] = 1
                shipLocs[i+24] = 1
                shipLeft[2] -= 1
                shipWholes.append([[i, i+8, i+16, i+24], 4])


def hoverLoc(count, i, test, rotation):
    if count == 2:
        if rotation:
            if (i % 8 != 7):
                if test[i][0].collidepoint(pygame.mouse.get_pos()):
                    if test[i][1] == 1 or test[i+1][1] == 1:
                        count = 2
                    else:
                        test[i][1] = 2
                        test[i+1][1] = 2
                elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                    count = 2
                else:
                    test[i][1] = 0
            elif not test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                test[i][1] = 0

        elif not rotation:
            if (i <= 55):
                if test[i][0].collidepoint(pygame.mouse.get_pos()):
                    if test[i][1] == 1 or test[i+8][1] == 1:
                        count = 2
                    else:
                        test[i][1] = 2
                        test[i+8][1] = 2
                elif test[i-8][0].collidepoint(pygame.mouse.get_pos()):
                    count = 2
                else:
                    test[i][1] = 0
            elif not test[i-8][0].collidepoint(pygame.mouse.get_pos()):
                test[i][1] = 0

    elif count == 3:
        if rotation:
            if ((i % 8) < 6):
                if test[i][0].collidepoint(pygame.mouse.get_pos()):
                    if test[i][1] == 1 or test[i+1][1] == 1 or test[i+2][1] == 1:
                        count = 3
                    else:
                        test[i][1] = 2
                        test[i+1][1] = 2
                        test[i+2][1] = 2
                elif test[i-1][0].collidepoint(pygame.mouse.get_pos()) or test[i-2][0].collidepoint(pygame.mouse.get_pos()):
                    count = 3
                else:
                    test[i][1] = 0
            elif not test[i-1][0].collidepoint(pygame.mouse.get_pos()) and not test[i-2][0].collidepoint(pygame.mouse.get_pos()):
                test[i][1] = 0

        elif not rotation:
            if i <= 47:
                if test[i][0].collidepoint(pygame.mouse.get_pos()):
                    if test[i][1] == 1 or test[i+8][1] == 1 or test[i+16][1] == 1:
                        count = 3
                    else:
                        test[i][1] = 2
                        test[i+8][1] = 2
                        test[i+16][1] = 2
                elif test[i-8][0].collidepoint(pygame.mouse.get_pos()) or test[i-16][0].collidepoint(pygame.mouse.get_pos()):
                    count = 3
                else:
                    test[i][1] = 0
            elif not test[i-8][0].collidepoint(pygame.mouse.get_pos()) and not test[i-16][0].collidepoint(pygame.mouse.get_pos()):
                test[i][1] = 0

    elif count == 4:
        if rotation:
            if ((i % 8) < 5):
                if test[i][0].collidepoint(pygame.mouse.get_pos()):
                    if test[i][1] == 1 or test[i+1][1] == 1 or test[i+2][1] == 1 or test[i+3][1] == 1:
                        count = 4
                    else:
                        test[i][1] = 2
                        test[i+1][1] = 2
                        test[i+2][1] = 2
                        test[i+3][1] = 2
                elif test[i-1][0].collidepoint(pygame.mouse.get_pos()) or test[i-2][0].collidepoint(pygame.mouse.get_pos()) or test[i-3][0].collidepoint(pygame.mouse.get_pos()):
                    count = 4
                else:
                    test[i][1] = 0
            elif not test[i-1][0].collidepoint(pygame.mouse.get_pos()) and not test[i-2][0].collidepoint(pygame.mouse.get_pos()) and not test[i-3][0].collidepoint(pygame.mouse.get_pos()):
                test[i][1] = 0
        
        elif not rotation:
            if i <= 39:
                if test[i][0].collidepoint(pygame.mouse.get_pos()):
                    if test[i][1] == 1 or test[i+8][1] == 1 or test[i+16][1] == 1 or test[i+24][1] == 1:
                        count = 4
                    else:
                        test[i][1] = 2
                        test[i+8][1] = 2
                        test[i+16][1] = 2
                        test[i+24][1] = 2
                elif test[i-8][0].collidepoint(pygame.mouse.get_pos()) or test[i-16][0].collidepoint(pygame.mouse.get_pos()) or test[i-24][0].collidepoint(pygame.mouse.get_pos()):
                    count = 4
                else:
                    test[i][1] = 0
            elif not test[i-8][0].collidepoint(pygame.mouse.get_pos()) and not test[i-16][0].collidepoint(pygame.mouse.get_pos()) and not test[i-24][0].collidepoint(pygame.mouse.get_pos()):
                test[i][1] = 0


if __name__ == "__main__":
    main()