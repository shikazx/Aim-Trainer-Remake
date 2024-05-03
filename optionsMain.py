import pygame
import sys
import button


optionTitle = pygame.image.load('images/optionstitle.png')
optionTitle = pygame.transform.scale(optionTitle, (900, 550))

backButton = button.Button('images/BACK.png', 550, 650)
backButton.resize((200, 120))

reticle1 = button.Button('images/reticle1.png', 100, 300)
reticle1.resize((300, 300))

reticle2 = button.Button('images/reticle2.png', 500, 300)
reticle2.resize((300, 300))

reticle3 = button.Button('images/reticle3.png', 900, 300)
reticle3.resize((300, 300))


def optionLoop(screen, menuBG):
    screen.fill((0, 0, 0))
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.blit(menuBG, (0, 0))
        screen.blit(optionTitle, (200, 0))

        reticle1.displayButton(screen)
        reticle2.displayButton(screen)
        reticle3.displayButton(screen)
        backButton.displayButton(screen)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # crosshair checks and scaling images to crosshair sizes
                    if reticle1.checkCollision(screen, event.pos):
                        pygame.mouse.set_cursor((10,10), pygame.transform.scale(reticle1.image, (30,30)))
                    elif reticle2.checkCollision(screen, event.pos):
                        pygame.mouse.set_cursor((10,10), pygame.transform.scale(reticle2.image, (30,30)))
                    elif reticle3.checkCollision(screen, event.pos):
                        pygame.mouse.set_cursor((10,10), pygame.transform.scale(reticle3.image, (30,30)))
                    elif backButton.checkCollision(screen, event.pos):
                        running = False



        pygame.display.flip()
        clock.tick(60)





