import random
import os

import pygame as pg

pg.init()
pg.mixer.init()

WIDTH = 750
HEIGHT = 750

root = pg.display.set_mode((WIDTH, HEIGHT))

app_folder = os.path.dirname(__file__)
albums_folder = os.path.join(app_folder, "albums")

class ToolBar:
    def __init__(self) -> None:
        self.height = 80
        self.y = self.height
        self.image = pg.Surface((WIDTH, self.height))
        self.image.fill("#62B8DA")

        self.state = "hide"

    def draw(self):
        root.blit(self.image, (0, -self.y))

        if self.state == "show":
            if -self.y <= 0:
                self.y -= 7
            else :
                pass

        if self.state == "hide":
            if -self.height <= -self.y:
                self.y += 7
            else :
                pass        



class Frame:
    def __init__(self, cover) -> None:
        self.cover = cover
    
    def draw(self):
        pg.draw.rect(
            root, "#55AC45", (self.cover.x, self.cover.y, self.cover.size[0], self.cover.size[1]),
            width = 3
        )
    

class Cover:
    def __init__(self) -> None:

        self.image = pg.image.load(os.path.join(albums_folder, "isin mutfagi.png")).convert()
        self.image = pg.transform.scale(self.image, (WIDTH, HEIGHT))
        self.size = self.image.get_size()
        self.x = 0 #WIDTH / 2 - ((self.size[0] / 2))
        self.y = 0 #HEIGHT / 2 - ((self.size[1] / 3) * 2) - 20

        self.width = (int(self.x), int(self.x + self.size[0]))
        self.bottom = self.y + self.size[1]

        self.albums = [
            pg.transform.scale(pg.image.load(os.path.join(albums_folder, "isin mutfagi.png")).convert(), (WIDTH, HEIGHT)),
            pg.transform.scale(pg.image.load(os.path.join(albums_folder, "deev.png")).convert(), (WIDTH, HEIGHT)),
        ]

    def draw(self):
        root.blit(self.image, (self.x, self.y))


class MusicWave:
    def __init__(self, cover, x):
        self.cover = cover
        self.x = x
        self.width = 3
        self.y = self.cover.bottom

        self.max_height = 150

        self.direction = "down"
        self.height = 300

        self.speed = random.randint(6, 11)

    def draw(self):
        pg.draw.rect(root, "#55AC45", (self.x, self.y, self.width, self.height))

    def move(self):
        if self.direction == "down":
            self.y += self.speed
            if self.y > HEIGHT:
                self.direction = "up"
                self.speed = random.randint(5, 10)

        elif self.direction == "up":
            self.y -= self.speed
            if self.y < self.cover.bottom - self.max_height:
                self.direction = "down"
                self.speed = random.randint(5, 10)

def mouse_over():
    mouse_y = pg.mouse.get_pos()[1]
    if mouse_y < toolbar.height:
        toolbar.state = "show"
    else:
        toolbar.state = "hide"


cover = Cover()
frame = Frame(cover)
toolbar = ToolBar()

bars = []

for x in range(cover.width[0], cover.width[1], 3 + 2):
    bars.append(MusicWave(cover, x))

clock = pg.time.Clock()

running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = not running
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                cover.image = random.choice(cover.albums)
                for musicwave in bars:
                    musicwave.y = HEIGHT


    mouse_over()
    
    root.fill((63, 57, 56))
    
    cover.draw()
    frame.draw()
    toolbar.draw()

    for musicwave in bars:
        musicwave.move()
        musicwave.draw()

    pg.display.update()