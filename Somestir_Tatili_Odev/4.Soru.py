#İki string'i birleştirin ve ardından bir substring arayın ve konumunu bulun.

cumle1 = input("lütfen bir cümle girin: ")
cumle2 = input("lütfen bir cümle girin: ")
aranan = input("lütfen aramak istediğiniz substringi girin: ")
cumle3 = (cumle1 + ' ' + cumle2)
konum = cumle3.find(aranan)
konum = str(konum)
    
if aranan in cumle3:
    print("Cümle içinde aradığınız substring mevcut")
else:
    print("Lütfen geçerli bir substring girin")
