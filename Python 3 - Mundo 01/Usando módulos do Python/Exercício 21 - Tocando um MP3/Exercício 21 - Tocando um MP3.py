"""
Enunciado do Exercício 21 - Tocando um MP3:

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

import pygame
import time

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load('audio021.mp3')

# Reproduz o áudio
pygame.mixer.music.play()

# Mantém o script rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    time.sleep(1)
