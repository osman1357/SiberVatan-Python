#Kullanıcıdan bir kelime alın ve kelimenin içindeki tüm 'a' harflerini '@' ile değiştirin.

kelime = input("lütfen bir kelime girin: ")
kelime = kelime.lower()
kelime_replace = kelime.replace ('a','@')
print(kelime_replace)