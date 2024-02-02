#Bir liste oluşturun,listenin ortasına yeni bir sayı ekleyin.

liste = [1, 2, 3, 4, 5, 6]

yeni_sayi = 20
ortalama = len(liste) // 2
liste.insert(ortalama, yeni_sayi)
print("Önceki Liste:", liste)
