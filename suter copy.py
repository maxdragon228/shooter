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
        bullet = Bulet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def ubdate(self):
        self.rect.y +=self.speed
        global score 
        if self.rect.y > h:
            self.rect.y = -50
            self.rect.x = randint(20, w-100)




w, h = 700, 500
mw = display.set_caption((w, h))
display.set_caption("Shooter")
background = transform.scale(image.load('galaxy.jpg'), (w, h))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

font.init()
text1 = font.Font(None, 36)
text2 = font.Font(none, 80)


player = Player("rocket.png", 200, h-100, 80,100,5)


monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy("ufo.png", randint(20,w-100), -50,80,50,randin(1,5))
    monster.add(monster)

score = 0
killed = 0
goal = 10
max_lost = 3

clock = time.Clock()
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False       
    if not finish:
        mw.blit(background, (0, 0))
        player.update()
        player.reset()
        monsters.draw(mw)
        monsters.ubdate()

        text_killed = text1.render("Score"+ str(killed, 1, (255,0,0)))
        mw.blit(text_killed, (20, 20))

    display.update()
    clock.tick(30)