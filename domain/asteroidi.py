from harvesting_asteroids.domain.objekti import Objekti


class Asteroidi(Objekti):

    def __init__(self, kuva, kulman_muutos, paikka, nopeus, pyoriminen, sirpaleet, sula, hp, ru):
        Objekti.__init__(self, kuva, kulman_muutos, paikka, nopeus)
        self.pyoriminen = pyoriminen
        self.sirpaleet = sirpaleet
        self.sula = sula
        self.hp_taydet = hp
        self.hp = hp
        self.ru = ru
        self.kuuma = False
        self.sulamispiste = hp // 2
        self.kaanny()
        self.aseta_suunta()

    def kuumene(self):
        self.kuuma = True
        paikka = self.paikka
        self.image = self.sula
        self.muunnettava = self.image
        self.rect = self.image.get_rect()
        self.rect.center = paikka

    def jaahdy(self):
        self.kuuma = False
        paikka = self.paikka
        self.hp = self.hp_taydet
        self.image = self.kuva
        self.muunnettava = self.image
        self.rect = self.image.get_rect()
        self.rect.center = paikka

    def pyori(self):
        self.kulman_muutos = self.pyoriminen
        self.kaanny()

    def update(self, *args, **kwargs) -> None:
        if not self.kuuma and self.hp <= self.sulamispiste:
            self.kuumene()
        if self.ylitys():
            self.jaahdy()
        self.siirra()
        self.pyori()
        self.liiku()
