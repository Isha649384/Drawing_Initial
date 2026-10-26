import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("!Draw Initial with Rectangles!")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    pen = pygame.draw.rect(screen,"purple",(100,10,400,90))
    pen = pygame.draw.rect(screen,"pink",(250,100,100,400))
    pen = pygame.draw.rect(screen,"white",(100,500,400,90))
    pygame.display.flip()
pygame.quit()