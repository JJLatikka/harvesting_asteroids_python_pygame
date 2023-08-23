from PIL import Image, ImageDraw
from math import radians, sin, cos
from random import randint, gauss


class AmmuksetJaSirpaleet:

    @classmethod
    def piirra_sirpaleet(cls, sivu, vari):
        sirpaleet = Image.new('RGBA', (sivu * 2, sivu * 2))
        piirto = ImageDraw.Draw(sirpaleet, 'RGBA')
        for n in range(sivu * 50):
            rad = radians(randint(0, 360))
            energia = gauss(1, sivu / 2)
            xy = sivu - cos(rad) * energia, sivu - sin(rad) * energia
            piirto.point(xy, fill=vari)
        return sirpaleet

    @classmethod
    def piirra_ammukset(cls):
        ammukset = Image.new('RGBA', (51, 101)), Image.new('RGBA', (51, 101))
        ImageDraw.Draw(ammukset[0], 'RGBA').line([(12, 50), (12, 40)], 'GREENYELLOW', width=2)
        ImageDraw.Draw(ammukset[1], 'RGBA').line([(39, 50), (39, 40)], 'GREENYELLOW', width=2)
        return ammukset
