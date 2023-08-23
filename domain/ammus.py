from harvesting_asteroids.domain.objekti import Objekti


class Ammus(Objekti):

    def __init__(self, kuva, kulman_muutos, paikka, nopeus):
        Objekti.__init__(self, kuva, kulman_muutos, paikka, nopeus)
        self.kaanny()
        self.aseta_suunta()

    def update(self, *args, **kwargs) -> None:
        self.liiku()
        if self.ylitys():
            self.kill()
