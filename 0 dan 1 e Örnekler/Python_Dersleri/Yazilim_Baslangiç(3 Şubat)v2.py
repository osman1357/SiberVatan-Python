# if ve else kullanımı:

# girilen_sayi =int(input("lütfen bir sayı giriniz: "))        #eğer sayı çift ise True tek sayı ise False döner.
# result =(girilen_sayi > 0 ) and (girilen_sayi % 2 == 0)
# print('sonuc..: ' + str(result))


# x=98
# y=50

# if (x > y):
#     print("True")
# elif (x ==y):
#     print("sayilar eşittir.")
# else:
#     print("False")


# ad = ("osman")
# şifre = ("123")
# girilen_ad = input("lütfne kullanıcı adınızı giriniz: ")
# girilen_şifre = input("Lütfen şifrenizi giriniz: ")

# if ((ad == girilen_ad) and (şifre == girilen_şifre)):             #BAKILACAK
#     print("Hoş geldiniz")
# elif (şifre == "123"):
#     print("şifre hatalı")
# elif (ad == "osman"):
#     print("kullanıcı adı hatalı")
# else:
#     print("kullanıcı adı ve şifre hatalı")


#KULLANICIDAN ALINAN İKİ SAYININ İSTENİLEN MATEMATİKSEL İŞLEME TABİ TUTARAK SONUCU EKRANA YAZDIRAN PROGRAMI YAZINIZ.(HESAP MAKİNASI)

print("*-*-*-*-*-*-*-*-*-*-*-HOŞ GELDİNİZ*-*-*-*-*-*-*-*-*-*-*-\n")

operatör=int(input("Lütfen yapmak istediğiniz işlemi belirtin: "))

if (operatör == 1):
    x =int(input("lütfen bir sayı giriniz: "))
    y =int(input("lütfen bir sayı giriniz: "))
    sonuc_toplama = (x + y)
    print(sonuc_toplama)
elif (operatör == 2):
    x =int(input("lütfen bir sayı giriniz: "))
    y =int(input("lütfen bir sayı giriniz: "))
    sonuc_cıkarma = (x - y)
    print(sonuc_cıkarma)
elif (operatör == 3):
    x =int(input("lütfen bir sayı giriniz: "))
    y =int(input("lütfen bir sayı giriniz: "))
    sonuc_carpma = (x * y)
    print(sonuc_carpma)
elif (operatör == 4):
    x =int(input("lütfen bir sayı giriniz: "))
    y =int(input("lütfen bir sayı giriniz: "))
    if (y == 0):
        print(x)
    else:
        sonuc_bolme = (x / y)
        print(sonuc_bolme)
else:
    print("lütfen geçerli bir sayı giriniz")









