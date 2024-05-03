import random
import pygame
import sys
import resultMain
import button

# timer font
pygame.font.init()
font = pygame.font.SysFont('Arial', 48)
font.set_bold(True)

# op sound for click
pygame.mixer.init()
gunSound = pygame.mixer.Sound('music/click.mp3')
gunSound.set_volume(0.01)

# in game background
ingameBG = pygame.image.load("images/ingamebg.jpg")
ingameBG = pygame.transform.scale(ingameBG, (1280, 800))

# creating targets
target = button.Button('images/reticle3.png', 900, 200)
target.resize((40, 40))


def ingameLoop(screen):
    # clear screen
    screen.fill((0, 0, 0))

    # megalovania LMAO
    pygame.mixer.music.stop()
    pygame.mixer.music.load('music/ingamemusic.mp3')
    pygame.mixer.music.play(-1, 0.0)

    clock = pygame.time.Clock()
    running = True

    # for keeping track of stats and timer
    startTime = pygame.time.get_ticks()
    targetsHit = 0
    clickAmount = 0

    while running:
        currentTime = pygame.time.get_ticks()
        # give 60 seconds for game
        timer = round((abs(currentTime - startTime - 5000) / 1000), 2)

        # display background and timer
        screen.blit(ingameBG, (0, 0))
        screen.blit(font.render(str(timer), True, (0,0,0)), (600, 0))

        # display target
        target.displayButton(screen)

        # event polling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # if they clicked
                    clickAmount += 1
                    gunSound.play()
                    if target.checkCollision(screen, event.pos):
                        targetsHit += 1
                        # change the position of the target button using random numbers
                        target.change_pos((random.randint(100, 1100)), random.randint(100, 700))


        # if the timer is finished
        if currentTime - startTime > 5000:
            # call the results screen loop, if this returns true we restart the game
            if resultMain.resultLoop(screen, targetsHit, clickAmount):
                pygame.mixer.music.load('music/ingamemusic.mp3')
                pygame.mixer.music.play(-1, 0.0)
                startTime = pygame.time.get_ticks()
                targetsHit = 0
                clickAmount = 0
            # stop the loop
            else:
                running = False


        pygame.display.flip()
        clock.tick(60)