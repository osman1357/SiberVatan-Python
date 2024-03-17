def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)
sayi = 998
print(faktoriyel(sayi))



x = "global değişken"

def function():
    x ="local degisken"
    print(x)
function()
print(x)

#ERROR lar:


#print(a)                                     # NameError verir.Tanımlanmayınca gösterir.

#int("a19")                                   # ValueError verir.Sayısal değer girilmediğinde gösterir.

#print(10/0)                                  #ZeroDivisionError verir.Bir şeyi sıfıra bölmeye çalıştığımızda gösterir

#print('hello'world)                          #SyntaxError verir.Yanlış kullanımda gösterir

try:
    x = int(input("x giriniz"))
    y = int(input("y giriniz"))
    print(x/y)
except ZeroDivisionError:
    print("sıfıra bölünme hatası")

except ValueError:
    print("x ve y için sayısal değer giriniz")

except Exception as ex:
    print("bilgiler yanlış", ex)

while True:
    try:
        x = int(input("lütfen x giriniz"))
        y = int(input("lütfen y giriniz"))
        print(x/y)
    except Exception as ex:
        print("Bilgiler yanlış", ex)
    else:
        break
    finally:
        print("Her şey yolunda")


while True:
    try:
        x= int(input("lütfen x gir"))
        y= int(input("lütfen y girin"))
        print(x/y)
    except ZeroDivisionError:
        print("Sıfıra Bölünme Hatası")
    except ValueError:
        print("x ve y için sayısal değer giriniz")
    except SyntaxError:
        print("Bir şeyler ters gitti")
    except NameError:
        print("Ad tanımlanmasında hata var")
    except Exception as ex:
        print("Bilgiler yanlış", ex)
    else:
        break
    finally:
        print("On numara çalışıyor")



#ÖRNEK PAROLA KOYMA:

import re
def parola_kontrol(parola):
    if len(parola)<8:
        raise Exception("Parola en az 8 karakter")
    elif not re.search("[a-z]",parola):
        raise Exception("Parola küçük harf içermelidir")
    elif not re.search("[A-Z]",parola):
        raise Exception("Parola büyük harf içermelidir")
    elif not re.search("[0-9]",parola):
        raise Exception("Parola sayı içermelidir")

password=input("Lütfen bir şifre giriniz: ")
try:
    parola_kontrol(password)
except Exception as ex:
    print(ex)
else:
    print("Parola oluşturma başarılı")







