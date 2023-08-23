from harvesting_asteroids.globaali import Globaali
from harvesting_asteroids.domain.objekti import Objekti
from pygame import KEYDOWN, KEYUP, K_UP, K_DOWN, K_RSHIFT, K_LEFT, K_RIGHT, K_SPACE


class Alus(Objekti):

    def __init__(self, kuva, kulman_muutos, paikka, nopeus, sirpaleet):
        Objekti.__init__(self, kuva, kulman_muutos, paikka, nopeus)
        self.sirpaleet = sirpaleet
        self.tulta = False

    def ohjaus(self, e):
        if e.type == KEYDOWN:
            if e.key == K_UP:
                self.eteenpain()
            elif e.key == K_DOWN:
                self.taaksepain()
            elif e.key == K_RSHIFT:
                self.nopeus = 0
            elif e.key == K_LEFT:
                self.kulman_muutos = 1.5
            elif e.key == K_RIGHT:
                self.kulman_muutos = -1.5
            elif e.key == K_SPACE and not self.suojassa():
                self.tulta = True
        elif e.type == KEYUP:
            if e.key == K_LEFT or e.key == K_RIGHT:
                self.kulman_muutos = 0

    def eteenpain(self):
        self.nopeus = 2.5
        self.aseta_suunta()

    def taaksepain(self):
        self.nopeus = -1
        self.aseta_suunta()

    def suojassa(self):
        s = [self.paikka[0] < 0, self.paikka[0] > Globaali.KOKO[0],
             self.paikka[1] < 0, self.paikka[1] > Globaali.KOKO[1]]
        return True in s

    def update(self, *args, **kwargs) -> None:
        self.siirra()
        if not self.kulman_muutos == 0:
            self.kaanny()
        if not self.nopeus == 0:
            self.liiku()
