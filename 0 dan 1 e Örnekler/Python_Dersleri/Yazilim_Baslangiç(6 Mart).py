#SORU:programınızın olduğu mevcut dizisini alsın ve sizin içini döngüyle ekrana yazsın
#daha sonra olduğunuz dininin içine yeni bir dizin oluşturun
#yeni dizine gidin
#yeni dizin içinde bir txt dosyası açıp içine hello world yazdırın ve kaydedin
#oluşturduğunuz txt dosyasını silin
#önceki dizine döünün
#ve oluşturduğunuz dizini silin

import os

gecerli_dizin = os.getcwd()
print(gecerli_dizin)

for i in os.listdir(gecerli_dizin):
    print(i)

new_directory = os.path.join(gecerli_dizin,"yeni_dizin")
os.mkdir(new_directory)
print(f"{new_directory} oluştu")

os.chdir(new_directory)
print(f"{new_directory}dizinine gidildi.")

dosya_yolu = os.path.join(new_directory,"example.txt")
with open(dosya_yolu,'w',encoding='utf-8') as file:
    file.write("hellö WÖRLD")

os.remove('example.txt')
print("dosya silindi")
os.chdir(gecerli_dizin)
print("dosktopa gidildi")
os.rmdir('yeni_dizin')
print("açtığım dizini sildim")

