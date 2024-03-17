#SORU: kullanıcıdan alınan bir kelimenin palindrom olup olmadığını kontrol eden fonksiyonu yazınız.

kelime = input("lütfen bir kelime giriiz: ")
kelime = kelime.lower()
kelime_ters =(kelime[::-1])

if kelime_ters != kelime:
    print("Yazmış olduğunuz kelime tersinden okunduğunda aynı değildir.")
else:
    print("Yazmış olduğunuz kelime tersinden okunduğunda aynıdır.")

# #----------------

def palindrom_mu(metin):
    temiz_metin = metin
    return temiz_metin == temiz_metin[::-1]
metin = input("metin giriniz: ")
if palindrom_mu(metin):
    print("bu palindrom bir kelimedir")
else:
    print("bu bir palindrom değildir")

#-----------------------------------------------------------------------------------------------------------------------------
#SORU: verilen iki listedeki ortak elemanları bulan fonksiyonu yazınız.

def ortak_elemanlar(liste1,liste2):
    ortaklar = set()
    for i in liste1:
        if i in liste2:
            ortaklar.add(i)
    return ortaklar

liste1 = [1,2,3,4,5]
liste2 = [3,4,5,6,7]

ortaklar = ortak_elemanlar(liste1,liste2)
print = (ortaklar)

#---------------------------------------------------------------------------------------------------------------------------------
#SORU: Verilen bir listedeki her bir elemanın frekansını(sıklığı) bulan bir python fonksiyonu yazınız.

def eleman_freaksnsi(liste):
    frekanslar = {}
    for eleman in liste:
        if eleman in frekanslar:
            frekanslar[eleman] += 1
        else:
            frekanslar[eleman] = 1
    return frekanslar

liste_ornegi = [2,3,5,7,9,29,42,13,7,2,96,5]

sonuc = eleman_freaksnsi(liste_ornegi)

for eleman,frekans in sonuc.items():
    print(f"{eleman}: {frekans}")
#--------------------------------------------------------------------------------------------------------------------------------#
#SORU: Verilen bir pozitif tam sayı için fibonacci dizisinin ilk n terimini hesaplayan bir fonksiyonu yazın.
# fibonacci
# n=10
# 0,1,1,2,3,5,8,13,21,34 Çıktı=34


def fibonacci(n):
    fibo = [0,1]

    for _ in range(2,n):
        next = fibo[-1] + fibo[-2]
        fibo.append(next)
    return fibo
n = 10
fibo = fibonacci(n)
print(f"{fibo}")
#---------------------------------------------------------------------------------------------------------------------------------------------#

