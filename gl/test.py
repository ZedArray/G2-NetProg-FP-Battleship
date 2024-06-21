import pygame

WIN = pygame.display.set_mode((1280, 720))
BG = pygame.transform.scale(pygame.image.load("gl/image.png"), (1280, 720))


def main():
    run = True
    rotation = True

    # test = [[
    #         pygame.draw.rect(WIN, "red", pygame.Rect(60, 130, 130, 110)),
    #         pygame.draw.rect(WIN, "red", pygame.Rect(195, 130, 130, 110)),
    #         pygame.draw.rect(WIN, "red", pygame.Rect(330, 130, 130, 110)),
    #         pygame.draw.rect(WIN, "red", pygame.Rect(465, 130, 130, 110))],

    #             [
    #         pygame.draw.rect(WIN, "red", pygame.Rect(60, 245, 130, 110)),
    #         pygame.draw.rect(WIN, "red", pygame.Rect(195, 245, 130, 110)),
    #         pygame.draw.rect(WIN, "red", pygame.Rect(330, 245, 130, 110)),
    #         pygame.draw.rect(WIN, "red", pygame.Rect(465, 245, 130, 110))],

    #             [
    #         pygame.draw.rect(WIN, "red", pygame.Rect(60, 360, 130, 110)),
    #         pygame.draw.rect(WIN, "red", pygame.Rect(195, 360, 130, 110)),
    #         pygame.draw.rect(WIN, "red", pygame.Rect(330, 360, 130, 110)),
    #         pygame.draw.rect(WIN, "red", pygame.Rect(465, 360, 130, 110))]
    # ]

    test = [
            [pygame.Rect(60, 130, 130, 110), 0],
            [pygame.Rect(195, 130, 130, 110), 0],
            [pygame.Rect(330, 130, 130, 110), 0],
            [pygame.Rect(465, 130, 130, 110), 0],

                
            [pygame.Rect(60, 245, 130, 110), 0],
            [pygame.Rect(195, 245, 130, 110), 0],
            [pygame.Rect(330, 245, 130, 110), 0],
            [pygame.Rect(465, 245, 130, 110), 0],

                
            [pygame.Rect(60, 360, 130, 110), 0],
            [pygame.Rect(195, 360, 130, 110), 0],
            [pygame.Rect(330, 360, 130, 110), 0],
            [pygame.Rect(465, 360, 130, 110), 0],

            [pygame.Rect(60, 475, 130, 110), 0],
            [pygame.Rect(195, 475, 130, 110), 0],
            [pygame.Rect(330, 475, 130, 110), 0],
            [pygame.Rect(465, 475, 130, 110), 0]
    ]

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for cell in test:
                        if cell[0].collidepoint(pygame.mouse.get_pos()):
                            cell[1] = 1
                if pygame.mouse.get_pressed()[2]:
                    if rotation:
                        rotation = False
                        print("Turned to False")
                    elif not rotation:
                        rotation = True
                        print("Turned to True")
                    
            for i in range(len(test)):
                if rotation:
                    if test[i][1] == 0 or test[i][1] == 2:
                        if i % 4 != 3:
                            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                                test[i][1] = 2
                                test[i+1][1] = 2
                                # if i % 4 != 3:
                                #     print("--------------")
                                #     print("b1" + str(test[i]))
                                #     print("b2" + str(test[i+1]))
                                #     test[i][1] = 2
                                #     # test[i+1][1] = 2
                                #     print("b1" + str(test[i]))
                                #     print("b2" + str(test[i+1]))
                                #     print("--------------")
                                # test[i][1] = 2
                                # test[i+1][1] = 2
                            elif test[i-1][0].collidepoint(pygame.mouse.get_pos()):
                                continue
                            else:
                                test[i][1] = 0
                        elif i % 4 == 3:
                            if test[i][0].collidepoint(pygame.mouse.get_pos()):
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
                            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                                test[i][1] = 2
                                test[i+4][1] = 2
                            elif test[i-4][0].collidepoint(pygame.mouse.get_pos()):
                                continue
                            else:
                                test[i][1] = 0
                        elif i >= 12:
                            if test[i][0].collidepoint(pygame.mouse.get_pos()):
                                test[i][1] = 2
                                test[i-4][1] = 2
                            elif test[i-4][0].collidepoint(pygame.mouse.get_pos()):
                                continue
                            else:
                                test[i][1] = 0
                        elif not test[i-4][0].collidepoint(pygame.mouse.get_pos()):
                            test[i][1] = 0
            # for cell in test:
            #     if cell[1] == 0 or cell[1] == 2:
            #         if cell[0].collidepoint(pygame.mouse.get_pos()):
            #             cell[1] = 2
            #         else:
            #             cell[1] = 0
        
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