from harvesting_asteroids.globaali import Globaali
from harvesting_asteroids.logic.peli import HarvestingAsteroids
from harvesting_asteroids.menu.tulokset import Statistiikka
from harvesting_asteroids.menu.valikko import Valikko
from os import getcwd
from pygame import mixer, init, mouse, quit, display


class Paaohjelma:

    def __init__(self):
        Globaali.POLKU = getcwd() + '/harvesting_asteroids'
        Globaali.LOPETUS = False
        self.statistiikka = Statistiikka()

    def suorita(self):
        while not Globaali.LOPETUS:
            Valikko(self.statistiikka).ikkuna.mainloop()
            if not Globaali.LOPETUS:
                HarvestingAsteroids(self.statistiikka).pelaa()


mixer.pre_init(frequency=44100, size=-16, channels=6, buffer=4096)
init()
display.init()
mixer.init(frequency=44100, size=-16, channels=6, buffer=4096, allowedchanges=0)
mixer.set_num_channels(11)
mouse.set_visible(False)
Paaohjelma().suorita()
quit()
exit()
