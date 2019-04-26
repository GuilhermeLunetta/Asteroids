# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:12:18 2019

@author: Usuario
"""
import pygame
import random
import time

from os import path
from config import FPS, GAME, QUIT, BLACK

def init_screen(screen, assets):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    # Carrega o fundo do jogo
    background = assets['background']
    background_rect = background.get_rect()
    
    running = True
    while running:
        #ajusta o FPS
        clock.tick(FPS)
        
        #Processa os eventos mouse, teclado, etc
        for event in pygame.event.get():
            #Verifica se foi fechado
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        
        #A cada loop, redesenha o fundo
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        
        #Depois de desenhar inverte o display
        pygame.display.flip()
        
    return state
        