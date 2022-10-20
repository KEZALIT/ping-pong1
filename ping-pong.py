import pygame

pygame.init()

window = pygame.display.set_mode((700,500))
back = (200,255,255)
pygame.display.set_caption('Ping-Pong')

class GameSprite(pygame.sprite.Sprite):
    def init(self, player_image, x, y, w, h, speed):
        super().init()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= win_height:
            self.rect.y = -5
            self.rect.x = randint(0, 630)
            lost += 1



clock = pygame.time.Clock()
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        clock.tick(60)
        pygame.display.update()
