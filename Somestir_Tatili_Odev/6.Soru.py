#Kullanıcıdan iki string alın, bu stringleri birleştirin ve tüm karakterleri küçük harfe çevirin.

cumle1 = input("Lütfen bir cümle girin: ")
cumle2 = input("lütfen bir cümle girin: ")
cumle3 = (cumle1 + ' ' + cumle2)
cumle3 = cumle3.lower()
print(cumle3)