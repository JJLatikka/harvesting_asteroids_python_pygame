from harvesting_asteroids.globaali import Globaali
from harvesting_asteroids.visual.ammuksen_ja_sirpaleiden_piirto import AmmuksetJaSirpaleet
from PIL import Image, ImageDraw
from random import randint, gauss
from math import radians, sin, cos


class AsteroidinKuvat:

    def __init__(self, indeksi, sivu, kulmia, vari):
        self.sivu = sivu
        self.kulmia = kulmia
        self.vari = vari
        self.kulmio = self.kulmio()
        self.asteroidi = self.piirra(self.vari)
        self.sirpaleet = AmmuksetJaSirpaleet.piirra_sirpaleet(self.sivu, self.vari)
        self.sula = self.piirra('RED')
        self.asteroidi.save(Globaali.POLKU + f'/visual/resurssit/asteroidien_kuvat/{indeksi}_asteroidi.png')
        self.sirpaleet.save(Globaali.POLKU + f'/visual/resurssit/asteroidien_kuvat/{indeksi}_sirpaleet.png')
        self.sula.save(Globaali.POLKU + f'/visual/resurssit/asteroidien_kuvat/{indeksi}_sula.png')

    def kulmio(self):
        l = []
        sade = self.sivu / 2
        kulma = 360 / self.kulmia
        for k in range(self.kulmia):
            rad = radians(kulma * k)
            siirros = sin(rad) * sade, cos(rad) * sade
            ex = gauss(sade / 20, 1) * randint(-1, 1)
            ey = gauss(sade / 20, 1) * randint(-1, 1)
            l.append((sade - siirros[0] - ex, sade - siirros[1] - ey))
        return l

    def piirra(self, vari):
        asteroidi = Image.new('RGBA', (self.sivu, self.sivu))
        ImageDraw.Draw(asteroidi, 'RGBA').polygon(self.kulmio, vari)
        return asteroidi
