import pygame

pygame.init()
screen = pygame.display.set_mode((640, 455))
pygame.display.set_caption("CenTown")
run = True
while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

pygame.quit()
quit()