from harvesting_asteroids.globaali import Globaali
from harvesting_asteroids.audio.aanet import Aanet
from harvesting_asteroids.domain.alus import Alus
from harvesting_asteroids.domain.ammus import Ammus
from harvesting_asteroids.domain.sirpaleet import Sirpaleet
from harvesting_asteroids.domain.satunnaisuus import Asteroidigeneraattori
from pygame import display, font, FULLSCREEN, NOFRAME, sprite, time, event
from time import sleep


class Pelitapahtumat:

    def __init__(self, taustakuva, aluksen_kuva, aluksen_sirpaleet, ammus_l_kuva, ammus_r_kuva):
        self.aanet = Aanet()
        self.saalis = 0
        self.fontti = font.SysFont('Noto Sans Mono', 25)
        self.saalis_kohta = 25, Globaali.KOKO[1] - 50
        self.keskikohta = Globaali.KOKO[0] / 2, Globaali.KOKO[1] / 2
        self.naytto = display.set_mode(Globaali.KOKO, FULLSCREEN | NOFRAME)
        self.taustakuva = taustakuva.convert()
        self.aluksen_kuva = aluksen_kuva.convert_alpha()
        self.aluksen_sirpaleet = aluksen_sirpaleet.convert_alpha()
        self.ammus_l_kuva = ammus_l_kuva.convert_alpha()
        self.ammus_r_kuva = ammus_r_kuva.convert_alpha()
        self.alus = Alus(self.aluksen_kuva, 0, self.keskikohta, 0, self.aluksen_sirpaleet)
        self.alusryhma = sprite.Group(self.alus)
        self.asteroidiryhma = sprite.Group()
        self.ammusryhma = sprite.Group()
        self.sirpaleryhma = sprite.Group()
        self.ryhmat = [self.alusryhma, self.asteroidiryhma, self.ammusryhma, self.sirpaleryhma]
        self.asteroidit = Asteroidigeneraattori(50).asteroidit
        self.kello = time.Clock()
        self.nopeus = int(60 * Globaali.SUHDE)

    def tapahtumat(self, kaynnissa):
        self.aanet.taustamusiikki()

        while kaynnissa:
            self.ohjaus()
            self.tulta()
            self.ammusten_osumat()
            self.lisaa_asteroideja()
            self.imuri()
            self.aluksen_tormays()

            self.naytto.blit(self.taustakuva, (0, 0))
            self.naytto.blit(self.fontti.render(
                f"RU's: {self.saalis}", True, 'BROWN'), self.saalis_kohta)

            for ryhma in self.ryhmat:
                if ryhma:
                    ryhma.update()
                    ryhma.draw(self.naytto)

            display.flip()
            self.kello.tick(self.nopeus)
            elossa, kiintio_ei_taynna = self.alus.alive(), self.saalis < 50000
            kaynnissa = elossa and kiintio_ei_taynna
            event.pump()

        return self.vuoro_ohi(elossa)

    def ohjaus(self):
        self.aluksen_aanet()
        for e in event.get(pump=False):
            self.alus.ohjaus(e)

    def aluksen_aanet(self):
        if self.alus.nopeus > 0:
            self.aanet.eteenpain()
        elif self.alus.nopeus < 0:
            self.aanet.taaksepain()
        elif self.alus.nopeus == 0:
            self.aanet.pysahdy()

    def tulta(self):
        if self.alus.tulta and len(self.ammusryhma) < 6:
            self.ammusryhma.add(Ammus(self.ammus_l_kuva, self.alus.kulma, self.alus.paikka, 7.5))
            self.ammusryhma.add(Ammus(self.ammus_r_kuva, self.alus.kulma, self.alus.paikka, 7.5))
            self.aanet.tulta()
            self.alus.tulta = False

    def ammusten_osumat(self):
        if self.ammusryhma:
            tormaykset = sprite.groupcollide(
                self.ammusryhma, self.asteroidiryhma, True, False, sprite.collide_mask)
            for v in tormaykset.values():
                for a in v:
                    a.hp -= 1
            for a in self.asteroidiryhma:
                if a.hp <= 0:
                    self.sirpaleryhma.add(Sirpaleet(a.sirpaleet, 0, a.paikka, 0))
                    self.saalis += a.ru
                    a.kill()
                    self.aanet.asteroidin_rajahdys()

    def lisaa_asteroideja(self):
        if len(self.asteroidiryhma) < 15:
            self.asteroidiryhma.add(self.asteroidit.pop())

    def imuri(self):
        if len(self.sirpaleryhma) > 5:
            [s for s in self.sirpaleryhma][0].kill()

    def aluksen_tormays(self):
        if not self.alus.suojassa():
            tormays = sprite.spritecollideany(self.alus, self.asteroidiryhma, sprite.collide_mask)
            if tormays:
                self.sirpaleryhma.add(Sirpaleet(self.alus.sirpaleet, 0, self.alus.paikka, 0))
                self.alus.kill()

    def vuoro_ohi(self, elossa):
        if elossa:
            self.aanet.loppufanfaari()
        else:
            self.aanet.aluksen_rajahdys()
        bonus = 1 if elossa else 0
        sleep(10)
        self.poistous()
        return self.saalis, bonus

    def poistous(self):
        for r in self.ryhmat:
            if r:
                r.empty()
        event.clear()
        display.flip()
        display.toggle_fullscreen()
