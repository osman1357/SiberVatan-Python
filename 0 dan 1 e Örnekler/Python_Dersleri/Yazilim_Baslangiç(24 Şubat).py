
#sayiKontrol isimli bir fonksiyon yazın.BU fonksiyon kendisine gönderilen sayının basamakları birbirine eşit ise 1 değilse 0 döndürsün.Yazdığınız
#fonksiyonu A listesi sayılardan basamakları aynı olan ve olmayanları bulmak için kullanın.

def sayiKontrol(sayi):
    rakam_str = str(sayi)
    if len(set(rakam_str)) == 1:
        return 1
    else:
        return 0

A = [233,45,777,81,999999,36,90,88,11,61]

for sayi in A:
    if sayiKontrol(sayi):
        print(f"{sayi}: basamakları aynı")
    else:
        print(f"{sayi}: basamaklar farklı")

# #--------------------------------------------------------------------------------------------------------------------------------

# #CLASS OLUŞTURMA:

liste = [1,2,3,4,5]
print(type(liste))

class Person:
    address = "bilgi yok"
    def __init__(self,name,lname,address,tarih):
        self.name = name
        self.lname = lname
        self.address = address
        self.tarih = tarih
    
    def intro(self):
        print('merhaba ben'+ self.name)
    
    def calculate(self):
        return 2024 - self.tarih


p1 = Person(name="ali",lname="koç",address="5000 evler",tarih=2000)
print(p1)
print(type(p1))
print("benim adım",p1.name,"soyadım",p1.lname,"adres bilgisi",p1.address,"doğum tarihim",p1.tarih,"yaşım",p1.calculate())

p2 = Person(name="osman",lname="gözel",address="5000 evler",tarih=2008)
print(p2)
print("benim adım",p2.name,"soyadım",p2.lname,"adres bilgisi",p2.address,"doğum tarihim",p2.tarih,"yaşım",p2.calculate())

p1.intro()
p2.intro()


#--------------------------------------------------------------------------------------------------------------------------------------
#ALAN VE ÇEVRE HESAPLAMA              #1.Sonuç Alan   2.Sonuç Çevre
class Daire:
    pi=3.14
    
    def __init__(self,yaricap):
        self.yaricap = yaricap
    
    def cevre_hesaplama(self):
        return 2* self.pi * self.yaricap
    def alan_hesaplama(self):
        return self.pi * self.yaricap * self.yaricap
    
daire1 = Daire(5)
daire2 = Daire(5)
print(daire1.alan_hesaplama())
print(daire2.cevre_hesaplama())

#Karenin alanı:

class Square:
    def __init__(self,kenar):
        self.kenar = kenar
        
    def alan_hesaplama(self):
        return self.kenar * self.kenar #veya    return self.kenar ** 2 --> üstünü alma
    
kare1 = Square(6)
print(kare1.alan_hesaplama())












