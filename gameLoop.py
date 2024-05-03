import sys
import pygame
import button
import optionsMain
import inGameMain

# setup
widthRes = 1280
heightRes = 800
pygame.init()
screen = pygame.display.set_mode((widthRes, heightRes))

# images for menu
menuBG = pygame.image.load('images/mainmenubg.jpg')
menuBG = pygame.transform.scale(menuBG, (widthRes, heightRes))
title = pygame.image.load('images/title.png')

# create buttons for menu page
startButton = button.Button('images/START.png', 100, 450)
optionsButton = button.Button('images/optionsbutton.png', 500, 450)
exitButton = button.Button('images/EXIT.png', 900, 450)

# music
pygame.mixer.music.load('music/menumusic.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1, 0.0)

# running loop
clock = pygame.time.Clock()
running = True


while running:

    # menu background and title
    screen.blit(menuBG, (0, 0))
    screen.blit(title, (25, 15))

    startButton.displayButton(screen)
    optionsButton.displayButton(screen)
    exitButton.displayButton(screen)

    # polling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if startButton.checkCollision(screen, event.pos):
                    inGameMain.ingameLoop(screen)
                elif optionsButton.checkCollision(screen, event.pos):
                    optionsMain.optionLoop(screen, menuBG)
                elif exitButton.checkCollision(screen, event.pos):
                    sys.exit()


    # update
    pygame.display.flip()
    clock.tick(60)















