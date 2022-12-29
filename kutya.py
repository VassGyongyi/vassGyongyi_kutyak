import random
class Kutya:
    def __init__(self, nev, nem, fajta, marmagassag, suly):
        self.__nev = nev
        self.nem = nem
        self.fajta = fajta
        self.marmagassag = marmagassag
        self.suly = suly


    def __str__(self):
      return f"{self.nev}:{self.nem},{self.fajta},{self.marmagassag},{self.suly}"

    def get_nev(self):
        return self.__nev

    def set_nev(self, adat):
        return self.__nev

    def tevekenyseg(self):
        tev_list =["ugat", "alszik", "játszik"]
        tev = random.choice(tev_list)
        return tev

