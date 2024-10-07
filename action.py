# Créé par FiercePC, le 02/01/2023 en Python 3.7


import pygame
import time
import os
import random
from importlib import reload
from pygame import mixer

pygame.init()

pygame.display.set_caption("Remember'em All!")
#defaultFont = pygame.font.Font("Nunito-SemiBold.ttf", 60)
gameDisplay = pygame.display.set_mode((1920,1080))
#gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

gare = "espace"

def a():
    pygame.display.update()

def affiche(blaze,x,y, provenance):
    blaze = provenance + "/" + blaze + ".png"
    #blaze.replace("Ã€", "À")
    img = pygame.image.load(blaze)
    gameDisplay.blit(img,(x,y))
    #print("j'ai affiché :", blaze, "aux coordonnées", x, y)
    pygame.display.update()


def creation_mob():
    x = random.randint(1, 1920-100)
    y = random.randint(1, 1080-300)
    censored = random.choice(liste)
    affiche(censored, x, y, "ennemi")
    return x, y

def stopify(son):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("son/" + str(son) + ".ogg"))
    pygame.mixer.Channel(1).set_volume(1)


def random_gare():
    liste_gare = ["gare", "gare2", "gare3", "espace"]
    gare = random.choice(liste_gare)
    return gare


clock = pygame.time.Clock()

tableau = []    #(name, x, y, étape)    #tableau.insert(0, blabla)

caca = True
en_vie = False
looser = False

milliseconds = 0
seconds = 0
minutes = 0
decompte = 0
x = 0
y = 0
timing = 2000
score = 0
attente = 0


liste = ["rouge", "moi", "kessie", "jaune", "bleu", "vert", "noir", "gris", "blanc", "rose", "violet", "dude", "sans", "thanos", "triste", "avi", "coo", "fro", "pie", "spe", "jar"]
listeL = ["chien"]

affiche(gare, 0, 0, "hud")


pygame.mixer.Channel(0).play(pygame.mixer.Sound("son/" + "Glamour" + ".ogg"))
pygame.mixer.Channel(0).set_volume(0.3)

while caca:
    if milliseconds > 1000:
        seconds += 1
        milliseconds -= 1000
    if seconds > 59:
        minutes += 1
        seconds -= 60
    #print ("{}:{}".format(minutes, seconds))
    ptn = clock.tick_busy_loop(60)
    milliseconds += ptn
    if looser:
        attente += ptn
    if en_vie:
        decompte += ptn

    if looser and attente > 5000:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("son/" + "Glamour" + ".ogg"))
        timing = 2000
        affiche(gare, 0, 0, "hud")
        looser = False

    if seconds > 20:
        timing = 1000


    a = random.randint(1, 20)
    if not en_vie and a == 1 and not looser:
        x, y = creation_mob()
        en_vie = True
        decompte = 0

    if en_vie and decompte > timing and not looser:
        en_vie = False
        affiche(gare, 0, 0, "hud")
        print("perdu looser")
        print("score de ", score)
        milliseconds = 0
        seconds = 0
        minutes = 0
        timing = 2
        censored = random.choice(listeL)
        affiche(censored, 0, 0, "defaite")

        if score < 10:
            affiche("0", 1920-64-64, 0, "score")
            affiche(str(score), 1920-64, 0, "score")
        else:
            affiche(str(score)[0], 1920-64-64, 0, "score")
            affiche(str(score)[1], 1920-64, 0, "score")

        score = 0

        looser = True
        attente = 0
        gare = random_gare()

        pygame.mixer.Channel(0).stop()
        stopify("perdu1")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN :
            if pygame.mouse.get_pressed() == (1,0,0):
                mouse = pygame.mouse.get_pos()
                if en_vie and x<mouse[0]<x+100 and y<mouse[1]<y+100:
                    affiche(gare, 0, 0, "hud")
                    score += 1
                    en_vie = False
                    if score < 10:
                        affiche("0", 1920-64-64, 0, "score")
                        affiche(str(score), 1920-64, 0, "score")
                    else:
                        affiche(str(score)[0], 1920-64-64, 0, "score")
                        affiche(str(score)[1], 1920-64, 0, "score")


