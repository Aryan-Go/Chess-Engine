import pygame
pygame.init()

backGround = pygame.image.load("images/chessboard.bmp")
bg_rect = backGround.get_rect()
width = bg_rect.width/1.5
height = bg_rect.height/1.5
backGround = pygame.transform.scale(backGround,(width,height))
gameDisplay = pygame.display.set_mode((width,height))

gameDisplay.blit(backGround,(0,0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()