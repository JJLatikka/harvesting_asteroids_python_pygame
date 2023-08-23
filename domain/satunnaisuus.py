from harvesting_asteroids.globaali import Globaali
from harvesting_asteroids.domain.asteroidi import Asteroidi
from harvesting_asteroids.visual.asteroidin_piirto import AsteroidinKuvat
from random import randint, choice, gauss
from pygame import image


class Asteroidigeneraattori:

    def __init__(self, maara):
        self.maara = maara
        self.asteroidit = self.luo_asteroidit()

    def kokoluokka(self):
        kl = int(abs(gauss(2, 1))) + 1
        if kl > 5:
            kl = 5
        return kl

    def paikka(self):
        d = {1: (0, randint(0, Globaali.KOKO[1])),
             2: (Globaali.KOKO[0], randint(0, Globaali.KOKO[1])),
             3: (randint(0, Globaali.KOKO[0]), 0),
             4: (randint(0, Globaali.KOKO[0]), Globaali.KOKO[1])}
        return d[choice([1, 2, 3, 4])]

    def nopeus(self):
        nopeus = gauss(0, 1.5)
        nopeus += -0.25 if nopeus < 0 else 0.25
        return nopeus

    def pyoriminen(self):
        pyoriminen = gauss(0, 1)
        pyoriminen += -0.15 if pyoriminen < 0 else 0.15
        return pyoriminen

    def ominaisuudet(self, kokoluokka):
        d = {}
        d['sivu'] = {1: 50, 2: 80, 3: 110, 4: 150, 5: 200}[kokoluokka]
        d['kulmia'] = choice([5, 6, 7, 8, 9][:kokoluokka])
        d['väri'] = choice(['DIMGREY', 'BURLYWOOD', 'LIGHTGRAY', 'DARKGREY', 'BLACK'])
        d['kulman_muutos'] = randint(10, 170)
        d['paikka'] = self.paikka()
        d['nopeus'] = self.nopeus()
        d['pyöriminen'] = self.pyoriminen()
        d['hp'] = {1: 2, 2: 2, 3: 4, 4: 4, 5: 6}[kokoluokka]
        d['ru'] = int(abs(gauss(75, 10)) * kokoluokka * 10)
        return d

    def luo_asteroidi(self, indeksi):
        d = self.ominaisuudet(self.kokoluokka())
        AsteroidinKuvat(indeksi, d['sivu'], d['kulmia'], d['väri'])
        ku = image.load(Globaali.POLKU + f'/visual/resurssit/asteroidien_kuvat/{indeksi}_asteroidi.png')
        si = image.load(Globaali.POLKU + f'/visual/resurssit/asteroidien_kuvat/{indeksi}_sirpaleet.png')
        su = image.load(Globaali.POLKU + f'/visual/resurssit/asteroidien_kuvat/{indeksi}_sula.png')
        return Asteroidi(ku, d['kulman_muutos'], d['paikka'], d['nopeus'], d['pyöriminen'], si, su, d['hp'], d['ru'])

    def luo_asteroidit(self):
        return [self.luo_asteroidi(i) for i in range(self.maara)]
