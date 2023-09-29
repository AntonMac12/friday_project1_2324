import sys
import pygame as pg


def check_events():
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


def update_screen(settings, screen, ship):
    screen.fill(settings.bg_color)  # заливаем экран игры цветом
    ship.blitme()
    pg.display.flip()  # обновление кадров в игре
