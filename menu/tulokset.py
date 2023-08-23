from harvesting_asteroids.globaali import Globaali
from harvesting_asteroids.domain.pelaaja import Pelaaja
from json import load, dumps


class Statistiikka:

    def __init__(self):
        self.pelaajat = self.get_pelaajat()

    def get_pelaajat(self):
        return self.set_pelaajat(self.lue_pelaajat())

    def lue_pelaajat(self):
        try:
            with open(Globaali.POLKU + '/menu/statistiikka.json', 'r') as t:
                return load(t)
        except FileNotFoundError:
            return []

    def set_pelaajat(self, tulokset):
        if tulokset:
            return {d['nimi']: Pelaaja(d['nimi'], d['koko_saalis'], d['bonukset']) for d in tulokset}
        else:
            return {}

    def uusi_pelaaja(self, nimi):
        self.pelaajat[nimi] = Pelaaja(nimi)

    def tallenna_pelaajat(self):
        with open(Globaali.POLKU + '/menu/statistiikka.json', 'w') as t:
            t.write(dumps(self.get_tallennettavat(), indent=4, ensure_ascii=False))

    def get_tallennettavat(self):
        return [p.to_d() for p in self.pelaajat.values()]

    def paivita_ja_tallenna_pelaajat(self, pelaaja, tulos):
        self.pelaajat[pelaaja].paivita_statistiikka(tulos[0], tulos[1])
        self.tallenna_pelaajat()
