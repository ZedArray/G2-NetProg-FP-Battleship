import pygame

WIN = pygame.display.set_mode((1280, 720))
BG = pygame.transform.scale(pygame.image.load("gl/image2.png"), (1280, 720))
ship1 = pygame.image.load("gl/ship1.png")
ship2 = pygame.transform.scale(pygame.image.load("gl/ship2.png"), (1280, 720))
ship3 = pygame.transform.scale(pygame.image.load("gl/ship3.png"), (1280, 720))


def main():
    run = True
    rotation = True
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
            [pygame.Rect(586, 604, 70, 62.5), 0],

            
    ]

    ship = [
        [pygame.Rect(700, 153, 520, 85), 2],
        [pygame.Rect(700, 248.5, 520, 85), 3],
        [pygame.Rect(700, 344, 520, 85), 3],
        [pygame.Rect(700, 443, 520, 85), 4]
    ]
    count=0
    while run:
        for event in pygame.event.get():
            # game quit then break the loop
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    print(pygame.mouse.get_pos())
                    for i in range(len(test)):
                        if test[i][1] == 2:
                            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                                if rotation:
                                    selectedLoc(count,i,test)
                # if pygame.mouse.get_pressed()[2]:
                #     if rotation:
                #         rotation = False
                #         print("Turned to False")
                #     elif not rotation:
                #         rotation = True
                #         print("Turned to True")

            
            for i in range(len(test)):
                if test[i][1] == 1: continue
                if rotation:
                    if test[i][1] == 1: continue
                    if test[i][1] == 0 or test[i][1] == 2:
                        hoverLoc(count,i,test)
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        # print(pygame.mouse.get_pos())
                        for i in range(len(ship)):
                            if ship[i][0].collidepoint(pygame.mouse.get_pos()):
                                if rotation:
                                    if i == 0:
                                        count = 2
                                        print("selected 2x1 tiles")
                                    elif i == 1 or i == 2:
                                        count =3
                                        print("selected 3x1 tiles")
                                    elif i == 3:
                                        count = 4
                                        print("selected 4x1 tiles")

            # for j in range(len(ship)):
            #     if rotation:
            #         if ship[j][0].collidepoint(pygame.mouse.get_pos()):
            #             ship[j][1] = 2
            #         else:
            #             ship[j][1] = 0

        WIN.blit(BG, (0, 0))
        #color tiles
        for cell in test:
            if cell[1] == 0:
                pygame.draw.rect(WIN, "red", cell[0])
            elif cell[1] == 1:
                pygame.draw.rect(WIN, "blue", cell[0])
            elif cell[1] == 2:
                pygame.draw.rect(WIN, "green", cell[0])

        #color ships
        # screen = pygame.display.set_mode((1280, 720))
        for cell in ship:
            if cell[1] == 2:
                # screen.fill("yellow")
                # screen.blit(ship1, ship1.get_rect())
                # pygame.draw.rect(screen, "red",  cell[0])
                # pygame.draw.rect(WIN, "red", cell[0])
                # pygame.draw.rect(WIN, "red", cell[0])
                pygame.draw.rect(ship1, (255,255,255,128), cell[0])
            elif cell[1] == 3:
                pygame.draw.rect(ship2, (255,255,255,128), cell[0])
            elif cell[1] ==4:
                pygame.draw.rect(ship3, (255,255,255,128), cell[0])
                

        pygame.display.update()
    
    

    pygame.quit()

def selectedLoc(count, i, test):
    if count == 2: #counts = tiles
        if i % 4 != 3:
            test[i][1] = 1
            test[i+1][1] = 1
        elif i % 4 == 3:
            test[i][1] = 1
            test[i-1][1] = 1
    elif count == 3:
        if i % 4 == 0 or i % 4 == 1:
            test[i][1] = 1
            test[i+1][1] = 1
            test[i+2][1] = 1
        elif i % 4 == 2:
            test[i][1] = 1
            test[i+1][1] = 1
            test[i-1][1] = 1
        elif i % 4 == 3:
            test[i][1] = 1
            test[i-1][1] = 1
            test[i-2][1] = 1
    elif count == 4:
        if i % 4 == 0:
            test[i][1] = 1
            test[i+1][1] = 1
            test[i+2][1] = 1
            test[i+3][1] = 1
        elif i % 4 == 1:
            test[i][1] = 1
            test[i+1][1] = 1
            test[i+2][1] = 1
            test[i-1][1] = 1
        elif i % 4 == 2:
            test[i][1] = 1
            test[i+1][1] = 1
            test[i-2][1] = 1
            test[i-1][1] = 1
        elif i % 4 == 3:
            test[i][1] = 1
            test[i-1][1] = 1
            test[i-2][1] = 1
            test[i-3][1] = 1


