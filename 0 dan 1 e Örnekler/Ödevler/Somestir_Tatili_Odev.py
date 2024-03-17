#1.SORU:
#Kullanıcıdan bir cümle alın, cümlenin başındaki ve sonundaki boşlukları kaldırın, ardından tüm harfleri küçük harfe çevirin.

cumle = input("lütfen bir cümle yazınız:")
cumle = cumle.strip()
cumle_kucuk= cumle.lower()
print(cumle_kucuk)
 
 
#2.SORU:
#Bir string içinde belirli bir karakterin kaç kez geçtiğini sayın.

cumle = input("lütfen bir metin giriniz:")
istenilen = input("lütfen kaç kez geçtiğini merak ettiğiniz karakteri giriniz:") 
deger = (cumle.count(istenilen))
deger = str(deger)
print ('cümlede ' + istenilen + ' ' + 'karakterinden ' + deger + ' ' + 'adet bulunmaktadır.')


#3.SORU
#Kullanıcıdan bir kelime ve bir harf alın, kelimenin içindeki o harfi kaç kez içerdiğini kontrol edin.

kelime = input("lütfen bir kelime giriniz: ")
harf = input("lütfen bir harf giriniz: ")
sayi = (kelime.count(harf))
sayi = str(sayi)
print ('kelimenizde ' + sayi + ' adet ' + harf + ' harfi bulunmaktadır.')



#4.SORU:
#İki string'i birleştirin ve ardından bir substring arayın ve konumunu bulun.

cumle1 = input("lütfen bir cümle girin: ")
cumle2 = input("lütfen bir cümle girin: ")
aranan = input("lütfen aramak istediğiniz substringi girin: ")
cumle3 = (cumle1 + ' ' + cumle2)
konum = cumle3.find(aranan)
konum = str(konum)
    
if aranan in cumle3:
    print("Cümle içinde aradığınız substring mevcut")
else:
    print("Lütfen geçerli bir substring girin")


#5.SORU:
#Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın.

cumle = input("Lütfen bir cümle giriniz: ")
cumle = cumle.lower()
kelime = cumle.split()
kelime.sort()

print("Alfabetik sıraya göre sıralanmış hali: ")
print(kelime)

#6.SORU:
#Kullanıcıdan iki string alın, bu stringleri birleştirin ve tüm karakterleri küçük harfe çevirin.

cumle1 = input("Lütfen bir cümle girin: ")
cumle2 = input("lütfen bir cümle girin: ")
cumle3 = (cumle1 + ' ' + cumle2)
cumle3 = cumle3.lower()
print(cumle3)


#7.SORU:
#Bir string içinde belirli bir alt dizeyi (substring) arayın ve yerine başka bir alt dize ekleyin.
substring = input("Lütfen bir cümle giriniz: ")
kelime1 = input("Lütfen değişmesini istediğiniz kelimeyi yazınız: ")
kelime2 = input("Lütfen yazılmasını istediğiniz kelimeyi yazınız: ")

substring = substring.lower()
kelime1 = kelime1.lower()
kelime2 = kelime2.lower()

def replace_substring(substring, kelime1, kelime2):
     return substring.replace(kelime1, kelime2)

yeni = replace_substring(substring, kelime1, kelime2)
print(yeni)


#8.SORU:
#Kullanıcıdan bir kelime alın ve kelimenin içindeki tüm 'a' harflerini '@' ile değiştirin.

kelime = input("lütfen bir kelime girin: ")
kelime = kelime.lower()
kelime_replace = kelime.replace ('a','@')
print(kelime_replace)


#9.SORU:
#Kullanıcıdan bir kelime alın ve kelimenin palindrome (tersinden de okunduğunda aynı olan) olup olmadığını kontrol edin.

kelime = input("lütfen bir kelime giriiz: ")
kelime = kelime.lower()
kelime_ters =(kelime[::-1])

if kelime_ters != kelime:
    print("Yazmış olduğunuz kelime tersinden okunduğunda aynı değildir.")
else:
    print("Yazmış olduğunuz kelime tersinden okunduğunda aynıdır.")



#10.SORU:
#Kullanıcıdan bir cümle alın, cümlede geçen kelimelerin içinde en uzun olanını bulun.

def en_uzun_kelime(cumle):
    kelimeler = cumle.split()
    en_uzun_kelime = max(kelimeler, key=len)
    return en_uzun_kelime

kullanicinin_cumlesi = input("Bir cümle girin: ")

sonuc = en_uzun_kelime(kullanicinin_cumlesi)

print(f"Cümledeki en uzun kelime: {sonuc}")


#11.SORU:
#Bir liste oluşturun ve listenin ortasındaki elemanı bulun.

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

orta = len(liste) // 2

orta_eleman = liste[orta]
print("Listenin ortasındaki eleman: ", orta_eleman)

#12.SORU:
#Bir tuple oluşturun, tuplein 2. ve 4. elemanlarını yeni bir tuple olarak alın.

tuple = (10,20,30,40,50)
Yeni_tuple = (tuple[1]), (tuple[3])
print(Yeni_tuple)


#13.SORU:
#Bir set oluşturun, set içine bir sayı ekleyin,ardından bu sayıyı setden çıkarın.

kume = {100,200,300}
kume.add(600)
kume.remove(200)
kume = str(kume)
print("En son hali: ", kume)


#14.SORU:
#Bir dictk oluşturun, dicte yeni bir anahtar-değer çifti ekleyin, ardından bir anahtarı silin.

dict ={'anahtar1':'deger1','anahtar2':'deger2'}
dict.update({'anahtar3':'deger3'})
del dict['anahtar2']
print(dict)


#15.SORU:
#Bir liste oluşturun,listenin ortasına yeni bir sayı ekleyin.

liste = [1, 2, 3, 4, 5, 6]

yeni_sayi = 20
ortalama = len(liste) // 2
liste.insert(ortalama, yeni_sayi)
print("Önceki Liste:", liste)


#16.SORU:
#Bir liste oluşturun ve listenin ortasındaki elemanı bir tuplee ekleyin.
liste = [1,2,3,4,5,6,7,8,9]
liste2 = len(liste) // 2
tuple = (100)
liste.insert(liste2, tuple)
print(liste)


#17.SORU:
#Bir set oluşturun ve setin elemanlarını içeren bir liste oluşturun, ardından bu liste elemanlarının toplamını hesaplayın.
set= {2, 4, 6, 8, 10}

liste = list(set)

toplam = sum(liste)

print("Oluşturulan Set:", set)
print("Set Elemanlarını İçeren Liste:", liste)
print("Liste Elemanlarının Toplamı:", toplam)



#18.SORU:
#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin karakter sayılarının toplamını bulun.
dict ={'anahtar1':'deger1','anahtar2':'deger2','anahtar3':'deger3'}


toplam_karakter_sayisi = sum(len(value) for value in dict.values() if isinstance(value, str))

print("Toplam karakter sayısı:", toplam_karakter_sayisi)



#19.SORU:
#Bir liste oluşturun ve listenin içindeki en büyük sayıyı bulun, ancak sadece aritmetik operatörler (+, -, *, /) kullanmadan yapın.

liste = (3, 7, 1, 15, 4, 11, 99,)
sayi = max(liste)
sayi1 = str(sayi)
print("En büyük sayı: ", sayi)


#20.SORU:
#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin hepsini birleştirerek tek bir string elde edin.

dict ={
    'key1': 'Benim',
    'key2': ' ',
    'key3': 'Adım',
    'key4': 'Osman'
}
birlestirme = ''.join(dict.values())
print(birlestirme)