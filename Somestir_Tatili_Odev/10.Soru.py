#Kullanıcıdan bir cümle alın, cümlede geçen kelimelerin içinde en uzun olanını bulun.

def en_uzun_kelime(cumle):
    kelimeler = cumle.split()
    en_uzun_kelime = max(kelimeler, key=len)
    return en_uzun_kelime

kullanicinin_cumlesi = input("Bir cümle girin: ")

sonuc = en_uzun_kelime(kullanicinin_cumlesi)

print(f"Cümledeki en uzun kelime: {sonuc}")
