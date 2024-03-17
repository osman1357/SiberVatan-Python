class Person():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        print("person oluştu")
    def ben_kimim(self):
        print("ben kişiyim")
    
    
class Teacher(Person):                               #class x(y) yaptığımızda y nin içindeki özellikleri x içinde belirtmiş oluruz(miraz yolu)
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
        print("teacher oluşturuldu")
    def ben_kimim(self):
        print("ben öğretmenim")
        

class Student(Person):
    def __init__(self,fname,lname,number):
        self.number = number
        Person.__init__(self,fname,lname)
        print("student oluşturuldu")
    def ben_kimim(self):
        print("ben öğrenciyim")
    
    
p1 = Person(fname="osman",lname="gözel")
print(p1)

t1 = Teacher(fname="hulusi",lname="gözel",branch="sınıf öğrt")
print(t1)

s1 = Student(fname="talha",lname="kirendibi",number=1045)
print(s1)

p1.ben_kimim()
s1.ben_kimim()           #-------> overrading
t1.ben_kimim()

#---------------------------------------------------------------------------------------------------------------------------------------------------#

#SORU:dört işlem yapan classları yazınız 5 class olacak 1 super class 4 sub class toplama çıkarma çarpma bölme işlemleri miras alma yoluyla yapılacak

class Ana():
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def sonuc_bul(self):
        pass  
    
class Toplama(Ana):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
        (sayi1 + sayi2)                                                    #Benim yağtığım(Çalışmıyor)(4 super class var)
                             
class Cıkarma(Ana):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
        return(sayi1 - sayi2)

class Carpma(Ana):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
        return(sayi1 * sayi2)
        
class Bolme(Ana):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
        return(sayi1 / sayi2)

p1 = Ana(sayi1=10,sayi2=5)
print()

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

class Islem():
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def sonucu_bul(self):
        pass 
    
class Toplama(Islem):
    
    def sonucu_bul(self):
        return self.sayi1 + self.sayi2
    
class Cıkarma(Islem):
    
    def sonucu_bul(self):
        return self.sayi1 - self.sayi2
#                                                                                    Hocanın yaptığı
class Carpma(Islem):
    
    def sonucu_bul(self):
        return self.sayi1 * self.sayi2
    
class Bolme(Islem):
    
    def sonucu_bul(self):
        return self.sayi1 / self.sayi2

t1 = Toplama(sayi1=10,sayi2=5)
print(t1.sonucu_bul())

c1 = Cıkarma(sayi1=10,sayi2=5)
print(c1.sonucu_bul())

cc1 = Carpma(sayi1=10,sayi2=5)
print(cc1.sonucu_bul())

b1 = Bolme(sayi1=10,sayi2=5)
print(b1.sonucu_bul())

#------------------------------------------------------------------------------------------------------------------#

#SORU:3 class yazalım bir class aracın marka modelini bir class aracın mototr gücünü diğer class ise bu iki classtan miras alıp
#bu bilgileri bir method yardımıyla ekrana yazdırın

class Arac:
    def __init__(self,marka,model):
        self.marka = marka
        self.model = model
    def arac_bilgi(self):
        print(f"marka: {self.marka} model: {self.model} ")

class Motor:
    def __init__(self,motor_gucu):
        self.motor_gucu = motor_gucu
    def motor_bilgisi(self):
        print(f"motor gücü: {self.motor_gucu} ")

class Araba(Arac,Motor):
    def __init__(self,marka,model,motor_gucu):
        Arac.__init__(self,marka,model)
        Motor.__init__(self,motor_gucu)
    def araba_bilgi(self):
        self.motor_bilgisi()
        self.arac_bilgi()

araba = Araba("Mercedes","G 63","585 hp")
araba.araba_bilgi()

#--------------------------------------------------------------------------------------------------#

#SORU:istenilen satırda floyd üçgeni ekrana basacak fonksiyonu yazınız.

def floyd(satir):
    number = 1
    for i in range(1,satir+1):
        for j in range(1,i+1):
            print(number, end=" ")
            number +=1
        print()
satir = int(input("lütfen kaç satırlık bir floyd üçgeni istediğinizi belirtiniz: "))
floyd(satir)
