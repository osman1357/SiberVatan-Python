

"""
import random
import string

def dogrulama_kodu():
    # Harf ve rakamları içeren bir karakter seti oluştur
    karakter_seti = string.ascii_letters + string.digits
    
    # Rastgele 5 karakter seç ve birleştir
    dogrulama_kodu = ''.join(random.choice(karakter_seti) for _ in range(5))
    
    return dogrulama_kodu

print("Rastgele doğrulama kodu:", dogrulama_kodu())
"""





import random
import string

def dogrulama_kodu_olustur():
    harfler = string.ascii_letters  # A'dan Z'ye büyük ve küçük harfler
    rakamlar = string.digits  # 0'dan 9'a rakamlar
    karakterler = harfler + rakamlar
    kod = ''.join(random.choice(karakterler) for i in range(5))  # Rastgele 5 karakterli kod oluştur
    return kod

def dogrulama_kodu_kontrol(kod, girilen_kod):
    return kod == girilen_kod

doğrulama_kodu = dogrulama_kodu_olustur()
print("Doğrulama kodu:", doğrulama_kodu)

girilen_kod = input("Lütfen doğrulama kodunu girin: ")

if dogrulama_kodu_kontrol(doğrulama_kodu, girilen_kod):
    print("Giriş başarılı!")
else:
    print("Hatalı kod girdiniz!")

