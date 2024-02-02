#Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın.

cumle = input("Lütfen bir cümle giriniz: ")
cumle = cumle.lower()
kelime = cumle.split()
kelime.sort()

print("Alfabetik sıraya göre sıralanmış hali: ")
print(kelime)
