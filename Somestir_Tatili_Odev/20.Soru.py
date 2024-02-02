#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin hepsini birleştirerek tek bir string elde edin.

dict ={
    'key1': 'Benim',
    'key2': ' ',
    'key3': 'Adım',
    'key4': 'Osman'
}
birlestirme = ''.join(dict.values())
print(birlestirme)