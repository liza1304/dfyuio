from pygame import *
from random import randint 

window = display.set_mode((700, 500))
display.set_caption("PinPong_game")
background = transform.scale(image.load("fon.jpg"), (700, 500))
game = True
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_widht, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_widht, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

    def update_r(self):
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

player = Player('racket.jpg', 100, 400, 50, 100, 10)









while game:
        window.blit(background, (0, 0))
        player.update()
        player.reset()

        for e in event.get():
            if e.type == QUIT:
                game = False

            clock.tick(FPS)
            display.update()