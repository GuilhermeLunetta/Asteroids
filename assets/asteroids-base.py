# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import random
import pygame
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')

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

#Classe que representa a nave
class Player(pygame.sprite.Sprite):
    
    #Construindo a classe
    def __init__(self):
        #Construindo a classe principal
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem de fundo
        player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
        self.image = player_img
        
        #Diminuindo o tamanho da imagem
        self.image = pygame.transform.scale(player_img, (50, 38))
        
        #Deixando transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhe sobre posicionamento
        self.rect = self.image.get_rect()
        
        #Centraliza embaixo da tela
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        
        #Velocidade da nave
        self.speedx = 0
        
    #Método que atualiza a posição da nave    
    def update(self):
        self.rect.x += self.speedx
        
        #Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
#Classe Mob
class Mob(pygame.sprite.Sprite):
    
    def __init__(self):
        #Construindo a classe dos meteoros
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem do meteoro
        meteoro_img = pygame.image.load(path.join(img_dir, "meteorBrown_med1.png")).convert()
        self.image = meteoro_img
        
        #Deixando a imagem transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhe sobre posicionamento
        self.rect = self.image.get_rect()
        
        #Randomiza posições do meteoro acima da tela
        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = random.randrange(10, 40)   
        
        #Velocidade em X e em Y
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 9)
        
        
        
        
# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Asteroids")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()

#Chamando o player
player = Player()
mob1 = Mob()
mob2 = Mob()
mob3 = Mob()
mob4 = Mob()
mob5 = Mob()
mob6 = Mob()
mob7 = Mob()
mob8 = Mob()

#Cria um grupo de sprites e add nave
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(mob1)
all_sprites.add(mob2)
all_sprites.add(mob3)
all_sprites.add(mob4)
all_sprites.add(mob5)
all_sprites.add(mob6)
all_sprites.add(mob7)
all_sprites.add(mob8)

#Cria um grupo mobs
mobs = pygame.sprite.Group()
mobs.add(mob1)
mobs.add(mob2)
mobs.add(mob3)
mobs.add(mob4)
mobs.add(mob5)
mobs.add(mob6)
mobs.add(mob7)
mobs.add(mob8)

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
                
            #Verifica se apertou alguma tecla
            if event.type == pygame.KEYDOWN:
                #Dependendo da tecla altera velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                    
            #Verifica se soltou alguma tecla
            if event.type == pygame.KEYUP:
                #Dependendo da tecla altera a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.sppedx = 0
        #Depois de processar os eventos
        #Atualiza a ação de cada sprite
        all_sprites.update()
        
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
