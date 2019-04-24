from battleOfAstarte import *
# from spacePortBase import *
from initGame import *
# from battleOfSirius import *
import _thread

def galaxyMapTravel():
    galaxy = True
    start_time = time.time()
    _thread.start_new_thread(say, ("Galaxy map loaded. Please choose the destination.",))
    while galaxy:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    galaxy = False
                    print("powinno wyjsc")

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                rectAroundImage = galaxyIconTwo.get_rect(topleft=(80, 340))
                rectAroundImage1 = galaxyIconTwo.get_rect(topleft=(260, 600))
                rectAroundImage2 = galaxyIconTwo.get_rect(topleft=(500, 630))

                if rectAroundImage.collidepoint(pos):
                    print("Astarte")
                    battleOfAstarte()

                if rectAroundImage1.collidepoint(pos):
                    print("Sirius")
                    # battleOfSirius()

                if rectAroundImage2.collidepoint(pos):
                    print("Home Planet")
                    # spacePortBase()

        gameDisplay.fill(white)
        gameDisplay.blit(galaxyMap, (0, 0))

        end_time = time.time()
        if end_time - start_time > 1.0 or end_time - start_time < 0.5:
            gameDisplay.blit(galaxyIconTwo, (75, 335))
            gameDisplay.blit(galaxyIconTwo, (255, 595))
            gameDisplay.blit(galaxyIconTwo, (495, 625))

        if end_time - start_time > 1.0:
            start_time = time.time()

        gameDisplay.blit(galaxyIconOne, (80, 340))
        gameDisplay.blit(galaxyIconOne, (260, 600))
        gameDisplay.blit(galaxyIconOne, (500, 630))
        pygame.display.update()
        clock.tick(FPS)

