from .abstract_model import AbstractModel
import random


class Model(AbstractModel):
    def __init__(self, szerokosc, wysokosc, komorka):
        super().__init__()
        # stworzyc na razie tablice 80 x 40 wypełnioną zerami
        tablica = []
        for j in range(int(szerokosc/komorka)):
            wiersz = []
            for i in range(int(wysokosc/komorka)):
                wiersz.append(round(random.uniform(0, 1)))
            tablica.append(wiersz)
        self.__tablica = tablica
        self.__szerokosc = szerokosc
        self.__wysokosc = wysokosc
        self.__komorka = komorka

    @property
    def tablica(self):
        return self.__tablica

    @property
    def komorka(self):
        return self.__komorka

    @property
    def szerokosc(self):
        return self.__szerokosc

    @property
    def wysokosc(self):
        return self.__wysokosc

    def modify(self, tablica):
        self.__tablica = self.przygotuj_populacje(tablica)
        self.notify()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update()

    def przygotuj_populacje(self, polegry):
        # na początku tworzymy 2-wymiarową listę wypełnioną zerami
        nast_gen = [0] * int(self.__szerokosc/self.__komorka)
        for i in range(int(self.__szerokosc/self.__komorka)):
            nast_gen[i] = [0] * int(self.__wysokosc/self.__komorka)

        # iterujemy po wszystkich komórkach
        for y in range(int(self.__wysokosc/self.__komorka)):
            for x in range(int(self.__szerokosc/self.__komorka)):

                # zlicz populację (żywych komórek) wokół komórki
                populacja = 0
                # wiersz 1
                try:
                    if polegry[x - 1][y - 1] == 1:
                        populacja += 1
                except IndexError:
                    pass
                try:
                    if polegry[x][y - 1] == 1:
                        populacja += 1
                except IndexError:
                    pass
                try:
                    if polegry[x + 1][y - 1] == 1:
                        populacja += 1
                except IndexError:
                    pass

                # wiersz 2
                try:
                    if polegry[x - 1][y] == 1:
                        populacja += 1
                except IndexError:
                    pass
                try:
                    if polegry[x + 1][y] == 1:
                        populacja += 1
                except IndexError:
                    pass

                # wiersz 3
                try:
                    if polegry[x - 1][y + 1] == 1:
                        populacja += 1
                except IndexError:
                    pass
                try:
                    if polegry[x][y + 1] == 1:
                        populacja += 1
                except IndexError:
                    pass
                try:
                    if polegry[x + 1][y + 1] == 1:
                        populacja += 1
                except IndexError:
                    pass

                # "niedoludnienie" lub przeludnienie = śmierć komórki
                if polegry[x][y] == 1 and (populacja < 2 or populacja > 3):
                    nast_gen[x][y] = 0
                # życie trwa
                elif polegry[x][y] == 1 \
                        and (populacja == 3 or populacja == 2):
                    nast_gen[x][y] = 1
                # nowe życie
                elif polegry[x][y] == 0 and populacja == 3:
                    nast_gen[x][y] = 1

        # zwróć nowe polegry z następną generacją komórek
        return nast_gen

