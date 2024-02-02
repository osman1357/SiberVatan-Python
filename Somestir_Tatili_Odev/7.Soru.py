#Bir string içinde belirli bir alt dizeyi (substring) arayın ve yerine başka bir alt dize ekleyin.
substring = input("Lütfen bir cümle giriniz: ")
kelime1 = input("Lütfen değişmesini istediğiniz kelimeyi yazınız: ")
kelime2 = input("Lütfen yazılmasını istediğiniz kelimeyi yazınız: ")

substring = substring.lower()
kelime1 = kelime1.lower()
kelime2 = kelime2.lower()

def replace_substring(substring, kelime1, kelime2):
     return substring.replace(kelime1, kelime2)

yeni = replace_substring(substring, kelime1, kelime2)
print(yeni)