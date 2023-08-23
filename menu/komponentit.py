from harvesting_asteroids.globaali import Globaali
from abc import ABC
from tkinter import Tk, Listbox, Scrollbar, Frame, Button, Entry, Label, SUNKEN


class Komponentit(ABC):

    def __init__(self, statistiikka):
        self.statistiikka = statistiikka
        self.ikkuna = Tk()
        self.koko = None
        self.suhde = None
        self.fontit = None
        self.kehykset = None
        self.lista = None
        self.pelaajien_listaindeksit = None
        self.luo_uusi_pelaaja = None
        self.pelaajan_nimi = None
        self.varattu = False

    def set_lista(self):
        leveys = int(59 + self.suhde // 1)
        self.lista = Listbox(master=self.ikkuna, bg='BLACK', fg='CORAL', width=leveys, height=7, bd=self.kehykset[0],
                             font=self.fontit[3], selectmode='SINGLE', relief=SUNKEN, selectforeground='RED',
                             selectbackground='BLACK', activestyle='none')
        self.lista.place(x=self.koko[0] / 7 - self.kehykset[0], y=self.koko[1] / 2)
        self.paivita_lista()

    def paivita_lista(self):
        def valittu_pelaaja(event):
            Globaali.PELAAJA = self.pelaajien_listaindeksit[event.widget.curselection()[0]]

        Globaali.PELAAJA = None
        self.lista.bind(sequence='<<ListboxSelect>>', func=valittu_pelaaja)
        self.set_pelaajien_listaindeksit()
        for k, v in self.pelaajien_listaindeksit.items():
            self.lista.insert(k + 1, self.statistiikka.pelaajat[v])

    def set_pelaajien_listaindeksit(self):
        pelaajat = [p for p in self.statistiikka.pelaajat]
        self.pelaajien_listaindeksit = {i: pelaajat[i] for i in range(len(pelaajat))}

    def set_uusi_pelaaja(self):
        def uusi_pelaaja():
            if not self.varattu:
                self.varattu = True
                self.lista.bindtags('all')
                self.set_luo_uusi_pelaaja()

        lisaa_pelaaja = Button(master=self.ikkuna, text='UUSI PELAAJA', width=15, height=1, bd=self.kehykset[1],
                               bg='GREY', fg='BLACK', font=self.fontit[4], command=uusi_pelaaja)
        lisaa_pelaaja.place(x=self.koko[0] / 6 - self.kehykset[1], y=self.koko[1] - self.koko[1] / 8)

    def set_luo_uusi_pelaaja(self):
        self.luo_uusi_pelaaja = Frame(master=self.ikkuna, width=self.koko[0] / 3, height=self.koko[1] / 3,
                                      bd=self.kehykset[1], bg='GREY', relief=SUNKEN)
        self.set_pelaajan_nimi()
        self.set_lisaa_pelaaja()
        self.set_poistu()
        self.luo_uusi_pelaaja.pack()
        self.luo_uusi_pelaaja.place(x=self.koko[0] / 3, y=self.koko[1] / 3)

    def set_pelaajan_nimi(self):
        leveys = int(9 - self.suhde // 1)
        self.pelaajan_nimi = Entry(master=self.luo_uusi_pelaaja, width=leveys, bd=self.kehykset[2], bg='DARKGREY',
                                   fg='BLACK', font=self.fontit[2], relief=SUNKEN)
        self.pelaajan_nimi.place(x=self.koko[0] / 8, y=self.koko[1] / 12)

    def set_lisaa_pelaaja(self):
        def lisaa():
            nimi = self.pelaajan_nimi.get().capitalize()
            if len(nimi) > 0 and nimi not in self.statistiikka.pelaajat:
                self.varattu = False
                self.statistiikka.uusi_pelaaja(nimi)
                self.statistiikka.tallenna_pelaajat()
                self.luo_uusi_pelaaja.destroy()
                self.set_lista()

        lisaa_pelaaja = Button(master=self.luo_uusi_pelaaja, text='LISÄÄ', width=6, height=1, bd=self.kehykset[2],
                               bg='DARKGREY', fg='BLACK', font=self.fontit[2], command=lisaa)
        lisaa_pelaaja.place(x=self.koko[0] / 16 - self.kehykset[2], y=self.koko[1] / 5)

    def set_poistu(self):
        def poistu():
            self.varattu = False
            self.luo_uusi_pelaaja.destroy()
            self.paivita_lista()
            self.set_lista()

        poistu = Button(master=self.luo_uusi_pelaaja, text='POISTU', width=7, height=1, bd=self.kehykset[2],
                        bg='DARKGREY', fg='BLACK', font=self.fontit[2], command=poistu)
        poistu.place(x=self.koko[0] / 5 - self.kehykset[2], y=self.koko[1] / 5)

    def set_pelaa(self):
        def poistu_valikosta():
            if not self.varattu:
                if Globaali.PELAAJA is None:
                    self.varattu = True
                    self.lista.bindtags('all')
                    self.set_herja()
                else:
                    self.ikkuna.destroy()

        pelaa = Button(master=self.ikkuna, text='PELAA', width=6, height=1, bd=self.kehykset[1], bg='GREY',
                       fg='BLACK', font=self.fontit[4], command=poistu_valikosta)
        pelaa.place(x=self.koko[0] / 2 - 25 * self.suhde, y=self.koko[1] - self.koko[1] / 8)

    def set_herja(self):
        def poista_herja():
            self.varattu = False
            herja.destroy()
            self.set_lista()

        herja = Frame(master=self.ikkuna, width=self.koko[0] / 3, height=self.koko[1] / 6, bd=self.kehykset[1],
                      bg='GREY', relief=SUNKEN)
        herjaus = 'Lisää pelaaja!' if not self.statistiikka.pelaajat else 'Valitse pelaaja!'
        Label(master=herja, text=herjaus, width=18, bg='GREY', fg='BLACK',
              font=self.fontit[2]).place(x=self.koko[0] / 11, y=self.koko[1] / 16)
        herja.pack()
        herja.place(x=self.koko[0] / 3 - self.kehykset[1], y=self.koko[1] / 9 * 4)
        herja.after(2000, poista_herja)

    def set_lopeta(self):
        def lopeta():
            if not self.varattu:
                self.ikkuna.destroy()
                Globaali.LOPETUS = True

        lopeta = Button(master=self.ikkuna, text='LOPETA', width=7, height=1, bd=self.kehykset[1], bg='GREY',
                        fg='BLACK', font=self.fontit[4], command=lopeta)
        lopeta.place(x=self.koko[0] - self.koko[0] / 3 + 90 * self.suhde, y=self.koko[1] - self.koko[1] / 8)
