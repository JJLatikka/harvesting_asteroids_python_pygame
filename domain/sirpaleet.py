from harvesting_asteroids.domain.objekti import Objekti


class Sirpaleet(Objekti):

    def __init__(self, kuva, kulman_muutos, paikka, nopeus):
        Objekti.__init__(self, kuva, kulman_muutos, paikka, nopeus)

    def update(self, *args, **kwargs) -> None:
        pass
