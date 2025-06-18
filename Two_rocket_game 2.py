import pygame
from pygame.locals import *
pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((119,8,111))
pygame.display.update()
pygame.display.set_caption("Two rockets game")


spaceship_yellow = pygame.image.load("yellow_roc.png")
spaceship_yellow = pygame.transform.scale(spaceship_yellow, (100, 100))
spaceship_red = pygame.image.load("redrocket.png")
spaceship_red = pygame.transform.scale(spaceship_red, (100, 100))
bullet = pygame.image.load("bullet.png")
bg = pygame.image.load("spaceroc.png")

x = 100
y = 100
def draw_window():
    screen.blit(bg,(0,0))
    screen.blit(spaceship_yellow,(250,0))
    screen.blit(spaceship_red,(250,500))
    screen.blit(bullet,(0,0))
    pygame.display.update()

speed = 5


running = True
while running:
    pygame.time.delay(10)
    #screen.fill((0, 0, 0))
    screen.blit(bg,(0,0))  
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and x > 0:
        x -= speed
    if keys[K_RIGHT] and x < WIDTH - 80:
        x += speed

    keys = pygame.key.get_pressed()
    if keys[K_a] and x > 0:
        x -= speed
    if keys[K_d] and x < WIDTH - 80:
        x += speed

    
screen.blit(spaceship_yellow, (x, y))
screen.blit(spaceship_red, (x,y))
pygame.display.update()

pygame.quit()
     
     
     

