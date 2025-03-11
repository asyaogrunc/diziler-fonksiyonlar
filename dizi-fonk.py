def sayilari_bul():
    sayilar = []
    
    for i in range(5):
        sayi = int(input("Bir tam sayı girin: "))
        sayilar.append(sayi)
    
    en_kucuk = min(sayilar)
    en_buyuk = max(sayilar)
    
    print("En küçük sayı: " + str(en_kucuk))
    print("En büyük sayı: " + str(en_buyuk))

sayilari_bul()
