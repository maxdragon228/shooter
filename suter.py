from pygame import *
from random import randint 


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            print("Left")
        if keys[K_RIGHT] and self.rect.x < w - 85:
            self.rect.x += self.speed
            print("Right")
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx,
                        self.rect.top, 15, 20, 15)
        bullets.add(bullet)

class Bullet (GameSprite):
    def ubdate(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill

class Enemy(GameSprite):
    def ubdate(self):
        self.rect.y +=self.speed
        global score 
        if self.rect.y > h:
            self.rect.y = -50
            self.rect.x = randint(20, w-100)



w = 700
h = 500
display.set_caption("Shooter")
window = display.set_mode((w, h))
background = transform.scale(image.load('galaxy.jpg'), (w, h))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound("fire.ogg")


font.init()
text1 = font.Font(None, 36)
text2 = font.Font(None, 80)


player = Player("rocket.png", 200, h-100, 80, 100, 5)
monsters = sprite.Group()
bullets = sprite.Group()
for i in range(1, 6):
    monster = Enemy("ufo.png", randint(20, w-100), -50, 80, 50, randint(1, 4))
    monsters.add(monster)

score = 0
killed = 0
goal = 10
max_lost = 3
clock = time.Clock()
finish = False
game = True
bullets = sprite.Group()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False       
        elif e.key == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                fire_sound.play()

    if not finish:
        mw.blit(background, (0, 0))
        player.update()
        bullets.update()
        player.reset()
        monsters.draw(mw)
        bullets.draw(mw)
        monsters.update()

        text_killed = text1.render(
            "Рахунок " + str(killed), 1, (255, 0, 0), (255, 255, 255))
        mw.blit(text_killed, (20, 20))

        text_lost = text1.render(
            "Пропущено "+str(score), 1, (135, 145, 240), (255, 255, 255))
        mw.blit(text_lost, (20, 50))
        
    display.update()
    clock.tick(30)



