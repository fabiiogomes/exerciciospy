# Importando o PyGame
import pygame
import os

# Inicializando o PyGame
pygame.init()

pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
pygame.event.wait()