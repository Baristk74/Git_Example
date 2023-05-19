
import arsa
import daire

while True:
    tur_secimi = input("Arsa fiyatı hesaplamak için 'a' daire fiyatı hesaplamak için 'd' tuşunu seçiniz! \n")
    while tur_secimi !="a" and tur_secimi !="d":
        tur_secimi = input("'a' ya da 'd' seçebilirsiniz!\n")
        if tur_secimi == "a":
            kat_sayi_secimi = int(input("sırasıyla deniz kenarı, şehir merkezi, kırsal için 1,2,3 seçiniz \n"))

            while kat_sayi_secimi != 1 and kat_sayi_secimi != 2 and kat_sayi_secimi != 3:
                kat_sayi_secimi = int(input("1,2,3 seçeneklerinden birini seçiniz!\n"))
            arsa.katsayi_secimi(kat_sayi_secimi)
            sekil_secimi = int(input("Arsa türünüzü belirtiniz dikdörtgen için 1, daire için 2 seçiniz \n"))

            while sekil_secimi != 1 and sekil_secimi != 2:
                sekil_secimi = int(input("1,2 seçeneklerinden birini seçiniz!"))

            if sekil_secimi == 1:
                kisa_kenar = int(input("Dikdörtgenin kısa kenarını metre cinsinden kenarını giriniz:\n"))
                uzun_kenar = int(input("Dikdörtgenin uzun kenarını metre cinsinden kenarını giriniz:\n"))
                arsa.dikdortgen(kisa_kenar, uzun_kenar)
                print("arsanın fiyatı {:0.2f} TL".format(arsa.arsanin_fiyati()))

            elif sekil_secimi == 2:
                yaricap = int(input("Dairenin yarıçapını metre cinsinden giriniz:\n"))
                arsa.daire(yaricap)
                print("Arsanın fiyatı {:0.2f} TL".format(arsa.arsanin_fiyati()))
        elif tur_secimi == "d":
            kat_sayi_secimi = int(input("sırasıyla ara kat, üst kat, zemin kat için 1,2,3 seçiniz\n"))

            while kat_sayi_secimi != 1 and kat_sayi_secimi != 2 and kat_sayi_secimi != 3:
                kat_sayi_secimi = int(input("1,2,3 seçeneklerinden birini seçiniz!\n"))
            daire.katsayi_secimi(kat_sayi_secimi)
            kisa_kenar = int(input("dairenin kısa kenarını metre cinsinden giriniz:\n"))
            uzun_kenar = int(input("dairenin uzun kenarını metre cinsinden giriniz:\n"))
            daire.dairenin_alani(kisa_kenar, uzun_kenar)
            print("Dairenin fiyatı {:0.2f} TL".format(daire.dairenin_fiyati()))
        denetleme = input("tekrar hesaplamak için e/E,çıkmak için h/H seçiniz \n")
        while denetleme != "e" and denetleme != "E" and denetleme != "h" and denetleme != "H":
            denetleme = input("e/E ya da h/H seçiniz!!\n")
        if denetleme == "e" or denetleme == "E":
            continue
        elif denetleme == "h" or denetleme == "H":
            exit()
