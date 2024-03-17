
def hesaplama_saatlik(toplam_calısma_saat):
    saatlik_ucret = 50
    if toplam_calısma_saat <= 40:
        maas = toplam_calısma_saat * saatlik_ucret 
    else:
        normal_calisma_saati = 40
        fazla_mesai_saati = toplam_calısma_saat - 40
        maas = normal_calisma_saati * saatlik_ucret + fazla_mesai_saati * (saatlik_ucret * 1.5)
    return maas

def hesaplama_komisyon(aylik_satis):
    sabit_maas = 500
    komisyon_orani = 0.05
    komisyon = aylik_satis * komisyon_orani
    maas = sabit_maas + komisyon
    return maas

while True:
    odeme_kodu = int(input("odeme kodu girin 1 saatlik 2 komisyonlu: "))
    if odeme_kodu == 1:
        calisma_saati = int(input("toplam çalışma saatini giriniz: "))
        maas = hesaplama_saatlik(calisma_saati)
        print("maaşınız",maas)
        break
    elif odeme_kodu == 2:
        aylik_satis=(input("aylık satış miktarını girin: "))
        maas = hesaplama_komisyon(aylik_satis)
        print("maaşınız",maas)
        break
    else:
        print("geçerli bir komut giriniz.")



#SORU: Liste içerisinde bir şehre ait günlük ortalama sıcaklık bilgileri tutulmaktadır.Günlük ortalama sıcaklık bilgileri -20 ile 40 derece arasındadır.Buna
#bu dizeyi parametre olrak alan ve 
#(-20)-(0)
#(0)-(20)
#(20)-(40)
#değerleri arasında kaç adet sıcaklık olduğunu bulup bu sırada  ekrana yazdıram bir fonksiyon yazınız.


def sicaklik_araligi(sicakliklar):
    sicaklik_araliklari = {
        "(-20) - (0)": 0,
        "(0) - (20)": 0,
        "(20) - (40)": 0,
    }
    
    for sicaklik in sicakliklar:
        if -20 <= sicaklik < 0:
            sicaklik_araliklari["(-20) - (0)"] += 1
        elif 0 <= sicaklik < 20:
            sicaklik_araliklari ["(0) - (20)"] += 1
        elif 20 <= sicaklik < 40:
            sicaklik_araliklari["(20) - (40)"] += 1
    
    for aralik,sayi in sicaklik_araliklari.items():
        print(aralik,"arasında",sayi,"tane sıcaklık var")

sicaklik_listesi=[5, 15, 25, 12, 2, 30, 18, -5, 35,-18, 8]
sicaklik_araligi(sicaklik_listesi)












