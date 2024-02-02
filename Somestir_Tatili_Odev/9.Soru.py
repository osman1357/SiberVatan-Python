#Kullanıcıdan bir kelime alın ve kelimenin palindrome (tersinden de okunduğunda aynı olan) olup olmadığını kontrol edin.

kelime = input("lütfen bir kelime giriiz: ")
kelime = kelime.lower()
kelime_ters =(kelime[::-1])

if kelime_ters != kelime:
    print("Yazmış olduğunuz kelime tersinden okunduğunda aynı değildir.")
else:
    print("Yazmış olduğunuz kelime tersinden okunduğunda aynıdır.")
