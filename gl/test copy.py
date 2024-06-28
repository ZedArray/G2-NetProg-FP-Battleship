import pygame

WIN = pygame.display.set_mode((1280, 720))
BG = pygame.transform.scale(pygame.image.load("gl/image2.png"), (1280, 720))


def main():
    run = True
    rotation = True
    test = [
            [pygame.Rect(60, 142.5, 70, 62.5), 0],
            [pygame.Rect(135, 142.5, 70, 62.5), 0],
            [pygame.Rect(210, 142.5, 70, 62.5), 0],
            [pygame.Rect(285, 142.5, 70, 62.5), 0],
            [pygame.Rect(360, 142.5, 70, 62.5), 0],
            [pygame.Rect(435, 142.5, 70, 62.5), 0],
            [pygame.Rect(510, 142.5, 70, 62.5), 0],
            [pygame.Rect(585, 142.5, 70, 62.5), 0],

            [pygame.Rect(60, 210, 70, 62.5), 0],
            [pygame.Rect(135, 210, 70, 62.5), 0],
            [pygame.Rect(210, 210, 70, 62.5), 0],
            [pygame.Rect(285, 210, 70, 62.5), 0],
            [pygame.Rect(360, 210, 70, 62.5), 0],
            [pygame.Rect(435, 210, 70, 62.5), 0],
            [pygame.Rect(510, 210, 70, 62.5), 0],
            [pygame.Rect(585, 210, 70, 62.5), 0],

            [pygame.Rect(60, 277.5, 70, 62.5), 0],
            [pygame.Rect(135, 277.5, 70, 62.5), 0],
            [pygame.Rect(210, 277.5, 70, 62.5), 0],
            [pygame.Rect(285, 277.5, 70, 62.5), 0],
            [pygame.Rect(360, 277.5, 70, 62.5), 0],
            [pygame.Rect(435, 277.5, 70, 62.5), 0],
            [pygame.Rect(510, 277.5, 70, 62.5), 0],
            [pygame.Rect(585, 277.5, 70, 62.5), 0],

            [pygame.Rect(60, 345, 70, 62.5), 0],
            [pygame.Rect(135, 345, 70, 62.5), 0],
            [pygame.Rect(210, 345, 70, 62.5), 0],
            [pygame.Rect(285, 345, 70, 62.5), 0],
            [pygame.Rect(360, 345, 70, 62.5), 0],
            [pygame.Rect(435, 345, 70, 62.5), 0],
            [pygame.Rect(510, 345, 70, 62.5), 0],
            [pygame.Rect(585, 345, 70, 62.5), 0],
            
            [pygame.Rect(60, 412.5, 70, 62.5), 0],
            [pygame.Rect(135, 412.5, 70, 62.5), 0],
            [pygame.Rect(210, 412.5, 70, 62.5), 0],
            [pygame.Rect(285, 412.5, 70, 62.5), 0],
            [pygame.Rect(360, 412.5, 70, 62.5), 0],
            [pygame.Rect(435, 412.5, 70, 62.5), 0],
            [pygame.Rect(510, 412.5, 70, 62.5), 0],
            [pygame.Rect(585, 412.5, 70, 62.5), 0],
            
            [pygame.Rect(60, 480, 70, 62.5), 0],
            [pygame.Rect(135, 480, 70, 62.5), 0],
            [pygame.Rect(210, 480, 70, 62.5), 0],
            [pygame.Rect(285, 480, 70, 62.5), 0],
            [pygame.Rect(360, 480, 70, 62.5), 0],
            [pygame.Rect(435, 480, 70, 62.5), 0],
            [pygame.Rect(510, 480, 70, 62.5), 0],
            [pygame.Rect(585, 480, 70, 62.5), 0],
            
            [pygame.Rect(60, 547.5, 70, 62.5), 0],
            [pygame.Rect(135, 547.5, 70, 62.5), 0],
            [pygame.Rect(210, 547.5, 70, 62.5), 0],
            [pygame.Rect(285, 547.5, 70, 62.5), 0],
            [pygame.Rect(360, 547.5, 70, 62.5), 0],
            [pygame.Rect(435, 547.5, 70, 62.5), 0],
            [pygame.Rect(510, 547.5, 70, 62.5), 0],
            [pygame.Rect(585, 547.5, 70, 62.5), 0],
            
            [pygame.Rect(60, 615, 70, 62.5), 0],
            [pygame.Rect(135, 615, 70, 62.5), 0],
            [pygame.Rect(210, 615, 70, 62.5), 0],
            [pygame.Rect(285, 615, 70, 62.5), 0],
            [pygame.Rect(360, 615, 70, 62.5), 0],
            [pygame.Rect(435, 615, 70, 62.5), 0],
            [pygame.Rect(510, 615, 70, 62.5), 0],
            [pygame.Rect(585, 615, 70, 62.5), 0]
    ]

    while run:
        for event in pygame.event.get():
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
                                    if i % 4 != 3:
                                        test[i][1] = 1
                                        test[i+1][1] = 1
                                    elif i % 4 == 3:
                                        test[i][1] = 1
                                        test[i-1][1] = 1
                                elif not rotation:
                                    if i < 12:
                                        test[i][1] = 1
                                        test[i+4][1] = 1
                                    elif i >= 12:
                                        test[i][1] = 1
                                        test[i-4][1] = 1
                if pygame.mouse.get_pressed()[2]:
                    if rotation:
                        rotation = False
                        print("Turned to False")
                    elif not rotation:
                        rotation = True
                        print("Turned to True")
                    
            for i in range(len(test)):
                if test[i][1] == 1: continue
                if rotation:
                    if test[i][1] == 1: continue
                    if test[i][1] == 0 or test[i][1] == 2:
                        if i % 4 != 3:
                            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                                if test[i][1] == 1 or test[i+1][1] == 1:
                                    continue
                                test[i][1] = 2
                                test[i+1][1] = 2
                            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                                continue
                            else:
                                test[i][1] = 0
                        elif i % 4 == 3:
                            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                                if test[i][1] == 1 or test[i-1][1] == 1:
                                    continue
                                test[i][1] = 2
                                test[i-1][1] = 2
                            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                                continue
                            else:
                                test[i][1] = 0
                        elif not test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                            test[i][1] = 0

                elif not rotation:
                    if test[i][1] == 0 or test[i][1] == 2:
                        if i < 12:
                            if test[i][1] == 1 or test[i+4][1] == 1: continue
                            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                                test[i][1] = 2
                                test[i+4][1] = 2
                            elif test[i-4][0].collidepoint(pygame.mouse.get_pos()):
                                continue
                            else:
                                test[i][1] = 0
                        elif i >= 12:
                            if test[i][1] == 1 or test[i-4][1] == 1: continue
                            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                                test[i][1] = 2
                                test[i-4][1] = 2
                            elif test[i-4][0].collidepoint(pygame.mouse.get_pos()):
                                continue
                            else:
                                test[i][1] = 0
                        elif not test[i-4][0].collidepoint(pygame.mouse.get_pos()):
                            test[i][1] = 0
        
        WIN.blit(BG, (0, 0))
        for cell in test:
            if cell[1] == 0:
                pygame.draw.rect(WIN, "red", cell[0])
            elif cell[1] == 1:
                pygame.draw.rect(WIN, "blue", cell[0])
            elif cell[1] == 2:
                pygame.draw.rect(WIN, "green", cell[0])

        pygame.display.update()
    
    

    pygame.quit()

if __name__ == "__main__":
    main()