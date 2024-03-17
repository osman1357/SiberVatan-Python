#Fonksiyonlar

def selamdunya():
    print("hello world")

selamdunya()


def hosgeldin(name):
    print("hoşgeldin "+ name)

hosgeldin('osman')


naber=(input("Lütfen isminizi giriniz: "))

def nasılsın(naber):
    print("nasılsın "+ naber)

nasılsın(naber)


def selamVer(isim):
    print("hosgeldin "+ isim)

selamVer(input("Lütfen isminizi giriniz: "))


def fonksiyon(sehir = "karabük"):
    print("en sevidğim şehir "+ sehir)

fonksiyon("isntabul")
fonksiyon()


def sayi(x):
    x= x+5
    return x
sonuc =sayi(10)
print(sonuc)


#FONKSİYON 2 PARAMETRE FONKSİYON İÇİ İKİ SAYIYI TOPLA YAZDIR.

def sayi(sonuc):
    x = int(input("lütfen bir sayı giriniz:"))
    y= int(input("Lütfen bir sayı giriniz: "))
    z = x+y
    return z
sonuc = sayi(45)
print(sonuc)

#FARKLI BİR ŞEKİLDE YAPIMI:

def topla(num1,num2):
    toplam= num1 + num2
    return toplam
sonuc=topla(10,50)
print(sonuc)


def fonk_tuple(*argv):
    for arg in argv:
        print(arg)

fonk_tuple('selam','naber','nasılsın','iyidir')

#Kullanıcıdan sayı alınıp o sayıya kadar olan çift sayıları fonksiyon içinde bulup bir listeye ekleyin ve listeyi yazdırın
#Örnek: sayıyı giriniz=8
#output= çift sayılar [0,2,4,6,8]

def ciftSayi(n):
    ciftsayi_list=[]
    for i in range(0,n+1):
        if i % 2 == 0:
            ciftsayi_list.append(i)
    return ciftsayi_list
limit = int(input("lütfen bir üst sınır giriniz: "))
print("çift sayılar", ciftSayi(limit))


