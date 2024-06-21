import pygame

WIN = pygame.display.set_mode((1280, 720))

test = [[pygame.draw.rect(WIN, "red", pygame.Rect(60, 130, 130, 110))]]
print(test[0])