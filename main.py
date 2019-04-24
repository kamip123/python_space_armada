from galaxyMap import *

def start_game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    galaxyMapTravel()
                    pass

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        gameDisplay.blit(backgroundStartingScreen, (0, 0))
        message_to_screen("Welcome to",
                          red,
                          -180,
                          "large")
        message_to_screen("Space Fleet Commander",
                          red,
                          -100,
                          "large")
        message_to_screen("The objective of the game is to destroy enemy fleet",
                          green,
                          -30)

        message_to_screen("You can give comands using keyboard, voice or gestures",
                          green,
                          10)

        message_to_screen("If you run into enemy ship you can die.",
                          green,
                          50)
        message_to_screen("If you run into edge of the map you die.",
                          green,
                          90)
        message_to_screen("Press Space to play or Q to quit.",
                          green,
                          180)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    start_game_intro()
