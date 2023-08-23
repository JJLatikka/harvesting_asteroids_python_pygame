from harvesting_asteroids.globaali import Globaali
from PIL import Image, ImageDraw


class Taustakuva:

    def __init__(self):
        self.alkuperainen = Image.open(Globaali.POLKU + '/visual/resurssit/nebula.jpg')
        self.alkuperaisen_koko = self.alkuperainen.size
        self.pixelit = self.alkuperainen.load()
        self.rajatun_aloituskohta = self.rajatun_aloituskohta()
        self.rajattu = self.rajaa()
        self.rajattu.save(Globaali.POLKU + '/visual/resurssit/taustakuva.png')

    def rajatun_aloituskohta(self):
        x = (self.alkuperaisen_koko[0] - Globaali.KOKO[0]) // 2
        y = (self.alkuperaisen_koko[1] - Globaali.KOKO[1]) // 2
        return x, y

    def rajaa(self):
        rajattu = Image.new('RGB', Globaali.KOKO)
        for x in range(Globaali.KOKO[0]):
            for y in range(Globaali.KOKO[1]):
                r = self.rajatun_aloituskohta[0] + x, self.rajatun_aloituskohta[1] + y
                rajattu.putpixel((x, y), self.pixelit[r[0], r[1]])
        return rajattu
