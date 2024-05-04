import datetime


# Kantin sahibinin kullanıcı adı ve şifresi
kantinci_kullanici_adi = "kantinci"
kantinci_sifre = "kantinci123"

# Müdürün özel şifresi
mudur_ad = "Mudur"
mudur_soyad = "123"
mudur_sifre = "1453"

# Kantinde bulunan ürünlerin veritabanı
urunler = [
    {"adi": "Sandviç", "fiyat": 10, "foto": "sandvic.jpg"},
    {"adi": "Makarna", "fiyat": 8, "foto": "makarna.jpg"},
    {"adi": "Salata", "fiyat": 7, "foto": "salata.jpg"}
]

# Öğrenci veritabanı
ogrenciler = {}

# Öğrenci mesajları
ogrenci_mesajlari = {}

# Log dosyasına giriş kaydı ekleme
def loga_kaydet(tur, kullanici_adi, mesaj):
    with open("log.txt", "a") as file:
        file.write(f"Tarih: {datetime.datetime.now()}, Tür: {tur}, Kullanıcı: {kullanici_adi}, Mesaj: {mesaj}\n")

# Öğrenci girişi
def ogrenci_girisi():
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    telefon = input("Telefon Numaranız: ")
    okul_no = input("Okul Numaranız: ")
    sinif = input("Sınıfınız: ")

    # Kantinde bulunan ürünleri listeleme
    print("Kantin Ürünleri:")
    for i, urun in enumerate(urunler, 1):
        print(f"{i}. {urun['adi']} - {urun['fiyat']} TL")

    secim = input("Ayırtmak istediğiniz ürün numarasını girin (çıkmak için 'q' tuşuna basın): ")
    if secim == "q":
        return
    elif secim.isdigit() and 0 < int(secim) <= len(urunler):
        secilen_urun = urunler[int(secim) - 1]
        print(f"{secilen_urun['adi']} seçildi. Ayırtma işlemi tamamlandı.")
        
        # Öğrencinin ayırdığı ürünü kaydetme
        ogrenciler[okul_no] = {
            "ad": ad,
            "soyad": soyad,
            "telefon": telefon,
            "okul_no": okul_no,
            "sinif": sinif,
            "ayirttigi_urun": secilen_urun['adi']  # Ayırtılan ürünü kaydet
        }

        # Log dosyasına giriş kaydı ekleme
        loga_kaydet("Öğrenci", okul_no, f"{ad} {soyad} tarafından {secilen_urun['adi']} ayırtıldı")  # Mesajı kaydet
    else:
        print("Geçersiz ürün numarası.")

# Kantinci girişi
def kantinci_girisi():
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    sifre = input("Şifreniz: ")
    if ad == "kantinci" and soyad == "123" and sifre == "1092":
        print("Kantinci olarak giriş yapıldı.")
        while True:
            print("1. Ürün Ekle")
            print("2. Ürün Sil")
            print("3. Öğrencileri Görüntüle")
            secim = input("Seçiminizi yapın (çıkış için 'q' tuşuna basın): ")
            if secim == "1":
                yeni_urun_adi = input("Lütfen Ürün Adı Girin: ")
                while True:
                    yeni_urun_fiyat = input("Lütfen Ürün Fiyatı Girin (ondalık sayı kullanın): ")
                    if yeni_urun_fiyat.replace(".", "", 1).isdigit():
                        urunler.append({"adi": yeni_urun_adi, "fiyat": float(yeni_urun_fiyat), "foto": ""})
                        print("Ürün başarıyla eklendi.")
                        break
                    else:
                        print("Geçersiz fiyat. Lütfen ondalık sayı kullanın.")
            elif secim == "2":
                print("Kantinde bulunan ürünler:")
                for i, urun in enumerate(urunler, 1):
                    print(f"{i}. {urun['adi']}")
                silinecek_urun_index = input("Silmek istediğiniz ürünün numarasını girin: ")
                if silinecek_urun_index.isdigit() and 0 < int(silinecek_urun_index) <= len(urunler):
                    silinecek_urun = urunler.pop(int(silinecek_urun_index) - 1)
                    print(f"{silinecek_urun['adi']} başarıyla silindi.")
                else:
                    print("Geçersiz ürün numarası.")
            elif secim == "3":
                print("Kantindeki öğrenciler:")
                for ogrenci in ogrenciler.values():
                    print(f"Ad: {ogrenci['ad']}, Soyad: {ogrenci['soyad']}, Okul No: {ogrenci['okul_no']}, Ayırtılan Ürün: {ogrenci['ayirttigi_urun']}")
            elif secim == "q":
                break
            else:
                print("Geçersiz seçim.")
    else:
        print("Hatalı giriş bilgileri.")

# Öğrenciye mesaj gönderme
def ogrenciye_mesaj_gonder():
    print("Öğrenciye Mesaj Gönderme")
    okul_no = input("Mesaj Göndermek İstediğiniz Öğrencinin Okul Numarasını Girin: ")
    if okul_no in ogrenciler:
        # Öğrenci bulundu, mesaj gönderme işlemi
        mesaj = input("Mesajınızı Yazın: ")
        dogrulama = input("Doğrulama Kodu: (Aq3Dv): ")
        
        
        if dogrulama == "Aq3Dv":
            ogrenci_mesajlari[okul_no] = mesaj.capitalize()  # Mesajı büyük harfle kaydetme
            print("Mesajınız Gönderildi.")
            
            # Log dosyasına giriş kaydı ekleme
            loga_kaydet("Mesaj", f"Öğrenci {okul_no}", mesaj)
        else:
            print("Geçersiz doğrulama kodu.")
    else:
        print("Öğrenci bulunamadı.")