def hoverLoc(count, i, test):
    if count == 2:
        if i % 4 != 3:
            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                if test[i][1] == 1 or test[i+1][1] == 1:
                    count=2
                else:
                    test[i][1] = 2
                    test[i+1][1] = 2
            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                count=2
            else:
                test[i][1] = 0
        elif i % 4 == 3:
            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                if test[i][1] == 1 or test[i-1][1] == 1:
                    count=2
                else:
                    test[i][1] = 2
                    test[i-1][1] = 2
            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                count=2
            else:
                test[i][1] = 0
        elif not test[i-1][0].collidepoint(pygame.mouse.get_pos()):
            test[i][1] = 0
    elif count == 3:
        if i % 4 == 0 or i % 4 == 1:
            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                if test[i][1] == 1 or test[i+1][1] == 1 or test[i+2][1] == 1:
                    count=3
                else:
                    test[i][1] = 2
                    test[i+1][1] = 2
                    test[i+2][1] = 2
            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                count=3
            else:
                test[i][1] = 0
        elif i % 4 == 2:
            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                if test[i][1] == 1 or test[i-1][1] == 1 or test[i+1][1] == 1:
                    count=3
                else:
                    test[i][1] = 2
                    test[i+1][1] = 2
                    test[i-1][1] = 2
            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                count=3
            else:
                test[i][1] = 0
        elif i % 4 == 3:
            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                if test[i][1] == 1 or test[i-1][1] == 1 or test[i-2][1] == 1:
                    count=3
                else:
                    test[i][1] = 2
                    test[i-1][1] = 2
                    test[i-2][1] = 2
            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                count=3
            else:
                test[i][1] = 0
        elif not test[i-1][0].collidepoint(pygame.mouse.get_pos()):
            test[i][1] = 0
    elif count == 4:
        if i % 4 == 0:
            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                if test[i][1] == 1 or test[i+1][1] == 1 or test[i+2][1] == 1 or test[i+3][1] == 1:
                    count=4
                else:
                    test[i][1] = 2
                    test[i+1][1] = 2
                    test[i+2][1] = 2
                    test[i+3][1] = 2
            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                count=3
            else:
                test[i][1] = 0
        elif i % 4 == 1:
            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                if test[i][1] == 1 or test[i+1][1] == 1 or test[i+2][1] == 1 or test[i-1][1] == 1:
                    count=3
                else:
                    test[i][1] = 2
                    test[i+1][1] = 2
                    test[i+2][1] = 2
                    test[i-1][1] = 2
            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                count=3
            else:
                test[i][1] = 0
        elif i % 4 == 2:
            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                if test[i][1] == 1 or test[i-1][1] == 1 or test[i+1][1] == 1 or test[i-2][1] == 1:
                    count=3
                else:
                    test[i][1] = 2
                    test[i+1][1] = 2
                    test[i-1][1] = 2
                    test[i-2][1] = 2
            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                count=3
            else:
                test[i][1] = 0
        elif i % 4 == 3:
            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                if test[i][1] == 1 or test[i-1][1] == 1 or test[i-2][1] == 1  or test[i-3][1] == 1:
                    count=3
                else:
                    test[i][1] = 2
                    test[i-1][1] = 2
                    test[i-2][1] = 2
            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                count=3
            else:
                test[i][1] = 0
        elif not test[i-1][0].collidepoint(pygame.mouse.get_pos()):
            test[i][1] = 0


if __name__ == "__main__":
    main()