import pygame
from collections import deque

WIN = pygame.display.set_mode((1280, 720))

BG = pygame.transform.scale(pygame.image.load("image.png"), (1280, 720))

def draw(b, c):
    WIN.blit(BG, (0, 0))
    cell11 = pygame.draw.rect(WIN, "red", pygame.Rect(60, 130, 130, 110))
    cell12 = pygame.draw.rect(WIN, "red", pygame.Rect(195, 130, 130, 110))
    cell13 = pygame.draw.rect(WIN, "red", pygame.Rect(330, 130, 130, 110))
    cell14 = pygame.draw.rect(WIN, "red", pygame.Rect(465, 130, 130, 110))

    cell21 = pygame.draw.rect(WIN, "red", pygame.Rect(60, 245, 130, 110))
    cell22 = pygame.draw.rect(WIN, "red", pygame.Rect(195, 245, 130, 110))
    cell23 = pygame.draw.rect(WIN, "red", pygame.Rect(330, 245, 130, 110))
    cell24 = pygame.draw.rect(WIN, "red", pygame.Rect(465, 245, 130, 110))
    
    cell31 = pygame.draw.rect(WIN, "red", pygame.Rect(60, 360, 130, 110))
    cell32 = pygame.draw.rect(WIN, "red", pygame.Rect(195, 360, 130, 110))
    cell33 = pygame.draw.rect(WIN, "red", pygame.Rect(330, 360, 130, 110))
    cell34 = pygame.draw.rect(WIN, "red", pygame.Rect(465, 360, 130, 110))

    pygame.draw.rect(WIN, "red", pygame.Rect(60, 475, 130, 110))
    pygame.draw.rect(WIN, "red", pygame.Rect(195, 475, 130, 110))
    pygame.draw.rect(WIN, "red", pygame.Rect(330, 475, 130, 110))
    pygame.draw.rect(WIN, "red", pygame.Rect(465, 475, 130, 110))
    # pygame.draw.rect(WIN, "red", pygame.Rect(580, 130, 130, 110))
    # WIN.blit(b, (200, 200))
    mouseX, mouseY = pygame.mouse.get_pos()
    # pygame.draw.rect(WIN, "red", pygame.Rect(mouseX - 50, mouseY - 50, 100, 100))
    # for buttons in b:
    #     b1, b2, b3, b4 = buttons
    #     pygame.draw.rect(WIN, c, pygame.Rect(buttons))
    # pygame.draw.rect(WIN, c, b)
    pygame.display.update()

def drawButton(button):
    WIN.blit(button, (0,0))
    pygame.display.update()

def main():
    run = True
    buttons = [(0, 0, 100, 100), (100, 100, 100, 100)]
    button = pygame.Rect(200, 100, 100, 100)
    color = "red"
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    print(pygame.mouse.get_pos())
                    if button.collidepoint(pygame.mouse.get_pos()):
                        color = "blue"
                        print("balls")
        draw(buttons, color)
    pygame.quit()

if __name__ == '__main__':
    main()