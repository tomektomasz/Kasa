from PyQt5 import QtWidgets , uic
from PyQt5.QtWidgets import *
import Kasa_pkp

def przycisk():

    if okno.rodzaj_zwykly.isChecked() == True:
        trasa=Kasa_pkp.Pociag(okno.miasto_z.currentText(),okno.miasto_cel.currentText())
    elif okno.rodzaj_posp.isChecked() == True:
        trasa = Kasa_pkp.Pospieszny(okno.miasto_z.currentText(), okno.miasto_cel.currentText())
    else:
        trasa = Kasa_pkp.Expres(okno.miasto_z.currentText(), okno.miasto_cel.currentText())
    ile_1=int(okno.ile_junior.text())
    ile_2=int(okno.ile_normal.text())
    ile_3=int(okno.ile_senior.text())

    bilet = Kasa_pkp.Bilet(trasa.oblicz_cene_1(), ile_1, ile_2, ile_3)

    #print(bilet)
    okno.bilet_wynik.setText("Bilet nr : {}  Wystawiony dnia : {} \n \n".format(bilet.licznik,bilet.data_wystawienia)+
                         "Trasa z miasta: {} - do miasta: {} \n".format(trasa.miasto_od,trasa.miasto_do)+
                         "Odległość : {} km \n".format(trasa.oblicz_dystans())+
                         "Opłata za {} juniorów : {} zł \n".format(bilet.ile_junior,bilet.cena_junior())+
                         "Opłata za {} bez ulgi : {} zł \n".format(bilet.ile_osob,bilet.cena_osob())+
                         "Opłata za {} seniorów : {} zł \n".format(bilet.ile_senior,bilet.cena_senior()))
    okno.suma_zl.setText("RAZEM : {} zł".format(bilet.cena()))

#---------PROGRAM-----------------------

app=QtWidgets.QApplication([])

try:
    Kasa_pkp.wczytanie_pliku("miasta.txt")
    okno = uic.loadUi("Kasa_okno.ui")

    for item in Kasa_pkp.spis_Miast :
        okno.miasto_z.addItem(item["nazwa"])
        okno.miasto_cel.addItem(item["nazwa"])
    okno.ile_junior.setText("0")
    okno.ile_normal.setText("0")
    okno.ile_senior.setText("0")

    okno.pushButton.clicked.connect(przycisk)
    okno.show()
    app.exec()

except Kasa_pkp.WyjatekException :
    print("Program zakonczony")
    QMessageBox.information(None, "Kasa PKP","Nie znaleziono pliku ze spisem miast")



