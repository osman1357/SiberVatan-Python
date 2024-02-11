num1,num2,num3=50,60,70
num1+=num2

numbers=(50,55,60)
#print(type(numbers))
num1,num2,num3=numbers

a,b,c,d=50,100,50,70

#print(str(a < b))

sonuc=(a>b)
#print(sonuc)

sonuc=(a==c)
#print(sonuc)

sonuc= (a>d)
#print(sonuc)

sonuc=(a!=c)
#print(sonuc)

username1="Ceku"
username2="Arif"

sonuc = (username1=="Ahmet")
print(sonuc)

sonuc = (username2=="Arif")
print(sonuc)

print("A.R.O:G'a Hoşgeldiniz.\n")
username_input=input("Bir kullanıcı adı giriniz: ")

sonuc = (username1==username_input)
print(sonuc)

sonuc = (username2==username_input)
print(sonuc)

sonuc = (username1.lower()==username_input.lower())
sonuc2 = (username2.lower()==username_input.lower())

sonuc3=(sonuc != sonuc2)
print(sonuc3)

#SORU : Kullanıcıdan alınan email ve şifrenin önceden tanımlanmış sözlük içerisinde bulunup bulunmadığını
#bulan ve bunu ekrana yazdıran programı yazınız.

dict={'mesut':'123','hüsnü':'987'}
                                                             #doğru fakat şifre veya kullanıcı adı yanlış girildiğinde true veriyor.
kullanici_adi=input("Lütfen e mailinizi giriniz: ")          #dick kullanılmadı.
kullanici_şifre=input("Lütfen şifrenizi giriniz: ")         

dict_sonuc1= ('mesut'==kullanici_adi)
sonuc= ('123'==kullanici_şifre)                                   

                                                                  #YANLIŞ
dict_sonuc2= ('hüsnü'==kullanici_adi)
sonuc1= ('987'==kullanici_şifre)


sonuc_yeni=(sonuc != sonuc1)
sonuc_yeni1=(dict_sonuc1 != dict_sonuc2)

print(sonuc_yeni)
print(sonuc_yeni1)

#DOĞRUSU

users ={"osman@gmail.com":"osman7818","hulusi@gmail.com":"hulusi7818"}

print("-*-*-*-*A.R.O.G. Portalina hoş geldiniz-*-*-*-*\n")
print("-*-*-*-*A.R.O.G. Portalina hoş geldiniz-*-*-*-*\n")

input_mail=input("Mail giriniz..: ")
input_sifre=input("Sifregiriniz..: ")

sonuc_mail=(input_mail in users.keys())
sonuc_sifre=(input_sifre in users.values())

sonuc_final=(int(sonuc_mail)+int(sonuc_sifre)== 2 )

print("Eşleşme durumu..: ",sonuc_final)



fruits=['elma','muz','portakal','kivi']      # "in" komutu içinde var mı ? sorusunu sordurur
print('kiraz' in fruits)

x=y=[10,20,30]
z=[10,20,30]

print(x is y)                                # "is komutu" karşılaştırma yapar.(İki değişkenin adresleri aynı mı?)sorusunu sorar.
print(x is z)
print(x == z)                                # "==" içindekiler aynı mı? sorusunu sorar.

vize = int(input("aldığınız vize notunu yazınız: "))
final = int(input("aldığınız final notunu yazınız"))

ortalama=(vize * 0.4 + final * 0.6)
(ortalama >= 50,print("geçiyorsunuz"))
(ortalama <= 49,print("maalesef geçemiyorsunuz"))

