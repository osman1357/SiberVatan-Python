Ad = ("Osman")
Soyad = ("Gözel")
Yas = ("16")
#print("Benim adım",Ad,Soyad)("yaşım",Yas,"Hoşgeldin")    #Bakılacak

karsilama = 'Benim adım '+ Ad + ' ' + Soyad + ' '+ 'yaşım ' + str(Yas) + ' Hoşgeldin'     #Doğrusu
#print(karsilama)

uzunluk = len(karsilama)        # len kalıbı sayı sayarken
#print(uzunluk)

#print(karsilama[3])              # [x] cümledeki x. karakteri gösterir

#print(karsilama[-1])             # [-x] cümledeki sondan x. karakteri gösterir

#print(karsilama[4:21])           # [x:y] cümlede x ile y arasın      -> Bakılacak

#print(karsilama[:21])            # [:x] cümlede x. harfe kadar yazar

#print(karsilama[21:])            # [x:] cümlede sondan x. harfe kadar yazar

#print(karsilama)                 # "benim adım osman gözel yaşım 16 hoşgeldin" yadır

#print(karsilama[2:25:3])         # [x:y:z] x ile y arasında her z basamakta bi yaz

#print(karsilama[:-4])            # [:-x] cümleyi yazar fakat sondan x kadar harf yazmaz

#print(karsilama[::-2])    # [::-x] cümleyi ters yazar (1 veya -1 yazarsan) eğer (-2 ...) olursa ters her x sayıdan atlaya atlaya yazar

karsilama_upper = karsilama.upper()      # Hepsini Büyük Yazma
#print(karsilama_upper)

karsilama_lower = karsilama.lower()      # Hepsini Küçük Yazma
#print(karsilama_lower)

karsilama_strip = karsilama.strip()      #cümleyi yazdırır
#print(karsilama_strip)

karsilama_split = karsilama.split()      # cümlede seçtiğin kelimeyi yadırır x_split[5] = 16 (5. kelime 16)
#print(karsilama_split)
#print(karsilama_split[5])

karsilama_join = "-".join(karsilama)     #kelimelerin arasına "x" (tırnak içine konulan x leri harflerin arasına koyar)
#print(karsilama_join)

karsilama_find = karsilama.find("osman")                #
#print(karsilama_find)

karsilama_startswith = karsilama.startswith('A')        #cümlenin başı 'A' ile mi başlıyor diye soruluyor
#print(karsilama_startswith)

karsilama_endswith = karsilama.endswith('n')            #cümlenin sonu 'n' ile mi bitiyor diye soruluyor
#print(karsilama_endswith)

karsilama_replace = karsilama.replace ('Osman','Gözel') # 2. yazılan kelime 1. yazılan kelimenin yerine koyuyor (kelimeyi değiştiriyor)
#print(karsilama_replace)



