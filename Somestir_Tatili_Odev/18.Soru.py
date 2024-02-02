#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin karakter sayılarının toplamını bulun.
dict ={'anahtar1':'deger1','anahtar2':'deger2','anahtar3':'deger3'}


toplam_karakter_sayisi = sum(len(value) for value in dict.values() if isinstance(value, str))

print("Toplam karakter sayısı:", toplam_karakter_sayisi)
