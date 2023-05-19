
import arsa
import daire

while True:
    tur_secimi = input("Arsa fiyatı hesaplamak için 'a' daire fiyatı hesaplamak için 'd' tuşunu seçiniz! \n")
    while tur_secimi !="a" and tur_secimi !="d":
        tur_secimi = input("'a' ya da 'd' seçebilirsiniz!\n")
        denetleme = input("tekrar hesaplamak için e/E,çıkmak için h/H seçiniz \n")
        while denetleme != "e" and denetleme != "E" and denetleme != "h" and denetleme != "H":
            denetleme = input("e/E ya da h/H seçiniz!!\n")