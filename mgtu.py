import pygame as pg


pg.init()
H, W = 500, 500
FPS = 60
jumpstep = 10
WHITE = (255, 255, 255)
GREEN = (0, 200, 200)
c_rad = 40
clock = pg.time.Clock()
jcount_const = 5

pg.init()
sc = pg.display.set_mode((H, W))
pg.display.set_caption('Игра по заданию МГТУ')
sc.fill(WHITE)


def check_close():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print('Game Over')
            pg.quit()


class Circle:

    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.jcount = 10
        self.space_pressed = False

    def drawing(self):
        pg.draw.circle(sc, self.color, (self.x, self.y), self.rad)

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.x > c_rad:
            self.x -= jumpstep
        elif keys[pg.K_RIGHT] and self.x < W - c_rad:
            self.x += jumpstep
        if not(self.space_pressed):
            if keys[pg.K_UP] and self.y > self.jcount + (c_rad * 2):
                self.y -= jumpstep
            if keys[pg.K_DOWN] and self.y < H - c_rad - self.jcount:
                self.y += jumpstep
            if keys[pg.K_SPACE]:
                self.space_pressed = True
        else:
            if self.jcount >= -10:
                self.y -= int(self.jcount * abs(self.jcount) * 0.5)
                self.jcount -= 1
            else:
                self.space_pressed = False
                self.jcount = 10


Gameboy = Circle(W // 2, H // 2, c_rad, GREEN)


def redraw():
    sc.fill(WHITE)
    Gameboy.drawing()
    pg.display.update()


while True:
    check_close()
    Gameboy.move()
    redraw()
    clock.tick(FPS)
