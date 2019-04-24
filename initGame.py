import numpy
import random
import pygame
import speech_recognition as sr
import pyaudio
import cv2 as cv
import time
from difflib import SequenceMatcher
import pyttsx3

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

alliedShipList = []
enemyShipList = []
shotsList = []

display_width = 1600
display_height = 900

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Flight')

bg = pygame.image.load("assets/background.png")
backgroundStartingScreen = pygame.image.load("assets/backgroundStartingScreen.png")
galaxyMap = pygame.image.load("assets/galaxyMap.png")

homePlanet = pygame.image.load("assets/homePlanet.png")
strzalka = pygame.image.load("assets/strzalka.png")

galaxyIconFinnished = pygame.image.load('assets/galaxyIconFinnished.png')
galaxyIconOne = pygame.image.load('assets/galaxyIconOne.png')
galaxyIconTwo = pygame.image.load('assets/galaxyIconTwo.png')

mcShipImage = pygame.image.load('assets/statekGracza.png')
enemyFlagshipimage = pygame.image.load('assets/enemyStatek.png')

alliedShipImage = pygame.image.load('assets/statekAlliedShip.png')
enemyShipimage = pygame.image.load('assets/statekEnemyShip.png')

alliedShipImageVenator = pygame.image.load('assets/venator.png')
enemyShipimageFrigate = pygame.image.load('assets/cisFrigate.png')

redLaser = pygame.image.load('assets/redLaser.png')
blueLaser = pygame.image.load('assets/blueLaser.png')

FPS = 30
direction = "up"

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

scanYesOrNo = 0

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

tempGameDisplayReady = pygame.Surface((6000, 3376))
tempGameDisplayReady.blit(bg, (0, 0))
tempGameDisplayReadyz = pygame.Surface((6000, 3376))
tempGameDisplayReadyz.blit(bg, (0, 0))


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)
