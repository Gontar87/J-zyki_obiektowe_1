from abc import ABC, abstractmethod
from models.model import Model
from views.view import View


class AbstractApp(ABC):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller

    @abstractmethod
    def run_app(self):
        pass

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, new_controller):
        self.__controller = new_controller


class App(AbstractApp):
    def __init__(self, controller):
        super().__init__(controller)
        self.__model = Model(800, 400, 10 )
        self.__view = View('View', self.__model)
        self.__model.add_observer(self.__view)


        controller.model = self.__model
        controller.view = self.__view

    def run_app(self):
        self.controller.graj()
