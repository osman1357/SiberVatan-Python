#SORU: python dili kullanarak 5 boyutuna sahip bir liste oluşturun.bu liste sırasıyla kullanıcıdan değerler alınarak doldurulacaktır.
#Klavyede girilen bu değerlerden 3 ile tam bölünenler listenin başından itibaren bölünemeyen ise sonundan itibaren diziyi eklenecektir.
#liste tamamen doldurulduktan sonra son halini ekrana yazdırın.

sayilar = []
sayi = 0
while sayi<5:
    sayi = int(input("Lütfen bir sayı giriniz: "))                 #BENİM YAPTIĞIM
    for i in sayilar:
        if (sayi %3 == 0):
            sayilar.append(sayi)
        else:
            continue

#--------------------------------------------------------------------------------------------------------------------------------------------

toplam = 5
liste = []

for i in range(toplam):
    deger = int(input("Lütfen bir sayı giriniz: "))                     #Bölünen sayılar sola,bölünemeyenler sağa yazıldı.
    if deger %3 == 0:                                                   #"insert" listenin başına,"append" listenin sonuna ekler.
        liste.insert(0,deger)
    else:
        liste.append(deger)

print(liste)

#-------------------------------------------------------------------------------------------------------------------------------------------

class Kisi:
    def __init__(self,name,age):
        self.name = name                                                 #Yeni Konu
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"
k1 = Kisi(name="osman",age="16")
print(k1)

#------------------------------------------------------------------------------------------------------------------------------------------

#SORU:Bir adet soru class ı olacak bu class soru ve cevapları alacak 3 adet soru ve cevap alsın "başkent neresidir" "ankara" gibi sonra bir
#listeye bu nesnelerin soru kısımlarını gönderip kullanıcıdan cevaoları alacak eğer ankara cevabı gelirse doğrı kabul edecek karabük
#cevabı gelirse yanlış kabul edecek.doğru cevapları artırıp sonunda kaç soruya doğru cevap verdiğini kullanıcıya söyleyecek.

class Soru:
    def __init__(self,soru,cevap):
        self.soru = soru
        self.cevap = cevap
    def dogru_mu(self,tahmin):
        return self.cevap == tahmin
soru1 = Soru("başkent neresi:","ankara")
soru2 = Soru("en kalabalık şehir:","istanbul")
soru3 = Soru("em güzel şehir:","konya")

dogru_cevaplar = 0
sorular = [soru1,soru2,soru3]
for i in sorular:
    cevap = input(i.soru)
    if i.dogru_mu(cevap):
        dogru_cevaplar += 1

print(f"doğru cevap sayısı {dogru_cevaplar}")

