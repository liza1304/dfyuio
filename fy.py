from pygame import *
from random import randint


window = display.set_mode((700, 500))
display.set_caption("Rases")
background = transform.scale(image.load("road.jpg"), (700, 500))
game = True
clock = time.Clock()
FPS = 60






while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
             game = False
























    clock.tick(FPS)
    display.update()