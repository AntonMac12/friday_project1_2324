import pygame as pg


class Ship:
    def __init__(self, screen):
        """Инициализация корабля и установка его в нужную позицию на экране"""
        self.screen = screen

        # загрузим картинку корабля
        self.image = pg.image.load('images/ship.png')
        self.rect = self.image.get_rect()  # получаю колижн-модель корабля
        self.screen_rect = self.screen.get_rect()   # получаю границы экрана игры

        # каждый корабль будет появляться посередине экрана внизу
        self.rect.centerx = self.screen_rect.centerx  # центр по горизонтали корабля берется из центра экрана
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабль на экране игры"""
        self.screen.blit(self.image, self.rect)
