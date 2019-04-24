from initGame import *


def say(s):
    try:
        engine = pyttsx3.init()
        engine.say(s)
        engine.runAndWait()  # blocks
    except:
        return 0


def callback(recognizer, audio):
    global scanYesOrNo
    try:
        global alliedShipList
        topCommand = "top"
        downCommand = "down"
        rightCommand = "right"
        leftCommand = "left"
        forwardCommand = "forward"
        stopCommand = "stop"
        retreatCommand = "retreat"
        scanCommand = "scan"
        scanEnemyCommand = "enemy"
        wingCommand = "wing"
        oneCommand = "one"
        oneoneCommand = "1"

        stringKomendy = recognizer.recognize_google(audio)
        stringKomendy = stringKomendy.lower()
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))

        if stringKomendy.find(topCommand) != -1:
            if mainShip.speedVector[1] == 2:
                say("Horizontal movement stop.")
                mainShip.speedVector[1] = 0
                mainShip.speedVector[0] = 0
            else:
                say("Ship moving ahead.")
                mainShip.speedVector[0] = -2
                mainShip.speedVector[1] = 0

        if stringKomendy.find(downCommand) != -1:
            if mainShip.speedVector[0] == -2:
                say("Horizontal movement stop.")
                mainShip.speedVector[0] = 0
                mainShip.speedVector[1] = 0
            else:
                say("Ship moving back.")
                mainShip.speedVector[0] = 0
                mainShip.speedVector[1] = 2

        if stringKomendy.find(rightCommand) != -1:
            if mainShip.speedVector[2] == -2:
                say("Vertical movement stop.")
                mainShip.speedVector[3] = 0
                mainShip.speedVector[2] = 0
            else:
                say("Ship moving right.")
                mainShip.speedVector[3] = 2
                mainShip.speedVector[2] = 0

        if stringKomendy.find(leftCommand) != -1:
            if mainShip.speedVector[3] == 2:
                say("Vertical movement stop.")
                mainShip.speedVector[2] = 0
                mainShip.speedVector[3] = 0
            else:
                say("Ship moving left.")
                mainShip.speedVector[2] = -2
                mainShip.speedVector[3] = 0

        if stringKomendy.find(forwardCommand) != -1:
            say("All power to the engines. Ship moving at full speed ahead.")
            mainShip.speedVector[0] = -2
            mainShip.speedVector[1] = 0

        if stringKomendy.find(retreatCommand) != -1:
            say("All power to the engines. Ship moving backward at full speed.")
            mainShip.speedVector[0] = 0
            mainShip.speedVector[1] = 2

        if stringKomendy.find(stopCommand) != -1:
            say("Engines stop. Ship not moving")
            mainShip.speedVector[0] = 0
            mainShip.speedVector[1] = 0
            mainShip.speedVector[2] = 0
            mainShip.speedVector[3] = 0

        if stringKomendy.find(scanCommand) != -1:
            say("Scanning nearby space for enemies.")
            scanYesOrNo = 1

        if stringKomendy.find(wingCommand) != -1:
            print("test" + str(alliedShipList[1].speedVector[3]))
            tempNumber = 1
            if stringKomendy.find(oneCommand) != -1 or stringKomendy.find(oneoneCommand):
                whatShipControll = 1
            ######### LEFT
            if stringKomendy.find(leftCommand) != -1:
                if alliedShipList[tempNumber].speedVector[3] == 1:
                    say("Wing" + str(whatShipControll) + "Vertical movement stop.")
                    for i in range(len(alliedShipList)):
                        if alliedShipList[i].wing == whatShipControll:
                            alliedShipList[i].speedVector[2] = 0
                            alliedShipList[i].speedVector[3] = 0
                else:
                    say("Wing" + str(whatShipControll) + " moving left.")
                    for i in range(len(alliedShipList)):
                        if alliedShipList[i].wing == whatShipControll:
                            alliedShipList[i].speedVector[2] = -1
                            alliedShipList[i].speedVector[3] = 0



    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
