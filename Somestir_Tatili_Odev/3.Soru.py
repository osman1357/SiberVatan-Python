#Kullanıcıdan bir kelime ve bir harf alın, kelimenin içindeki o harfi kaç kez içerdiğini kontrol edin.

kelime = input("lütfen bir kelime giriniz: ")
harf = input("lütfen bir harf giriniz: ")
sayi = (kelime.count(harf))
sayi = str(sayi)
print ('kelimenizde ' + sayi + ' adet ' + harf + ' harfi bulunmaktadır.')