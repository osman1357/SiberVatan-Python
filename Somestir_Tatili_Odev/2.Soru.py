#Bir string içinde belirli bir karakterin kaç kez geçtiğini sayın.

cumle = input("lütfen bir metin giriniz:")
istenilen = input("lütfen kaç kez geçtiğini merak ettiğiniz karakteri giriniz:") 
deger = (cumle.count(istenilen))
deger = str(deger)
print ('cümlede ' + istenilen + ' ' + 'karakterinden ' + deger + ' ' + 'adet bulunmaktadır.')