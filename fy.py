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
        if keys[K_s] and self.rect.y < 635:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed() 
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
player1 = Player('racket.png', 25, 400, 30, 100, 10)
player2 = Player('racket.png', 650, 400, 30, 100, 10)

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_widht, player_height, player_speed):
        super().__init__(player_image, player_x, player_y, player_widht, player_height, player_speed)
        self.speed_x = player_speed
        self.speed_y = player_speed
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 450:
            self.speed_y *= -1
        if self.rect.x < 0 or self.rect.x > 650:
            self.speed_x *= -1


ball = Ball('Ball.jpg', 250, 400, 30, 30, 10)

font.init()
font2 = font.SysFont('Arial', 36)
lose = font2.render("YOU LOSE", 1, (255, 255, 255))
win = font2.render("YOU WIN", 1, (255, 255, 255))

while game:
    window.blit(background, (0, 0))
    player1.update_l()
    player2.update_r()
    player1.reset()
    player2.reset()
    ball.update()
    ball.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
 