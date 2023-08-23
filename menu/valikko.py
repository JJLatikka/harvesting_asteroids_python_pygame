from harvesting_asteroids.globaali import Globaali
from harvesting_asteroids.menu.komponentit import Komponentit
from tkinter import Label, Text, font


class Valikko(Komponentit):

    def __init__(self, statistiikka):
        Komponentit.__init__(self, statistiikka)
        self.asetukset()
        Globaali.KOKO = self.koko
        Globaali.SUHDE = self.suhde

    def asetukset(self):
        self.ikkuna.attributes('-fullscreen', True)
        self.ikkuna.configure(bg='BLACK')
        self.set_koko_ja_suhde()
        self.set_fontit_ja_kehykset()
        self.set_otsikko()
        self.set_tarina()
        self.set_lista()
        self.set_uusi_pelaaja()
        self.set_pelaa()
        self.set_lopeta()

    def set_koko_ja_suhde(self):
        self.koko = self.ikkuna.winfo_screenwidth(), self.ikkuna.winfo_screenheight()
        self.suhde = self.koko[0] / 1920

    def set_fontit_ja_kehykset(self):
        koot = list(map(lambda k: int(k * self.suhde), [40, 20, 30]))
        self.fontit = [font.Font(size=koot[0], family='MathJax_Caligraphic'),
                       font.Font(size=koot[1], family='Chilanka'),
                       font.Font(size=koot[1], family='Arial'),
                       font.Font(size=koot[2], family='Chilanka'),
                       font.Font(size=koot[2], family='MathJax_Caligraphic')]
        self.kehykset = [15 * self.suhde, 7.5 * self.suhde, 3.75 * self.suhde]

    def set_otsikko(self):
        otsikko = Label(master=self.ikkuna, text='HARVESTING ASTEROIDS', width=32,
                        bg='BLACK', fg='YELLOW', font=self.fontit[0])
        otsikko.place(x=self.koko[0] / 4, y=self.koko[1] / 20)

    def set_tarina(self):
        teksti = [f"Olet 'asteroidimainari', ja työskentelet Asteroid-Mining Corporationin (AMC) palveluksessa.\n",
                  f"Tehtäväsi on kauko-ohjata 'suhteellisen turvallisesta' avaruustukikohdasta käsin\n",
                  f"huippukehittynyttä ja -kallista robottidrone-harvesteria vaarallisella Tannhauser-gate:n\n",
                  f"asteroidivyöhykkeellä. Aluksesi on varustettu tulinopeudeltaan hitaanlaisilla, mutta kuitenkin\n",
                  f"melko tehokkailla erikois-Z-beam-plasma-tuhosäde-tykeillä. - Vaikka et itse olekkaan\n",
                  f"välittömässä hengenvaarassa, yritä kuitenkin väistellä asteroideja parhaasi mukaan,\n",
                  f"koska hyvä 'mainari' kerää enemmän resursseja kuin mitä hänen ohjauksessaan\n",
                  f"tuhoutuneiden dronejen rakentamiseen on käytetty. Liian alhainen hyötysuhde vähentää\n",
                  f"bonuksia!!! - Pitäähän AMC:n kuitenkin maksaa ne 'tellit' ja 'lellit' ja 'sotut' ja 'votut'..."]
        tarina = Text(master=self.ikkuna, bg='BLACK', fg='YELLOW', width=80, height=9,
                      font=self.fontit[1], borderwidth=0, highlightthickness=0)
        tarina.place(x=self.koko[0] / 5, y=self.koko[1] / 7)
        for i in range(len(teksti)):
            tarina.insert(f'{i + 1}.0', teksti[i])
