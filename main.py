import sys
import pygame as pg
from settings import Settings


def run_game():
    ai_settings = Settings()

    pg.init()  # инициализируем pygame
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # создаем экран игры разрешением 1280х720px
    pg.display.set_caption("Alien Invasion")  # название окна игры
    while True:  # цикл игры
        for event in pg.event.get():  # обработчик событий pygame
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill(ai_settings.bg_color)  # заливаем экран игры цветом
        pg.display.flip()  # обновление кадров в игре


run_game()  # вызываем игровую функцию
