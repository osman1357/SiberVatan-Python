
#1.SORU:

#Bir fonksiyon oluşturun. Emeklilik yaşını 65 olarak belirleyin. Kullanıcıdan yaşını alıp 65 yaş altındakilere emekliliğine kaç yıl kaldığını
#65 yaş üstüne zaten emekli olduğunu ekrana yazdırın.
#örnek:yaş giriniz:60
#output:emekliliğinize 5 yıl kaldı
#örnek:yaş giriniz:70
#output:zaten emekli oldunuz

def emeklilik(yas):
    emeklilik_yasi = 65
    if (yas < emeklilik_yasi):
        kalan = emeklilik_yasi - yas
        print("Emekliliğinize kalan süre: ", kalan, "yıldır.")
    else:
        print("emekli oldunuz.")

Yas = int(input("lütfen yaşınızı giriniz: "))
emeklilik(Yas)


#2.SORU:

#Bir fonksiyon oluşturun.Fonksiyon kullanıcıdan iki sayı alıp bu iki sayı arasındaki asal sayıları ekrana bastırın.
#örnek:sayı gir:10
#      sayı1 gir:20
#output:iki sayı arasındaki asal sayılar 11,13,17,19

def asal_sayilari_bul():
    sayi1 = int(input("İlk sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))

    print(f"{sayi1} ile {sayi2} arasındaki asal sayılar:")

    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, int(sayi**0.5) + 1):
                if (sayi % i) == 0:
                    break
            else:
                print(sayi)

asal_sayilari_bul()




#3.SORU:

# İki fonksiyon oluşturun. İki fonksiyon içinde de listeler olsun ilk fonksiyon içindeki listenin en büyük sayısını ikinci fonksiyon içindeki
# listenin en küçük sayısını toplayıp ekrana bastırın.
# örnek list1 [10,15,20]
#       list2 [5,100,250]	
# output:25

def en_buyuk_bul(liste):
    if not liste:
        return None
    else:
        return max(liste)

def en_kucuk_bul(liste):
    if not liste:
        return None
    else:
        return min(liste)

def toplama_ve_yazdir(liste1, liste2):
    en_buyuk_liste1 = en_buyuk_bul(liste1)
    en_kucuk_liste2 = en_kucuk_bul(liste2)

    if en_buyuk_liste1 is not None and en_kucuk_liste2 is not None:
        toplam = en_buyuk_liste1 + en_kucuk_liste2
        print("Output:", toplam)
    else:
        print("Bir veya her iki liste boş.")

list1 = [10, 15, 20]
list2 = [5, 100, 250]

toplama_ve_yazdir(list1, list2)


#4.SORU:

# Bir fonksiyon oluşturun. Fonksiyon içinde bir tane liste olsun ve bu listenin ilk ve son sayısı eşitse ekrana true değilse false yazdırsın.
# örnek list[10,20,30,50]
# output:false
# örnek list[10,20,30,10]
# output:true

def kontrol_fonksiyonu(lst):
    if len(lst) < 2:
        return False
    
    return lst[0] == lst[-1]

liste1 = [10, 20, 30, 50]
print(kontrol_fonksiyonu(liste1))

liste2 = [10, 20, 30, 10]
print(kontrol_fonksiyonu(liste2))



#5.SORU:

# Bir sayının palindrom sayı olup olmadığını kontrol eden fonksiyonu yazınız.
# örnek:525 
# output:525 sayısı palindromdur
# örnek 124
# output:124 sayısı palindrom değildir.

def is_palindrome(number):
    str_number = str(number)
    reversed_str = str_number[::-1]
    
    if str_number == reversed_str:
        return f"{number} sayısı palindromdur."
    else:
        return f"{number} sayısı palindrom değildir."

num1 = 525
num2 = 124

result1 = is_palindrome(num1)
result2 = is_palindrome(num2)

print(result1)
print(result2)



#6.SORU:

#Bir fonksiyon oluşturun. Fonksiyon içinde iki liste olsun ilk listenin çift sayılarını ikinci listenin tek sayılarını alıp yeni bir listeye ekleyin ve ekrana yazdırın.


def combine_lists(list1, list2):
    liste_1 = [num for num in list1 if num % 2 == 0]
    liste_2 = [num for num in list2 if num % 2 != 0]
    yeni_list = liste_1 + liste_2

    print("Combined List:", yeni_list)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

combine_lists(list1, list2)


#7.SORU:

#rus ruleti oyunu yazın. Random kütüphanesi kullanarak 1-6 arasında bir sayı seçilsin ve kullanıcıdan bir sayı alsın eşit olduğunda oyun biter.
#2 fonksiyon kullanarak yazabilirsiniz.

import random

def zar_at():
    return random.randint(1, 6)

def oyun():
    hedef_sayi = zar_at()
    print(f"Hedef sayı: {hedef_sayi}")

    while True:
        kullanici_sayi = int(input("Bir sayı girin (1-6 arasında): "))

        if kullanici_sayi < 1 or kullanici_sayi > 6:
            print("Geçersiz giriş! Lütfen 1-6 arasında bir sayı girin.")
            continue

        zar_sonucu = zar_at()
        print(f"Zar atıldı: {zar_sonucu}")

        if kullanici_sayi == zar_sonucu:
            print("WASTED")
            break
        else:
            print("Hayatta Kaldın")

if __name__ == "__main__":
    oyun()