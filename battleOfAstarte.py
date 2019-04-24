from ShipsThings import *
from speechThings import *
from galaxyMap import *
import copy
import _thread
import threading


def battleOfAstarte():
    global stop_listening
    global r
    global m
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height - 50

    lead_x_enemy = display_width / 2
    lead_y_enemy = 50

    position = [lead_x, lead_y]
    positionEnemy = [lead_x_enemy, lead_y_enemy]
    global mainShip
    global scanYesOrNo
    mainShip = McShip()
    mainEnemyShip = EnemyShip()

    mainShip.position[0] = lead_x
    mainShip.position[1] = lead_y

    mainEnemyShip.position[0] = lead_x_enemy
    mainEnemyShip.position[1] = lead_y_enemy

    stop_listening = r.listen_in_background(m, callback)
    startTime = time.time()
    startTimeLaserMc = time.time()
    whatShipControll = 0
    make_new_temp = True
    template = cv.imread('assets/enemyShip_scan.png', 0)
    _thread.start_new_thread(say, ('Roger. Ship is undocking. Engines set to level 2',))
    global alliedShipList


    #### allied ships

    for i in range(10):
        positionTemp=[100+i*25, 850]
        wingTemp = 1
        alliedShipList.append(GenericAllyship(alliedShipImage, 10, 10, [-1, 0, 0, 0], positionTemp, wingTemp, i, 1, 1000))

    idCounter = 10

    for i in range(10):
        positionTemp=[1270+i*25, 850]
        wingTemp = 2
        alliedShipList.append(GenericAllyship(alliedShipImage, 10, 10, [-1, 0, 0, 0], positionTemp, wingTemp, idCounter + i, 1, 300))

    idCounter = 20

    for i in range(10):
        positionTemp=[690+i*25, 800]
        wingTemp = 3
        alliedShipList.append(GenericAllyship(alliedShipImage, 10, 10, [-1, 0, 0, 0], positionTemp, wingTemp, idCounter + i, 1, 300))



    #### enemy ships

    for i in range(10):
        positionTemp=[100+i*25, 100]
        wingTemp = 1
        enemyShipList.append(GenericAllyship(enemyShipimage, 10, 10, [0, 1, 0, 0], positionTemp, wingTemp, i, 1, 300))

    idCounter = 10

    for i in range(10):
        positionTemp=[1270+i*25, 100]
        wingTemp = 2
        enemyShipList.append(GenericAllyship(enemyShipimage, 10, 10, [0, 1, 0, 0], positionTemp, wingTemp, idCounter + i, 1, 300))

    idCounter = 20

    for i in range(10):
        positionTemp=[690+i*25, 150]
        wingTemp = 3
        enemyShipList.append(GenericAllyship(enemyShipimage, 10, 10, [0, 1, 0, 0], positionTemp, wingTemp, idCounter + i, 1, 300))

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if whatShipControll == 0:
                    if event.key == pygame.K_LEFT:
                        direction = "left"
                        if mainShip.speedVector[3] == 1:
                            _thread.start_new_thread(say, ("Vertical movement stop.",))
                            mainShip.speedVector[2] = 0
                            mainShip.speedVector[3] = 0
                        else:
                            _thread.start_new_thread(say, ("Ship moving left.",))
                            mainShip.speedVector[2] = -1
                            mainShip.speedVector[3] = 0
                    elif event.key == pygame.K_RIGHT:
                        direction = "right"
                        if mainShip.speedVector[2] == -1:
                            _thread.start_new_thread(say, ("Vertical movement stop.",))
                            mainShip.speedVector[3] = 0
                            mainShip.speedVector[2] = 0
                        else:
                            _thread.start_new_thread(say, ("Ship moving right.",))
                            mainShip.speedVector[3] = 1
                            mainShip.speedVector[2] = 0
                    elif event.key == pygame.K_UP:
                        direction = "up"
                        if mainShip.speedVector[1] == 1:
                            _thread.start_new_thread(say, ("Horizontal movement stop.",))
                            mainShip.speedVector[1] = 0
                            mainShip.speedVector[0] = 0
                        else:
                            _thread.start_new_thread(say, ("Ship moving ahead.",))
                            mainShip.speedVector[0] = -1
                            mainShip.speedVector[1] = 0
                    elif event.key == pygame.K_DOWN:
                        direction = "down"
                        if mainShip.speedVector[0] == -1:
                            _thread.start_new_thread(say, ("Horizontal movement stop.",))
                            mainShip.speedVector[0] = 0
                            mainShip.speedVector[1] = 0
                        else:
                            _thread.start_new_thread(say, ("Ship moving back.",))
                            mainShip.speedVector[0] = 0
                            mainShip.speedVector[1] = 1
                    elif event.key == pygame.K_s:
                        _thread.start_new_thread(say, ("Scanning nearby space for enemies.",))
                        scanYesOrNo = 1
                        tempShipList = []
                        for i in range(len(alliedShipList)):
                            if alliedShipList[i].wing == 1:
                                tempShipList.append(alliedShipList[i])

                        wprowadzFormacje(alliedShipList, "klin", 1)
                    elif event.key == pygame.K_SPACE:
                        _thread.start_new_thread(say, ("Firing lasers from flahship",))
                        endTimeLaserMc = time.time()
                        if endTimeLaserMc - startTimeLaserMc > 1:
                            startTimeLaserMc = time.time()
                            if mainShip.direction == "up":
                                tempPosition = [mainShip.position[0] + 12, mainShip.position[1] + 10]
                                startingPosition = [mainShip.position[0] + 12, mainShip.position[1] + 10]
                                tempSpeed = [-10, 0, 0, 0]
                            if mainShip.direction == "down":
                                tempPosition = [mainShip.position[0] + 12, mainShip.position[1] - 10]
                                startingPosition = [mainShip.position[0] + 12, mainShip.position[1] - 10]
                                tempSpeed = [0, 10, 0, 0]
                            if mainShip.direction == "left":
                                tempPosition = [mainShip.position[0] - 10, mainShip.position[1] + 12]
                                startingPosition = [mainShip.position[0] - 10, mainShip.position[1] + 12]
                                tempSpeed = [0, 0, -10, 0]
                            if mainShip.direction == "right":
                                tempPosition = [mainShip.position[0] + 10, mainShip.position[1] + 12]
                                startingPosition = [mainShip.position[0] + 10, mainShip.position[1] + 12]
                                tempSpeed = [0, 0, 0, 10]

                            laser = Laser(startingPosition, tempPosition, mainShip, tempSpeed, redLaser)
                            shotsList.append(laser)
                    elif event.key == pygame.K_ESCAPE:
                        _thread.start_new_thread(say, ("Disengaging from battle",))
                        gameExit = True
                    elif event.key == pygame.K_0:
                        _thread.start_new_thread(say, ("Controling flagship",))
                        whatShipControll = 0
                    elif event.key == pygame.K_1:
                        _thread.start_new_thread(say, ("Controling wing 1",))
                        whatShipControll = 1
                    elif event.key == pygame.K_2:
                        _thread.start_new_thread(say, ("Controling wing 2",))
                        whatShipControll = 2
                    elif event.key == pygame.K_3:
                        _thread.start_new_thread(say, ("Controling wing 3",))
                        whatShipControll = 3
                    elif event.key == pygame.K_4:
                        _thread.start_new_thread(say, ("Controling wing 4",))
                        whatShipControll = 4
                    elif event.key == pygame.K_5:
                        _thread.start_new_thread(say, ("Controling wing 5",))
                        whatShipControll = 5
                else:
                    tempNumber = 0
                    for i in range(len(alliedShipList)):
                        if alliedShipList[i].wing == whatShipControll:
                            tempNumber = i
                            break
                    ######### LEFT
                    if event.key == pygame.K_LEFT:
                        direction = "left"
                        if alliedShipList[tempNumber].speedVector[3] == 1:
                            temp_string = "Wing " + str(whatShipControll) + " Vertical movement stop."
                            _thread.start_new_thread(say, (temp_string,))
                            for i in range(len(alliedShipList)):
                                if alliedShipList[i].wing == whatShipControll:
                                    alliedShipList[i].speedVector[2] = 0
                                    alliedShipList[i].speedVector[3] = 0
                        else:
                            temp_string = "Wing" + str(whatShipControll) + " moving left."
                            _thread.start_new_thread(say, (temp_string,))
                            for i in range(len(alliedShipList)):
                                if alliedShipList[i].wing == whatShipControll:
                                    alliedShipList[i].speedVector[2] = -1
                                    alliedShipList[i].speedVector[3] = 0
                    ######## RIGHT
                    elif event.key == pygame.K_RIGHT:
                        direction = "right"
                        if alliedShipList[tempNumber].speedVector[2] == -1:
                            temp_string = "Wing" + str(whatShipControll) + " Vertical movement stop."
                            _thread.start_new_thread(say, (temp_string,))
                            for i in range(len(alliedShipList)):
                                if alliedShipList[i].wing == whatShipControll:
                                    alliedShipList[i].speedVector[3] = 0
                                    alliedShipList[i].speedVector[2] = 0
                        else:
                            temp_string = "Wing" + str(whatShipControll) + " moving right."
                            _thread.start_new_thread(say, (temp_string,))
                            for i in range(len(alliedShipList)):
                                if alliedShipList[i].wing == whatShipControll:
                                    alliedShipList[i].speedVector[3] = 1
                                    alliedShipList[i].speedVector[2] = 0
                    elif event.key == pygame.K_UP:
                        direction = "up"
                        if alliedShipList[tempNumber].speedVector[1] == 1:
                            temp_string = "Wing" + str(whatShipControll) + " Horizontal movement stop."
                            _thread.start_new_thread(say, (temp_string,))
                            for i in range(len(alliedShipList)):
                                if alliedShipList[i].wing == whatShipControll:
                                    alliedShipList[i].speedVector[1] = 0
                                    alliedShipList[i].speedVector[0] = 0
                        else:
                            temp_string = "Wing" + str(whatShipControll) + " moving ahead."
                            _thread.start_new_thread(say, (temp_string,))
                            for i in range(len(alliedShipList)):
                                if alliedShipList[i].wing == whatShipControll:
                                    alliedShipList[i].speedVector[0] = -1
                                    alliedShipList[i].speedVector[1] = 0
                    elif event.key == pygame.K_DOWN:
                        direction = "down"
                        if alliedShipList[tempNumber].speedVector[0] == -1:
                            temp_string = "Wing" + str(whatShipControll) + " Horizontal movement stop."
                            _thread.start_new_thread(say, (temp_string,))
                            for i in range(len(alliedShipList)):
                                if alliedShipList[i].wing == whatShipControll:
                                    alliedShipList[i].speedVector[0] = 0
                                    alliedShipList[i].speedVector[1] = 0
                        else:
                            temp_string = "Wing" + str(whatShipControll) + " moving back."
                            _thread.start_new_thread(say, (temp_string,))
                            for i in range(len(alliedShipList)):
                                if alliedShipList[i].wing == whatShipControll:
                                    alliedShipList[i].speedVector[0] = 0
                                    alliedShipList[i].speedVector[1] = 1
                    elif event.key == pygame.K_s:
                        if scanYesOrNo == 1:
                            scanYesOrNo = 0
                        else:
                            _thread.start_new_thread(say, ("Scanning nearby space for enemies.",))
                            scanYesOrNo = 1
                    elif event.key == pygame.K_0:
                        _thread.start_new_thread(say, ("Controling flagship",))
                        whatShipControll = 0
                    elif event.key == pygame.K_1:
                        _thread.start_new_thread(say, ("Controling wing 1",))
                        whatShipControll = 1
                    elif event.key == pygame.K_2:
                        _thread.start_new_thread(say, ("Controling wing 2",))
                        whatShipControll = 2
                    elif event.key == pygame.K_3:
                        _thread.start_new_thread(say, ("Controling wing 3",))
                        whatShipControll = 3
                    elif event.key == pygame.K_4:
                        _thread.start_new_thread(say, ("Controling wing 4",))
                        whatShipControll = 4
                    elif event.key == pygame.K_5:
                        _thread.start_new_thread(say, ("Controling wing 5",))
                        whatShipControll = 5
                    elif event.key == pygame.K_SPACE:
                        endTimeLaser = time.time()
                        for i in range(len(alliedShipList)):
                            if alliedShipList[i].wing == whatShipControll and endTimeLaser - alliedShipList[i].startTime > 1:
                                alliedShipList[i].startTime = time.time()
                                if alliedShipList[i].direction == "up":
                                    tempPosition = [alliedShipList[i].position[0] + 12, alliedShipList[i].position[1] + 10]
                                    startingPosition = [alliedShipList[i].position[0] + 12, alliedShipList[i].position[1] + 10]
                                    tempSpeed = [-20, 0, 0, 0]
                                if alliedShipList[i].direction == "down":
                                    tempPosition = [alliedShipList[i].position[0] + 12, alliedShipList[i].position[1] - 10]
                                    startingPosition = [alliedShipList[i].position[0] + 12, alliedShipList[i].position[1] - 10]
                                    tempSpeed = [0, 20, 0, 0]
                                if alliedShipList[i].direction == "left":
                                    tempPosition = [alliedShipList[i].position[0] - 10, alliedShipList[i].position[1] + 12]
                                    startingPosition = [alliedShipList[i].position[0] - 10, alliedShipList[i].position[1] + 12]
                                    tempSpeed = [0, 0, -20, 0]
                                if alliedShipList[i].direction == "right":
                                    tempPosition = [alliedShipList[i].position[0] + 10, alliedShipList[i].position[1] + 12]
                                    startingPosition = [alliedShipList[i].position[0] + 10, alliedShipList[i].position[1] + 12]
                                    tempSpeed = [0, 0, 0, 20]

                                laser = Laser(startingPosition, tempPosition, alliedShipList[i], tempSpeed, redLaser)
                                shotsList.append(laser)

        positionEnemy[0] = lead_x_enemy
        positionEnemy[1] = positionEnemy[1] + mainEnemyShip.speedVector[0] + mainEnemyShip.speedVector[1]

        position[0] = position[0] + mainShip.speedVector[2] + mainShip.speedVector[3]
        position[1] = position[1] + mainShip.speedVector[0] + mainShip.speedVector[1]

        mainShip.position[0] = position[0]
        mainShip.position[1] = position[1]

        gameDisplay.fill(white)
        #gameDisplay.blit(bg, (0, 0))
        # wazne!!!!!!!!!!!
        # dziala na zasadzie: stworz 2 takie same surface, na pierwszym robimy klatke, a drugi to backup.
        # w kolejnej klatce nadpisujemy backupem i rysujemy od nowa
        # oszczedza sporo czasu na stworzenie background i wiekszosci klatki
        tempGameDisplay = copy.copy(tempGameDisplayReadyz)


        mainShip.ruch()
        mainShip.wyswietl(tempGameDisplay)

        mainEnemyShip.ruch()
        mainEnemyShip.wyswietl(tempGameDisplay)

        i = 0
        while i in range(len(shotsList)):
            if shotsList[i].position[0] > 1600 or shotsList[i].position[0] < 0 or \
                    shotsList[i].position[1] < 0 or shotsList[i].position[1] > 1200:
                del shotsList[i]
            else:
                i += 1

        i = 0
        while i in range(len(shotsList)):
            if shotsList[i].position[0] > shotsList[i].startingPosition[0] + shotsList[i].owner.weaponRange or shotsList[i].position[0] < shotsList[i].startingPosition[0] - shotsList[i].owner.weaponRange or \
                    shotsList[i].position[1] > shotsList[i].startingPosition[1] + shotsList[i].owner.weaponRange or shotsList[i].position[1] < shotsList[i].startingPosition[1] - shotsList[i].owner.weaponRange:
                del shotsList[i]
            else:
                i += 1

        for i in range(len(shotsList)):
            shotsList[i].position[0] = shotsList[i].position[0] + shotsList[i].speedVector[2] + shotsList[i].speedVector[3]
            shotsList[i].position[1] = shotsList[i].position[1] + shotsList[i].speedVector[0] + shotsList[i].speedVector[1]

        for i in range(len(shotsList)):
            shotsList[i].wyswietl(tempGameDisplay)



        for i in range(len(alliedShipList)):
            alliedShipList[i].position[0] = alliedShipList[i].position[0] + alliedShipList[i].speedVector[2] + alliedShipList[i].speedVector[3]
            alliedShipList[i].position[1] = alliedShipList[i].position[1] + alliedShipList[i].speedVector[0] + alliedShipList[i].speedVector[1]

        for i in range(len(enemyShipList)):
            enemyShipList[i].position[0] = enemyShipList[i].position[0] + enemyShipList[i].speedVector[2] + enemyShipList[i].speedVector[3]
            enemyShipList[i].position[1] = enemyShipList[i].position[1] + enemyShipList[i].speedVector[0] + enemyShipList[i].speedVector[1]

        for i in range(len(alliedShipList)):
            alliedShipList[i].wyswietl(tempGameDisplay)

        for i in range(len(enemyShipList)):
            enemyShipList[i].wyswietl(tempGameDisplay)


        #for i in range(len(alliedShipList)):
        for i in range(len(enemyShipList)):
            for j in range(len(shotsList)):
                if enemyShipList[i].rectangle.colliderect(shotsList[j].rectangle):
                    if enemyShipList[i].shield > 0:
                        enemyShipList[i].shield -= 5
                    else:
                        enemyShipList[i].hitpoints -= 5
        i = 0
        while i in range(len(enemyShipList)):
            if enemyShipList[i].hitpoints <= 0:
                del enemyShipList[i]
            else:
                i += 1

        zoomNumber = 1.0
        positionScreenX = 0
        positionScreenY = 0
        #tempGameDisplay = pygame.transform.rotozoom(tempGameDisplay, 0, zoomNumber)
        #tempGameDisplay = pygame.transform.smoothscale(tempGameDisplay, (int(1600*zoomNumber), int(1200*zoomNumber)))
        gameDisplay.blit(tempGameDisplay, (positionScreenX, positionScreenY))


        if scanYesOrNo == 1:
            endTime = time.time()

            if make_new_temp:
                create_temp()
                make_new_temp = False

            if endTime - startTime > 1.0:

                make_new_temp = True
                # pygame.image.save(gameDisplay, "tempScreen.png")
                t2.join()
                # pil_img = cv.imread('tempScreen.png')
                # img_bgr = numpy.array(pil_img)

                img_gray = cv.cvtColor(pil_img, cv.COLOR_BGR2GRAY)

                # template = cv.resize(template, (0, 0), fx=zoomNumber, fy=zoomNumber)

                w, h = template.shape[::-1]

                res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

                threshold = 0.80
                loc = numpy.where(res >= threshold)


                for pt in zip(*loc[::-1]):
                    pygame.draw.line(gameDisplay, red, [pt[0], pt[1]], [pt[0] + w, pt[1]], 3)
                    pygame.draw.line(gameDisplay, red, [pt[0], pt[1]], [pt[0], pt[1] + h], 3)
                    pygame.draw.line(gameDisplay, red, [pt[0] + w, pt[1] + h], [pt[0] + w, pt[1]], 3)
                    pygame.draw.line(gameDisplay, red, [pt[0] + w, pt[1] + h], [pt[0], pt[1] + h], 3)

                startTime = time.time()



        pygame.display.update()
        clock.tick(FPS)




def read_temp():
    global pil_img
    pil_img = cv.imread('tempScreen.png')


def create_temp():
    global t1
    global t2

    t1 = threading.Thread(pygame.image.save(gameDisplay, "tempScreen.png"))
    t1.start()
    t1.join()
    t2 = threading.Thread(read_temp())
    t2.start()
