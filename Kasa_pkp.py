from datetime import date
from math import sqrt


spis_Miast = []

class Pociag :
    def __init__(self, miasto_od, miasto_do):
        self.miasto_od=miasto_od
        self.miasto_do=miasto_do
       # self.spis_Miast=spis

    def oblicz_dystans(self):
        for item in spis_Miast :
            if item["nazwa"]==self.miasto_od :
                self.x_od=item["x"]
                self.y_od=item["y"]
        for item in spis_Miast:
            if item["nazwa"] == self.miasto_do:
                self.x_do = item["x"]
                self.y_do = item["y"]
        return(round(sqrt((self.x_do-self.x_od)**2+(self.y_do-self.y_od)**2),2))

    def oblicz_cene_1(self):
        return round(self.oblicz_dystans()*0.2+20,2)

    def __str__(self):
        return ("Miasto_od:  {}  -x={}  -y={}".format(self.miasto_od,self.x_od,self.y_od)+'\n'
                "Miasto_do:  "+self.miasto_do+"  -x={}   -y={}".format(self.x_do,self.y_do))

class Pospieszny(Pociag) :
    def __init__(self, miasto_od, miasto_do):
        super().__init__(miasto_od=miasto_od,miasto_do=miasto_do)

    def oblicz_cene_1(self):
        return (super().oblicz_cene_1()*1.5)

class Expres(Pociag) :
    def __init__(self, miasto_od, miasto_do):
        super(Expres, self).__init__(miasto_od=miasto_od, miasto_do=miasto_do)

    def oblicz_cene_1(self):
        return (Pociag.oblicz_cene_1(self)*2)

class Bilet():
    licznik=1000
    def __init__(self,cena_1=0,ile_junior=0,ile_osob=0,ile_senior=0):
        self.cena_1=cena_1
        self.ile_junior=ile_junior
        self.ile_osob=ile_osob
        self.ile_senior=ile_senior
        self.data_wystawienia=date.today()
        self.zwieksz_licznik()

    def cena_senior(self):
        if self.ile_senior !=0 :
            return round(self.cena_1*self.ile_senior*0.7)
        else:
            return 0

    def cena_junior(self):
        if self.ile_junior != 0 :
            return round(self.cena_1*self.ile_junior*0.5)
        else:
            return 0

    def cena_osob(self):
        if self.ile_osob != 0 :
            return round(self.cena_1*self.ile_osob,2)
        else:
            return 0

    def cena(self):
        return round(self.cena_junior()+self.cena_osob()+self.cena_senior(),2)

    def ile_razem(self):
        return self.ile_junior+self.ile_osob+self.ile_senior

    def zwieksz_licznik(self):
        Bilet.licznik+=1

    def __str__(self):
        return ("Bilet numer: {}  wystawiony dnia: {} \n".format(self.licznik,self.data_wystawienia)+
                'Zaplata za {} juniorow     : {} zł \n'.format(self.ile_junior,self.cena_junior())+
                'Zaplata bez ulg za {} osob : {} zł \n'.format(self.ile_osob,self.cena_osob())+
                'Zaplata za {} seniorow     : {} zł \n'.format(self.ile_senior,self.cena_senior())+
                'RAZEM                     : {} zł'.format(self.cena()))

class WyjatekException(Exception):
    pass

def wczytanie_pliku(nazwa_pliku):
    try:
        plik=open(nazwa_pliku,"r")
        linie=plik.readlines()
        for item in linie :
            spis_Miast.append({"nazwa":item.split()[0],
                           "x":int(item.split()[1]),
                           "y":int(item.split()[2])})
        plik.close()
    except FileNotFoundError :
        print("Nie znaleziono pliku z miastami")
        raise WyjatekException


