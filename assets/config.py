# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:55:06 2019

@author: Usuario
"""

# Importando as bibliotecas necessárias.
from os import path


# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')

# Estabelece a pasta que contém as músicas
snd_dir = path.join(path.dirname(__file__), 'snd')

fnt_dir = path.join(path.dirname(__file__), 'font')

# Dados gerais do jogo.
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Estados do init_screen
INIT = 0
GAME = 1
QUIT = 2

