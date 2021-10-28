import pygame as pg
pg.init()
gameRun = True
SIZE = H, W = 500, 500
FPS = 60
JumpStep = 10
WHITE = (255, 255, 255)
GREEN = (0, 200, 200)
C_rad = 40
clock = pg.time.Clock()
JCount_const = 5
pg.display.set_caption('Игра по заданию МГТУ')
sc = pg.display.set_mode(SIZE)
sc.fill(WHITE)


def check_close():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            gameRun = False


class Circle:

    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.JCount = 10
        self.Space_pressed = False

    def drawing(self):
        pg.draw.circle(sc, self.color, (self.x, self.y), self.rad)

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.x > C_rad:
            self.x -= JumpStep
        elif keys[pg.K_RIGHT] and self.x < W - C_rad:
            self.x += JumpStep
        if not(self.Space_pressed):
            if keys[pg.K_UP] and self.y > self.JCount + (C_rad * 2):
                self.y -= JumpStep
            if keys[pg.K_DOWN] and self.y < H - C_rad - self.JCount:
                self.y += JumpStep
            if keys[pg.K_SPACE]:
                self.Space_pressed = True
        else:
            if self.JCount >= -10:
                self.y -= int(self.JCount * abs(self.JCount) * 0.5)
                self.JCount -= 1
            else:
                self.Space_pressed = False
                self.JCount = 10


Gameboy = Circle(W // 2, H // 2, C_rad, GREEN)


def redraw():
    sc.fill(WHITE)
    Gameboy.drawing()
    pg.display.update()


while gameRun:
    check_close()
    Gameboy.move()
    redraw()
    clock.tick(FPS)


print('Game Over')
