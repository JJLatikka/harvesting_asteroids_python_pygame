from harvesting_asteroids.globaali import Globaali
from harvesting_asteroids.logic.pelitapahtumat import Pelitapahtumat
from harvesting_asteroids.visual.taustakuvan_piirto import Taustakuva
from harvesting_asteroids.visual.ammuksen_ja_sirpaleiden_piirto import AmmuksetJaSirpaleet
from pygame import image


class HarvestingAsteroids:

    def __init__(self, statistiikka):
        self.taustakuva = self.lataa_taustakuva(Globaali.POLKU + '/visual/resurssit/taustakuva.png')
        self.aluksen_kuva = image.load(Globaali.POLKU + '/visual/resurssit/alus.png')
        self.ammus_l_kuva = image.load(Globaali.POLKU + '/visual/resurssit/ammus_l.png')
        self.ammus_r_kuva = image.load(Globaali.POLKU + '/visual/resurssit/ammus_r.png')
        self.statistiikka = statistiikka

    def lataa_taustakuva(self, polku):
        if not self.nayton_koko() == Globaali.KOKO:
            Taustakuva()
            self.tallenna_nayton_koko()
            return image.load(polku)
        else:
            return image.load(polku)

    def nayton_koko(self):
        with open(Globaali.POLKU + '/visual/nayton_koko.txt') as t:
            koko = t.readline().split(';')
            return int(koko[0]), int(koko[1])

    def tallenna_nayton_koko(self):
        with open(Globaali.POLKU + '/visual/nayton_koko.txt', 'w') as t:
            t.write(f'{Globaali.KOKO[0]};{Globaali.KOKO[1]}')

    def pelaa(self):
        aluksen_sirpaleet = self.lataa_aluksen_sirpaleet(Globaali.POLKU + '/visual/resurssit/aluksen_sirpaleet.png')
        tulos = Pelitapahtumat(self.taustakuva, self.aluksen_kuva, aluksen_sirpaleet,
                               self.ammus_l_kuva, self.ammus_r_kuva).tapahtumat(True)
        self.statistiikka.paivita_ja_tallenna_pelaajat(Globaali.PELAAJA, tulos)

    def lataa_aluksen_sirpaleet(self, polku):
        AmmuksetJaSirpaleet().piirra_sirpaleet(100, 'YELLOW').save(polku)
        return image.load(polku)
