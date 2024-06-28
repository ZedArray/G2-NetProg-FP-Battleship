import pygame

WIN = pygame.display.set_mode((1280, 720))
BG1 = pygame.transform.scale(pygame.image.load("gl/image2.png"), (1280, 720))
BG2 = pygame.transform.scale(pygame.image.load("gl/image3.png"), (1280, 720))

def main():
    run = True
    switch = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    switch = True
        
        if not switch:
            WIN.blit(BG1, (0, 0))
        elif  switch:
            WIN.blit(BG2, (0, 0))
        pygame.display.update()

if __name__ == "__main__":
    main()