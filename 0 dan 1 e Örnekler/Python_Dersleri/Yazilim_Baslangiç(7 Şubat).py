meyveler=["elma","kivi","limon","bögurtlen"]
print(meyveler[2])

sayilar=[10,20,30,40,50]
toplam=0

for sayi in sayilar:
    toplam+=sayi
print(toplam)

meyveler=["elma","kivi","limon","bögurtlen"]

for meyve in meyveler:
    print(meyve)


sayilar=[2,3,6,7,8,89,43,76,34,23]
#Çift sayıları ekrana yazdıran kod
for sayi in sayilar:
    if (sayi%2 == 0):
        print(sayi)
    else:
        continue
        



#While komutu ve kullanımı(koşul)

sayi=int(input("Bir sayı giriniz: "))
sayac=0

while sayac<=sayi:
    print(sayac)
    sayac+=1


#Kullanıcıdan 5 sayı alıp boş listeye ekleyen ve en sonunda ekrana yazdıran programı yazınız.

liste = []
sayi = 0
while sayi<5:
    sayi = int(input("Lütfen bir sayı giriniz: "))
    liste.append(sayi)
print(liste)

