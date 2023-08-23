from harvesting_asteroids.globaali import Globaali
from pygame import mixer


class Aanet:

    def __init__(self):
        mixer.music.load(Globaali.POLKU + '/audio/resurssit/Battlestar.ogg')
        self.fwd = mixer.Channel(0)
        self.thrusters_fwd = mixer.Sound(Globaali.POLKU + '/audio/resurssit/Thrusters.ogg')
        self.rwd = mixer.Channel(1)
        self.thrusters_rwd = mixer.Sound(Globaali.POLKU + '/audio/resurssit/Thrusters.ogg')
        self.laaserit1 = mixer.Channel(2)
        self.laaserit2 = mixer.Channel(3)
        self.laaserit3 = mixer.Channel(4)
        self.lasers = mixer.Sound(Globaali.POLKU + '/audio/resurssit/Lasers.ogg')
        self.rajahdys1 = mixer.Channel(5)
        self.rajahdys2 = mixer.Channel(6)
        self.rajahdys3 = mixer.Channel(7)
        self.explosion = mixer.Sound(Globaali.POLKU + '/audio/resurssit/Explosion.ogg')
        self.ydinrajahdys = mixer.Channel(8)
        self.nuke = mixer.Sound(Globaali.POLKU + '/audio/resurssit/NuclearBlast.ogg')
        self.fanfaari = mixer.Channel(9)
        self.galactica = mixer.Sound(Globaali.POLKU + '/audio/resurssit/Galactica.ogg')
        self.kanavien_asetukset()

    def kanavien_asetukset(self):
        mixer.music.set_volume(1)
        self.fwd.set_volume(0.7)
        self.rwd.set_volume(0.5)
        self.laaserit1.set_volume(0.3)
        self.laaserit2.set_volume(0.3)
        self.laaserit3.set_volume(0.3)
        self.rajahdys1.set_volume(0.3)
        self.rajahdys2.set_volume(0.3)
        self.rajahdys3.set_volume(0.3)
        self.ydinrajahdys.set_volume(0.5)
        self.fanfaari.set_volume(1)

    def taustamusiikki(self):
        mixer.music.play(-1)

    def eteenpain(self):
        self.rwd.stop()
        if not self.fwd.get_busy():
            self.fwd.play(self.thrusters_fwd, fade_ms=500)

    def taaksepain(self):
        self.fwd.stop()
        if not self.rwd.get_busy():
            self.rwd.play(self.thrusters_rwd, fade_ms=500)

    def pysahdy(self):
        self.fwd.stop()
        self.rwd.stop()

    def tulta(self):
        if not self.laaserit1.get_busy():
            self.laaserit1.play(self.lasers, maxtime=1000, fade_ms=100)
        elif not self.laaserit2.get_busy():
            self.laaserit2.play(self.lasers, maxtime=1000, fade_ms=100)
        elif not self.laaserit3.get_busy():
            self.laaserit3.play(self.lasers, maxtime=1000, fade_ms=100)

    def asteroidin_rajahdys(self):
        if not self.rajahdys1.get_busy():
            self.rajahdys1.play(self.explosion, maxtime=2500, fade_ms=100)
        elif not self.rajahdys2.get_busy():
            self.rajahdys2.play(self.explosion, maxtime=2500, fade_ms=100)
        elif not self.rajahdys3.get_busy():
            self.rajahdys3.play(self.explosion, maxtime=2500, fade_ms=100)

    def aluksen_rajahdys(self):
        mixer.music.stop()
        self.pysahdy()
        self.ydinrajahdys.play(self.nuke, maxtime=10000, fade_ms=100)

    def loppufanfaari(self):
        mixer.music.stop()
        self.pysahdy()
        self.fanfaari.play(self.galactica)
