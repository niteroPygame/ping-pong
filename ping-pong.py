from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
clock = time.Clock()
FPS = 60
lost = 0

background = transform.scale(image.load('galaxy.jpg'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, self_x, self_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(self_x, self_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y<357:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y<357:
            self.rect.y += self.speed
    # def fire(self):
    #     bullet = Bullet('bullet.png', self.rect.centerx-(self.rect.x*0.019), self.rect.top, 15,20, 15)
    #     bullets.add(bullet)

racket1 = Player('racket.png', 20,200,39,136,6)
racket2 = Player('racket.png',640,200,39,136,6)
ball = GameSprite('tenis_ball.png',350,250,50,50,7)
game = True
finish = False
speed_x = 5
speed_y = 5
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        racket1.reset()
        racket2.reset()
        ball.reset()
        ball.update()
        racket1.update_l()
        racket2.update_r()
        clock.tick(FPS)
        display.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.x > win_width-50  or ball.rect.x < 0:
            finish = True
