#Fonksiyonları Kullanarak Bir Hesap Makinası Yapınız.

def toplam(x,y):
    return x+y

def cıkarma(x,y):
    return x-y                                                 

def carpma(x,y):
    return x*y

def bolme(x,y):
    if y == 0:
        print("Tanımsız")
    else:
        sonuc_bolme = (x / y) 
        return sonuc_bolme
    
def faktoriyel(x):
    if (x == 0):
        print(x)
    else:
        x*x-1
    return

print("*-*-*-*-*-*-*-*-*-*-*-HOŞ GELDİNİZ*-*-*-*-*-*-*-*-*-*-*-\n")
print("toplamak için 1 e")
print("çıkarmak için 2 ye")
print("çarpmak için 3 e")
print("bölmek için 4 e")
print("faktöriyle için 5 e")
print("çıkış yapmak için 'çıkış' yazınız")
print("basınız")

operatör=int(input("Lütfen yapmak istediğiniz işlemi belirtin: "))
x =int(input("lütfen bir sayı giriniz: "))
y =int(input("lütfen bir sayı giriniz: "))

sonuc=0
if (operatör == 1):
    sonuc = toplam(x,y)
elif (operatör == 2):
    sonuc = cıkarma(x,y)
elif (operatör == 3):
    sonuc = carpma(x,y)
elif (operatör == 4):
    sonuc = bolme(x,y)
elif (operatör == 5):
    sonuc = faktoriyel(x)
    
    
    
    
    
elif (operatör == "çıkış"):
    quit
elif (operatör > 4):
    sonuc = ("lütfen geçerli bir sayı giriniz")
    quit

else:
    quit

print(sonuc)


