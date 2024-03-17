#list

liste = [1,2,3,4,5]  
print(liste)          # listeyi yazdırır  

print(liste[4])       #listenin 5. elemanı

print(type(liste))    #yaptığının ne tür olduğunu belirtiyor

liste[2] = 100        
print(liste)

alt_liste = liste[2:4]
print(alt_liste)
#----------------------------------------------
tuple

tuple = (10,20,30,40,50)
print(tuple)
print(tuple[1])

tuple[1] = 50
print(tuple)

alt_tuple = tuple[1:4]
print(alt_tuple)
#-----------------------------------------------
#kümeler  (set-sets)

kume = {100,200,300,400,500}
print(kume)

kume.add(700)
print(kume)
kume.update([400,900])
print(kume)
#-----------------------------------------------
#dict dictionary sözlük

dict ={'anahtar1':'deger1','anahtar2':'deger2'}
print(dict)

deger = dict['anahtar1']
print(deger)

kume_liste = list(kume)
print(kume_liste)
print(type(kume_liste))

kume_liste = list(kume)
print(kume_liste)
print(type(kume_liste))



list_keys = list(dict.keys())
list_values = list(dict.values())             #aynısı
print("keys",list_keys) 
print("values",list_values)

list_keys = list(dict.keys())               #aynısı
print(type(list_keys))
print(list_keys)

list_values = list(dict.values())
print(type(list_values))
print(list_values)

#------------------------------------------------------------

sayilar =[10,8,5,3,15,10]
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)
print(en_buyuk)
print(en_kucuk)
sayilar.append(20)
sayilar.append(1)


yeni_en_buyuk = max(sayilar)
yeni_en_kucuk = min(sayilar)

print(yeni_en_buyuk)
print(yeni_en_kucuk)
print(sayilar)

sayilar.pop()                    #pop yapısı sona geleni siler                 #fifo ilk giren ilk çıkan , lifo son giren son çıkan
print(sayilar)

sayilar.sort()
print(sayilar)                      #sayıları küçükten büyüğe sıralar           

sayilar.reverse()                   #sayıları büyükten küçüğe sıralar
print(sayilar)

print(sayilar.count(10))            #sayıdan kaç tane olduğunu gösterir

aralik = range(1,100)
print(list(aralik))

import random

rastgele_sayi = random.randint(1,100)
print("tutulan sayi",rastgele_sayi)

