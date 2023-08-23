class Pelaaja:

    def __init__(self, nimi, koko_saalis: int = 0, bonukset: int = 0):
        self.nimi = nimi
        self.koko_saalis = koko_saalis
        self.bonukset = bonukset

    def paivita_statistiikka(self, saalis, bonus):
        self.koko_saalis += saalis
        self.bonukset += bonus

    def to_d(self):
        return {'nimi': self.nimi, 'koko_saalis': self.koko_saalis, 'bonukset': self.bonukset}

    def __str__(self):
        return f'{self.nimi:<10}{"kerätyt resurssit:":>24}{self.koko_saalis:>15}' \
               f'{"bonukset:":>15}{self.bonukset:>6}'
