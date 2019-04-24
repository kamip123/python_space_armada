from initGame import *


class EnemyShip:
    hitpoints = 100
    shield = 100
    speedVector = [2, 0, 0, 0]
    position = [0, 0]
    direction = "up"
    head = mcShipImage
    shotsList = [0]

    def __init__(self):
        self.hitpoints = 50
        self.shield = 20
        self.speedVector = [2, 0, 0, 0]
        self.position = [0, 0]
        self.direction = "down"
        self.head = enemyFlagshipimage

    def ruch(self):
        if direction == "right":
            head = pygame.transform.rotate(enemyFlagshipimage, 270)

        if direction == "left":
            head = pygame.transform.rotate(enemyFlagshipimage, 90)

        if direction == "up":
            head = enemyFlagshipimage

        if direction == "down":
            head = pygame.transform.rotate(enemyFlagshipimage, 180)

    def wyswietl(self, gameDisplay):
        gameDisplay.blit(self.head, (self.position[0], self.position[1]))


class McShip:
    def __init__(self):
        self.hitpoints = 100
        self.shield = 100
        self.speedVector = [-1, 0, 0, 0]
        self.position = [0, 0]
        self.direction = "up"
        self.head = mcShipImage
        self.weapon = 2
        self.weaponRange = 400

    def ruch(self):
        if direction == "right":
            head = pygame.transform.rotate(mcShipImage, 270)

        if direction == "left":
            head = pygame.transform.rotate(mcShipImage, 90)

        if direction == "up":
            head = mcShipImage

        if direction == "down":
            head = pygame.transform.rotate(mcShipImage, 180)

    def wyswietl(self, gameDisplay):
        gameDisplay.blit(self.head, (self.position[0], self.position[1]))


class GenericAllyship:

    def __init__(self, genericShipImage, hitpoints, shield, speedVector, position, wing, idShip, weapon, weaponRange):
        self.hitpoints = hitpoints
        self.shield = shield
        self.speedVector = speedVector
        self.position = position
        self.direction = "up"
        self.head = genericShipImage
        self.idShip = idShip
        self.wing = wing
        self.weapon = weapon
        self.weaponRange = weaponRange
        self.startTime = time.time()
        self.rectangle = genericShipImage.get_rect(topleft=(self.position[0], self.position[1]))

    #def ruch(self):
    #    if direction == "right":
    #        head = pygame.transform.rotate(mcShipImage, 270)
    #
    #    if direction == "left":
    #        head = pygame.transform.rotate(mcShipImage, 90)
    #
    #    if direction == "up":
    #        head = mcShipImage
    #
    #   if direction == "down":
    #      head = pygame.transform.rotate(mcShipImage, 180)

    def wyswietl(self, gameDisplay):
        gameDisplay.blit(self.head, (self.position[0], self.position[1]))
        self.rectangle = self.head.get_rect(topleft=(self.position[0], self.position[1]))


class Laser:
    def __init__(self, startingPosition, position, owner, speedVector, head):
        self.startingPosition = startingPosition
        self.position = position
        self.owner = owner
        self.speedVector = speedVector
        self.head = head
        self.rectangle = redLaser.get_rect(topleft=(self.position[0], self.position[1]))

    def wyswietl(self, gameDisplay):
        gameDisplay.blit(self.head, (self.position[0], self.position[1]))
        self.rectangle = redLaser.get_rect(topleft=(self.position[0], self.position[1]))


def wprowadzFormacje(tempShipList, formationType, wingNumber):
    if formationType == "klin":
        shipsList = []
        for i in range(len(tempShipList)):
            if tempShipList[i].wing == wingNumber:
                shipsList.append(tempShipList[i])

        amount = len(shipsList)

        if amount > 2:
            shipsList[int(amount / 2)].position[0] = shipsList[0].position[0] + shipsList[amount-1].position[0]
            shipsList[int(amount / 2)].position[1] -= 100
            for i in range(int(amount / 2) + 1, amount):
                shipsList[i].position[0] = shipsList[i-1].position[0] + 20
                shipsList[i].position[1] = shipsList[i-1].position[1] + 20
            for i in range(int(amount / 2)-1, -1, -1):

                shipsList[i].position[0] = shipsList[i+1].position[0] - 20
                shipsList[i].position[1] = shipsList[i+1].position[1] + 20
