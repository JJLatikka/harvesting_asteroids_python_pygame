from harvesting_asteroids.globaali import Globaali
from PIL import Image, ImageDraw


class AluksenKuva:

    def __init__(self):
        self.alus = self.piirra()
        self.alus.save(Globaali.POLKU + '/visual/resurssit/alus.png')

    def runko(self):
        return [(28, 0), (35, 53), (40, 60), (50, 100), (45, 100), (35, 85),
                (15, 85), (5, 100), (0, 100), (10, 60), (15, 53), (22, 0)]

    def viivat(self):
        return [[(27, 4), (34, 54)], [(34, 54), (39, 61)], [(39, 61), (48, 98)],
                [(42, 92), (36, 83)], [(36, 83), (14, 83)], [(14, 83), (8, 92)],
                [(22, 4), (15, 54)], [(15, 54), (10, 61)], [(10, 61), (1, 98)]]

    def silmat(self):
        return [[(20, 62), (30, 62)], [(20, 66), (30, 66)], [(20, 70), (30, 70)], [(20, 74), (30, 74)]]

    def karjet(self):
        return [[(22, 0), (28, 0), (30, 10), (20, 10)], [(0, 100), (2, 90), (12, 90), (5, 100)],
                [(50, 100), (48, 90), (38, 90), (45, 100)]]

    def moottori(self):
        return [(17, 89), (17, 86), (33, 86), (33, 89)]

    def piirra(self):
        alus = Image.new('RGBA', (51, 101))
        piirto = ImageDraw.Draw(alus, 'RGBA')
        piirto.polygon(self.runko(), 'GREY')
        piirto.polygon(self.moottori(), 'YELLOW')
        for l in self.viivat():
            piirto.line(l, 'CORAL', width=2)
        for l in self.silmat():
            piirto.line(l, 'RED', width=2)
        for l in self.karjet():
            piirto.polygon(l, 'BLACK')
        return alus
