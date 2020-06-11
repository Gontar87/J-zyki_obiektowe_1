from .abstract_controller import AbstractController
import pygame
import sys
import random
from pygame.locals import *

class Controller(AbstractController):
    def __init__(self, model=None, view=None):
        super().__init__(model, view)
        self.__przycisk_wdol = False

    def get_user_input(self):
        pass

    def graj(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.view.show()


