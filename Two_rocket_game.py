import pygame
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

def draw():
    screen.blit(bg,(0,0))
    screen.blit(spaceship_yellow,(250,0))
    screen.blit(spaceship_red,(250,500))
    screen.blit(bullet,(0,0))
    pygame.display.update()

     
     
     


while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   running = False
                   pygame.quit()