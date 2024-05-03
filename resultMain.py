import pygame
import sys
import button

# displaying stats
pygame.font.init()
font = pygame.font.SysFont('Comic Sans', 60)

resultBG = pygame.image.load('images/resultsbg.png')
resultBG = pygame.transform.scale(resultBG, (1280, 800))

resultTitle = pygame.image.load('images/resulttitle.png')
resultTitle = pygame.transform.scale(resultTitle, (950, 600))

restartButton = button.Button("images/RESTART.png", 100, 570)
restartButton.resize((275, 200))

menuButton = button.Button("images/MENU.png", 500, 570)
menuButton.resize((275, 200))

quitButton = button.Button("images/EXIT.png", 900, 570)
quitButton.resize((275, 200))

def resultLoop(screen, targetsHit, clickAmount):
    screen.fill((0, 0, 0))

    # play same as menu music
    pygame.mixer.music.stop()
    pygame.mixer.music.load('music/menumusic.mp3')
    pygame.mixer.music.play(-1, 0.0)

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(resultBG, (0, 0))
        screen.blit(resultTitle, (215, 0))

        # string format for stats
        screen.blit(font.render("Targets Hit: {x}".format(x=targetsHit), True, (255, 255, 255)), (300, 250))
        screen.blit(font.render("Number of Shots: {x}".format(x=clickAmount), True, (255, 255, 255)), (300, 350))
        screen.blit(font.render("Accuracy: {x:.2f}%".format(x=targetsHit/clickAmount * 100), True, (255, 255, 255)), (300, 450))

        restartButton.displayButton(screen)
        menuButton.displayButton(screen)
        quitButton.displayButton(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # return true to restart the in game loop
                    if restartButton.checkCollision(screen, event.pos):
                        return True
                    # go back to main menu
                    elif menuButton.checkCollision(screen, event.pos):
                        return False
                    elif quitButton.checkCollision(screen, event.pos):
                        sys.exit()


        pygame.display.flip()
        clock.tick(60)