# Müdüre gönderilen mesajları görüntüleme
def mudure_mesajlari_goruntule():
    print("Gelen Mesajlar:")
    for kullanici, mesaj in ogrenci_mesajlari.items():
        print(f"{kullanici}: {mesaj}")

# Müdüre mesaj cevapla
def mudure_mesaj_cevapla():
    okul_no = input("Cevap vermek istediğiniz öğrencinin okul numarasını girin: ")
    if okul_no in ogrenci_mesajlari:
        mesaj = input("Cevabınızı yazın: ")
        ogrenci_mesajlari[okul_no] = mesaj.capitalize()  # Mesajı büyük harfle kaydetme
        print("Mesajınız gönderildi.")

# Müdür girişi
def mudur_girisi():
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    sifre = input("Şifreniz: ")
    if ad == mudur_ad and soyad == mudur_soyad and sifre == mudur_sifre:
        print("Müdür olarak giriş yapıldı.")
        while True:
            print("1. Kantin Ayrılan Yemek")
            print("2. Gelen Mesajları Görüntüle")
            print("3. Mesajlara Cevap Ver")
            secim = input("Seçiminizi yapın (çıkış için 'q' tuşuna basın): ")
            if secim == "1":
                print("Kantinde ayrılan yemekler:")
                for ogrenci in ogrenciler.values():
                    print(f"Ad: {ogrenci['ad']}, Soyad: {ogrenci['soyad']}, Okul No: {ogrenci['okul_no']}, Ayırtığı Ürün: {ogrenci['ayirttigi_urun']}")
            elif secim == "2":
                # Gelen mesajları görüntüleme
                mudure_mesajlari_goruntule()
            elif secim == "3":
                # Mesajlara cevap verme
                mudure_mesaj_cevapla()
            elif secim == "q":
                break
            else:
                print("Geçersiz seçim.")
    else:
        print("Hatalı giriş bilgileri.")

# Ana menü
def ana_menu():
    print("1. Öğrenci Girişi")
    print("2. Kantinci Girişi")
    print("3. Müdür Girişi")
    print("4. Çıkış")
    print("5. Öğrenciye Mesaj Gönderme")
    print("6. Gizlilik Politikası")

# Ana menüye bu seçeneği ekleyin
while True:
    ana_menu()
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        ogrenci_girisi()
    elif secim == "2":
        kantinci_girisi()
    elif secim == "3":
        mudur_girisi()
    elif secim == "4":
        print("Çıkış yapılıyor...")
        break
    elif secim == "5":
        ogrenciye_mesaj_gonder()
    elif secim == "6":
        print("""
    Gizlilik Politikası:

    Uygulamada olan herhangi bir sorunun sorumluluğu kullanıcıya aittir. Oluşturma ekibi, herhangi bir sorunu kabul etmez. Herhangi bir sorun karşısında, sorunun kullanıcı kaynaklı olduğunu ve uygulama sahiplerinin bir kusuru olmadığını kabul edersiniz. Ayrıca, uygulamanın beta aşamasında olduğunu ve bu nedenle çeşitli sorunların, çökme ve istenilen şekilde çalışmama gibi durumların olabileceğini kabul edersiniz.

    Uygulamada güvenlik amacıyla IP adresi gibi kişisel bilgilerin toplandığını kabul etmiş olursunuz. Bu veriler süresiz olarak kayıt altına alınır ve içerisinde okul numarası, ad, soyad, telefon numarası, giriş şifresi, giriş tarihi gibi bilgiler bulunabilir. Uygulamaya giriş yapmak, kullanmak ve uygulamada dolaşmak bu verilerin işlenmesine, toplanmasına ve saklanmasına izin verdiğiniz anlamına gelir.

    Uygulamaya hasar vermek, yasaktır ve kullanıcılar bunun yasal olmadığını kabul ederler. (DDoS ve benzeri saldırılar, şifre kırma, başka hesaplara izinsiz erişim sağlama veya bu tür girişimler) Kullanıcılar, bunları yapmanın yasal olmadığını ve bunun sonuçlarından sorumlu olacaklarını kabul etmiş sayılırlar. Uygulama, okul kantini için yapılmış olup, harici kullanıma uygun değildir ve beta sürümündedir.

    Uygulamanın içeriği ve verileri, uygulama sahipleri tarafından istenildiği gibi değiştirme, silme ve kopyalama hakkına sahiptir. Uygulama içindeki verilerin kopyalanması, silinmesi ve çoğaltılması gibi işlemler uygulama sahipleri tarafından istendiği ölçüde yapılabilir.

    Gizlilik politikası yukarıdaki gibi açık ve nettir. Uygulama yapımcıları, hiçbir sorunu kabul etmez ve kullanıcılar bu politikayı kabul etmiş sayılırlar.
    """)
    else:
        print("Geçersiz seçim. Tekrar deneyin.")
