from .abstract_view import AbstractView
import pygame
import sys
import random
from pygame.locals import *


import random


class View(AbstractView):
    def __init__(self, name, model):
        super().__init__(name, model)
        self.__model = model
        pygame.init()
        self.__okno_gry = pygame.display.set_mode((self.__model.szerokosc, self.__model.wysokosc), 0, 32)
        pygame.display.set_caption('Gra o życie')

    def add_component(self, comp):
        pass


    def update(self):
        pass

    # tu wyświetlamy
    def show(self):
        self.__okno_gry.fill((0,0,0,))
        for y in range(int(self.__model.wysokosc/self.__model.komorka)):
            for x in range(int(self.__model.szerokosc/self.__model.komorka)):
                if str(self.__model.tablica[x][y]) == '1':
                    pygame.draw.rect(self.__okno_gry, (255, 255, 255), Rect((x * self.__model.komorka, y * self.__model.komorka), (self.__model.komorka, self.__model.komorka)), 1)
        pygame.display.update()
        pygame.time.delay(1000)
        self.__model.modify(self.__model.tablica)














