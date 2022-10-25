import pygame
from pygame import *

class GameSprite(sprite.Sprite):
    def init(self, player_image, x, y, w, h, speed):
        super().init()
        self.image = transform.scale(image.load(player_image),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.y > 1:
            self.rect.y -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.y < 415:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 410:
            self.rect.y += self.speed

# class Enemy(GameSprite):
#     def



player = Player("nik.png", 10, 400, 75, 75, 10)
player2 = Player2("nik.png", 615, 400, 75, 85, 10)


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PING-PONG")

background = transform.scale(image.load("fon.jpg"), (win_width, win_height))

clock = pygame.time.Clock()

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player.reset()
        player.update()
        player2.reset()
        player2.update()

    clock.tick(40)
    display.update()
