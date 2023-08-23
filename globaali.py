from enum import Enum


class Globaali(Enum):

    def __init__(self):
        self.POLKU = self.polku
        self.KOKO = self.koko
        self.SUHDE = self.suhde
        self.LOPETUS = self.lopetus
        self.PELAAJA = self.pelaaja

    @property
    def polku(self):
        return self.POLKU

    @property
    def koko(self):
        return self.KOKO

    @property
    def suhde(self):
        return self.SUHDE

    @property
    def lopetus(self):
        return self.LOPETUS

    @property
    def pelaaja(self):
        return self.PELAAJA

    @polku.setter
    def polku(self, cwd):
        self.POLKU = cwd

    @koko.setter
    def koko(self, xy):
        self.KOKO = xy

    @suhde.setter
    def suhde(self, s):
        self.SUHDE = s

    @lopetus.setter
    def lopetus(self, tosi):
        self.LOPETUS = tosi

    @pelaaja.setter
    def pelaaja(self, nimi):
        self.PELAAJA = nimi
