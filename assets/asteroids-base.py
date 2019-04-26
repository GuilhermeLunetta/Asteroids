# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.

import pygame
from os import path
from game_screen import game_screen
from config import WIDTH, HEIGHT, snd_dir, img_dir, fnt_dir, BLACK, INIT, GAME, QUIT
from init_screen import init_screen

def load_assets(img_dir, snd_dir, fnt_dir):
    assets = {}
    assets['player_img'] = pygame.image.load(path.join(img_dir, 'playerShip1_orange.png')).convert()
    assets['mob_img'] = pygame.image.load(path.join(img_dir, 'meteorBrown_med1.png')).convert()
    assets['bullet_img'] = pygame.image.load(path.join(img_dir, 'laserRed16.png')).convert()
    assets['background'] = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
    assets['boom_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))
    assets['destruction_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))
    assets['pew_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
    explosion_anim = []
    for i in range(9):
        filename = 'regularExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img = pygame.transform.scale(img, (32, 32))
        img.set_colorkey(BLACK)
        explosion_anim.append(img)
    assets['explosion_anim'] = explosion_anim
    assets['score_font'] = pygame.font.Font(path.join(fnt_dir, 'PressStart2P.ttf'), 28)
    return assets

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Asteroids by Luna")

#Carrega todas as assets uma vez só e guarda num dicionario
assets = load_assets(img_dir, snd_dir, fnt_dir)
    
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = init_screen(screen, assets)
        elif state == GAME:
            state = game_screen(screen, assets)
        else:
            state = QUIT
    
finally:
    pygame.quit()
