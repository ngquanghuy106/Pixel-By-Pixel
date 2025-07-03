import sys
from random import randint
import time as t
import pygame as pg

clock = pg.time.Clock()
status = True

def init(w, h):
    pg.init()
    return pg.display.set_mode((w, h))

def caption(text):
    pg.display.set_caption(text)

def draw(screen, pos, color):
    pg.draw.rect(screen, color, pg.Rect(pos[0], pos[1], 1, 1))

def detect_x():
    global status
    for event in pg.event.get():
        if event.type == pg.QUIT:
            status = False

def exit():
    pg.quit()
    sys.exit()

def flip():
    pg.display.flip()

def tick(fps):
    clock.tick(fps)

def mouse_pos():
    return pg.mouse.get_pos()

def mouse_click():
    return pg.mouse.get_pressed()

def key_down():
    return pg.key.get_pressed()

def rand(min, max):
    return randint(min, max)

def load_sound(path):
    return pg.mixer.Sound(path)

def play_sound(sound):
    sound.play()

def get_time():
    return t.time()

version = "v0.1b"

if __name__ == '__main__':
    print("\nBRO this is a module, you need to import it into your .py!")
else:
    print(f"\nPain import successfully! Welcome to Pixel by Pixel - {version}")
    print("By using this module, you are agree to LICENSE (CC BY-NC-ND 4.0)")
