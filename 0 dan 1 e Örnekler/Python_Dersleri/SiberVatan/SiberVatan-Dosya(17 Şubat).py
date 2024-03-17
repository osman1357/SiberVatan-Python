open("yenidosya.txt","w")            #open yeni dosya açmada işe yarar. (w) o klasörün ne yapacağını söyler.w= write (yazma modu)

#"w" write -> Yazma modu , yoksa oluşturur içeriği silip eklemek
#"a" append -> ekleme modu
#"x" creat -> oluşturma modu, aynısı varsa hata verir
#"r" read -> okuma modu

file = open("yenidosya.txt","w")
print(file)
file.close()
file_dizin = open("C:/Users/Monster_/Desktop/SiberVatan/yenidosya.txt","w")

file = open("yenidosya.txt","w")
file.write("Osman HULUSİ")
file.close()

file = open("yenidosya.txt","w",encoding='utf-8')
file.write("OSMAN HULUSİ gözel")
file.close()

file = open("yenidosya.txt","a",encoding='utf-8')
file.write("\nOSMAN HULUSİ")
file.close()

file = open("yenidosya2.txt","x")

try:
    file = open("yenidosya.txt","r",encoding='utf-8')
    print(file)
except FileNotFoundError:
    print("Dosya Bulunamadı")
finally:
    print("Dosya Kapandı")
    file.close()

for i in file:
    print(i,end="")

içerik = file.read()
print(içerik)

file = open("yenidosya.txt","r",encoding='utf-8')
içerik_karakter = file.read(0)
içerik_karakter = file.read(25)
print(içerik_karakter)
print("#############")
print(file.readline(),end="")
print(file.readline(),end="")

liste = file.readlines()
print(liste[0])
print(liste[1])
file.close()

with open("yenidosya.txt","r",encoding='utf-8') as file:
    content = file.read()
    print(content)
    file.seek(10)
    print(file.tell())
    content2 = file.read()
    print(content2)

with open("yenidosya.txt","r+",encoding='utf-8') as file:
    file.seek(20)
    file.write("siber vatan")



citylist=['Karabük','Bayburt','İzmir']

index=1
with open ("yenidosya.txt","a",encoding='utf-8')as file:
    for i in citylist:
        if index==len(citylist):
            file.write(i)
        else:
            file.write(i+"\n")
        index+=1


import math as islem

sonuc=islem.sqrt(5)
print(sonuc)

sonuc=islem.factorial(5)
print(sonuc)



from math import *

print(factorial(5))
print(sqrt(5))
print(factorial(5))


import random
sayilar=[0,1,2,3,4,5,6,7,8]
list=[]
i=0

while i!=6:
    list.append(random.choice(sayilar))
    i+=1

print(list)
random.shuffle(list)

print(list)


import math 

print(math.pow(6,6))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#KÜTÜPHANE YAZMA:

import SiberVatan

sayi = SiberVatan.sayilar[2]
print(sayi)

sayi2=SiberVatan.number
print(sayi2)

