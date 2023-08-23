from harvesting_asteroids.globaali import Globaali
from abc import ABC
from pygame import sprite, mask, transform
from math import radians, cos, sin


class Objekti(ABC, sprite.Sprite):

    def __init__(self, kuva, kulman_muutos, paikka, nopeus):
        sprite.Sprite.__init__(self)
        self.kuva = kuva
        self.image = transform.rotozoom(self.kuva, 0, Globaali.SUHDE)
        self.muunnettava = self.image
        self.mask = mask.from_surface(self.image)
        self.koko = self.mask.get_size()
        self.kulma = 0
        self.kulman_muutos = kulman_muutos
        self.paikka = paikka
        self.paikan_muutos = 0, 0
        self.rect = self.image.get_rect()
        self.rect.center = paikka
        self.nopeus = nopeus

    def kaanny(self):
        self.kulma += self.kulman_muutos
        self.image = transform.rotozoom(self.muunnettava, self.kulma, 1)
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = self.paikka
        if abs(self.kulma) == 360:
            self.kulma = 0

    def aseta_suunta(self):
        self.kulman_muutos = 0
        rad = radians(self.kulma)
        self.paikan_muutos = sin(rad) * self.nopeus, cos(rad) * self.nopeus

    def liiku(self):
        self.paikka = self.paikka[0] - self.paikan_muutos[0], self.paikka[1] - self.paikan_muutos[1]
        self.rect = self.image.get_rect()
        self.rect.center = self.paikka

    def ylitykset(self):
        y = [self.paikka[0] < -self.koko[0] / 2, self.paikka[0] > Globaali.KOKO[0] + self.koko[0] / 2,
             self.paikka[1] < -self.koko[1] / 2, self.paikka[1] > Globaali.KOKO[1] + self.koko[1] / 2]
        kohta = y.index(True) if True in y else -1
        return True in y, kohta

    def siirra(self):
        ylitys, siirros = self.ylitykset()
        if ylitys:
            self.paikka = [(Globaali.KOKO[0] + self.koko[0] / 2, self.paikka[1]),
                           (-self.koko[0] / 2, self.paikka[1]),
                           (self.paikka[0], Globaali.KOKO[1] + self.koko[1] / 2),
                           (self.paikka[0], -self.koko[1] / 2)][siirros]

    def ylitys(self):
        return self.ylitykset()[0]

    def update(self, *args, **kwargs) -> None:
        pass
