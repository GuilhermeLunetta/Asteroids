# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import random
import pygame
from os import path
import time

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

#Classe que representa a nave
class Player(pygame.sprite.Sprite):
    
    #Construindo a classe
    def __init__(self, player_img):
        #Construindo a classe principal
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem de fundo
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
        
        #Rario do círculo de colisão
        self.radius = 25
        
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
    
    def __init__(self, mob_img):
        #Construindo a classe dos meteoros
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem do meteoro
        self.image = mob_img
        
        #Deixando a imagem mais clara
        self.image = pygame.transform.scale(mob_img, (50, 38))
        
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
        
        #Raio da colisão entre nave e meteoro
        self.radius = int(self.rect.width * .85/2)
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #Se o meteoro passar do final da tela volta pra cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH +20:
            self.rect.x = random.randrange(0, WIDTH)
            self.rect.y = random.randrange(10, 40)   
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(2, 9)

#Classe bullet que representa o tiro
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y, bullet_img):
        #Construindo a classe tiros
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem do tiro
        self.image = bullet_img
        
        self.rect = self.image.get_rect()
        
        #Deixando imagem transparente
        self.image.set_colorkey(BLACK)
        
        #Velocidade Y (sobe)
        self.speedy = -10
        
        #Coloca no lugar definido
        self.rect.bottom = y
        self.rect.centerx = x
    
    def update(self):
        self.rect.y += self.speedy
        
        #Se o tiro passar do início da tela, morre
        if self.rect.bottom < 0:
            self.kill()
class Explosion(pygame.sprite.Sprite):
    
    #Classe que representa a explosao
    def __init__(self, center, explosion_anim):
        #Construtor da classe
        pygame.sprite.Sprite.__init__(self)
        
        #Carrega a animacao
        self.explosion_anim = explosion_anim
        
        #Inicia o processo de animacao colocando a primeira imagem na tela
        self.frame = 0
        self.image = self.explosion_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        
        #guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        
        #Controle de ticks da animacao
        self.frame_ticks = 50
    
    def update(self):
        #Verifica o tick atual
        now = pygame.time.get_ticks()
        
        #Verifica quantos ticks se passaram desde a ultima mudança de frame
        elapsed_ticks = now - self.last_update
        
        #Se ja esta na hora de mudar a imagem
        if elapsed_ticks > self.frame_ticks:
            
            #Marca o tick da nova imagem
            self.last_update = now
            
            #avança um quadro
            self.frame += 1
            
            #Verifica se ja chegou no final da animacao
            if self.frame == len(self.explosion_anim):
                #se sim, tchau!
                self.kill()
            else:
                #Se ainda nao, troca imagem
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


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

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = assets['background']
background_rect = background.get_rect()

#Carrega os sons do jogo
pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.4)
boom_sound = assets['boom_sound']
destruction_sound = assets['destruction_sound']
pew_sound = assets['pew_sound']

#Carrega o placar de score
score_font = assets['score_font']

#Chamando o player
player = Player(assets['player_img'])

#Cria um grupo de sprites e add nave
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#Cria um grupo mobs
mobs = pygame.sprite.Group()

bullets = pygame.sprite.Group()

for i in range(8):
    m = Mob(assets['mob_img'])
    all_sprites.add(m)
    mobs.add(m)
    
# Comando para evitar travamentos.
try:
    
    # Loop principal.
    pygame.mixer.music.play(loops=-1)
    
    PLAYING = 0
    EXPLODING = 1
    DONE = 2
    
    lifes = 3
    
    score = 0
    
    state = PLAYING
    while state != DONE:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        if state == PLAYING:
            
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
            
                # Verifica se foi fechado
                if event.type == pygame.QUIT:
                    state = DONE
                
                #Verifica se apertou alguma tecla
                if event.type == pygame.KEYDOWN:
                    #Dependendo da tecla altera velocidade
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(player.rect.centerx, player.rect.top, assets['bullet_img'])
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        pew_sound.play()

                #Verifica se soltou alguma tecla
                if event.type == pygame.KEYUP:
                    #Dependendo da tecla altera a velocidade
                    if event.key == pygame.K_LEFT:
                        player.speedx += 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= 8
                 
        #Depois de processar os eventos
        #Atualiza a ação de cada sprite
        all_sprites.update()
        
        if state == PLAYING:
        
            #Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
            if hits:
                #Toca o som da colisão
                boom_sound.play()
                player.kill()
                lifes -= 1
                explosao = Explosion(player.rect.center, assets['explosion_anim'])
                all_sprites.add(explosao)
                state = EXPLODING
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
                
            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
            #Recriando os meteoros
            for hit in hits:
                m = Mob(assets['mob_img'])
                all_sprites.add(m)
                mobs.add(m)
                #Toca som de explosão
                destruction_sound.play()
            
                #no lugar do meteoro antigo, adicionar explosao
                explosao = Explosion(hit.rect.center, assets['explosion_anim'])
                all_sprites.add(explosao)
                #Ganhou pontos
                score += 100
        
        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lifes == 0:
                    state = DONE
                    
                #Sistema 100000 pontos = + 1 vida
                #elif lifes%100000 == 0:
                    #lifes += 1
                    
                else:
                    #Jogo infinito renascendo a nave
                    state = PLAYING
                    player = Player(assets['player_img'])
                    all_sprites.add(player)
                
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        #Display do score na tela
        text_surface = score_font.render('{:08d}'.format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH/2, 10)
        screen.blit(text_surface, text_rect)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
