# OBJECT ORIANTED PROGRAMMING - NESNE YÖNELİMLİ PROGRAMLAMA
# tam olarak ne öğreneceğimi bilmiyorum ama kesinlikle beni bir basamak yukarı atlatacağına şüphem yok. başlayalım.

#CLASS: nesne yönelimli programlamanın en önemlisidir. her şey bunun üstünden dönüyor.
#ortak özellikleri olan nesneleri gruplandırmaya yarayan bir yapıdır.

#class nasıl oluşturulur?

"""
class calisan:                                                                                                                  #init burada başlat / oluştur anlamı taşıyor. 
    def __init__(self,name,surname,age):                                  
        self.name = name                                               #self burada benim calisan1 olarak belirlediğim değişkeni ifade ediyor. bunu python otomatik olarak initten sonra bir değişken başlatması zorunlu olduğundan sana veriyor bunu.
        self.surname = surname                                         #selfin (calisan1'in) age'i age olsun (= koyduk.) diyorum.
        self. age = age 
    def show_info(self):
        print(f"Ad:{self.name} Soyad: {self.surname} Yaş: {self.age}")                        #self yerine calisan1 gelecek.      
"""
"""calisan1 = calisan()"""
#bu şekilde çalıştırınca:

"""TypeError: calisan.__init__() missing 3 required positional arguments: 'name', 'surname', and 'age'"""
#hatası alıyorum. init benden name surname ve age için 3 tane arguments beklediğini söylüyor. bu yüzden içeriye değişken giriyoruz:

"""calisan1 = calisan("ali","veli",20)
print(calisan1.name, calisan1.surname, calisan1.age)"""
#ali veli 20 yazdı.

"""calisan2 =calisan("Ahmet","mehmet",25)
print(calisan2.name,calisan2.surname, calisan2.age)"""
#ahmet mehmet 25 geldi.

#yukarıdaki def show infoyu çalıştırmak için:

"""calisan1.show_info()"""
#calisan2 istiyosan calisan 2 yazman lazım mantıken:
"""calisan2.show_info()"""
#şöyle de çağırabilirim:
"""calisan.show_info(calisan2)"""
#ilk yazdığım tercih edilir genellikle.

#////////////////////////////////////////////////////////////////////////////////

#class variables - instance variables (sınıf değişkenleri ve nesne değişkenleri)

"""from datetime import date  #bunu sonralardan ekledik tam hakim değilim.

class calisan:
    zam_orani = 1.1
    personel_sayisi = 0
    def __init__(self,isim,maas):                                       #self oluşturduğun nesne demek. = ' den sonraki yazdığın da fonksiyonla gelecek olan kısım.
        self.isim = isim
        self.maas = maas
        calisan.personel_sayisi += 1                                    #calisan class ı içerisinde personel sayısı adında bir değişken var ve ben bunu bir artırmak istiyorum.

calisan1 = calisan("Ali", 5000) #bunlar instance variable olmuş oluyor.
calisan2 = calisan("Veli", 3750)                                        #class ımdan 2 tane nesne ürettim.
"""
"""print(calisan1.isim)"""  
#ali yazdırır
"""print(calisan2.maas)"""
#3750 yazdırır.

#dict = __dict__ yani. sahip olunan özellikleri sözlük olarak yazmasını sağlar.
"""print(calisan1.__dict__)"""
#{'isim': 'Ali', 'maas': 5000} olarak alırım.

#zam oranı eklemesini bunları yazdıktan sonra yapıyorum.
"""
print(calisan.zam_orani)
print(calisan1.zam_orani)
print(calisan2.zam_orani)
"""
#üçü de 1.1 verecektir.

#ama şöyle bir değişiklik yaparsak:
"""calisan.zam_orani = 1.2"""

#böylelikle en üstteki zam oranını değiştirmiş oluyorum ve üstteki üçlüyü tekrar yazdırdığımda sonuç 1.2 olacaktır.

#class ın kendi üzerinden değil de nesnenin kendisi üzerinden değişiklik yaparsam:
"""calisan1.zam_orani = 1.2  #1 olarak spesifikleştirdim.

print(calisan.zam_orani)
print(calisan1.zam_orani)
print(calisan2.zam_orani)"""
#1.1 
#1.2
#1.1 alırım. 

#personel sayısı eklemesini bundan sonra yapıyorum.
"""print(calisan.personel_sayisi)"""
#2 yazacaktır çünkü 2 calisan tanımladım.

#///////////////////////////////////////////////////////////////////////////////
#class methods - static methods - instance methods
"""
class kisi:
    kisi_sayisi = 0
    def __init__(self,isim,yas):
        self.isim = isim
        self.yas = yas
        kisi.kisi_sayisi += 1
    
    def bilgilerini_soyle(self): #Instance Method yazmış oldum.
        return f"ad:{self.isim} yas:{self.yas}"
    
    @classmethod #decorator oluşturdum! ve classmethod kullanmış oldum.
    def kisi_sayisini_soyle(cls):
        return cls.kisi_sayisi #cls burada fonksiyonu çağırırken kullandığımız class. 
    
    @classmethod
    def string_ile_olustur(cls,str): #class methodum cls'yi içine birinci parametre olarak otomatik bir şekilde alıyor. BU DURUM STATİC METHODDA FARKLI. parametre almak zorunda değil.
        isim,yas = str.split("-")
        return cls (isim,yas)  #ilk olarak bize bir string gelecek bilgi gelecek yani, geleni istediğimiz formata getirip yeni nesne oluşturacağız.
    
    @classmethod
    def dogum_yili_ile_olustur(cls,isim,dogum_yili):
        return cls(isim,date.today().year - dogum_yili)
    
    @staticmethod
    def dogum_yili_hesapla(kisi):
        return date.today().year - kisi.yas

"""
"""
kisi1 = kisi("ali", 21)
kisi2 = kisi("veli", 32)
kisi3 = kisi.string_ile_olustur("ayşe-25") #bu şekilde de kişi türetmiş olduk.
kisi4 = kisi.dogum_yili_ile_olustur("elif",1990)

"""

"""print(kisi1.bilgilerini_soyle())"""
#ad: ali yas: 21 çıktısı.

# classmethod eklemesinden sonra geliyor bu:

"""print(kisi.kisi_sayisini_soyle())"""
#2 veriyor. hepsini silince de 0 verir.
#kisi 3 eklemesinden sonra da sonuç 3 geliyor.
#kisi 4  eklemesinden sonra da sonuç 4 geliyor.

#@staticmethoddan sonra eklendi:
"""print(kisi.dogum_yili_hesapla(kisi4))"""
#1990 çıktısı.

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#inheritance - kalıtım 
#bu konu sayesinde class içerisinde alt classlar oluşturarak özelleştirmeyi sağlayacak, dolayısıyla kodumuzu kısa ve işlevli bir hale getireceğiz.
"""
class calisan:
    zam_orani = 1.1 #herkese 1.1 zam yapılıyor.
    def __init__(self,isim,soyisim,maas): #bu kısma ekstradan email eklemeye gerek duymuyorum çünkü emaili zaten nesnelerimden oluşturuyorum. ayriyeten bir email tanımlamama gerek yok.
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim+ "@sirket.com"
    def bilgileri_goster(self):
         return "ad:{} soyad:{} maas:{} email:{}".format(self.isim,self.soyisim,self.maas,self.email)
    
calisan1 = calisan("ali","caliskan",5000)
calisan2 = calisan("veli","uzun",6000)
"""
#şimdi yukarıdaki class'tan miras alan yeni bir subclass yani alt class oluşturup yeni özellikler tanımlayacağız. üsttekinden geldiği için aslında kalıtım miras anlamı taşıyor zaten.
"""
class yazilimci(calisan):   #parantez açtım çünkü bu class çalışandan miras alacak yani çalışanın da özelliklerini kapsayacak.
        def __init__(self, isim, soyisim, maas, bildigi_dil):
             super().__init__(isim, soyisim, maas)
             self.bildigi_dil = bildigi_dil
        zam_orani = 1.2
        def bilgileri_goster(self):
             return (f"ad: {self.isim}, soyad: {self.soyisim}, maas: {self.maas}, email: {self.email}, bildiği dil: {self.bildigi_dil}")
        def dilini_soyle(self):
             return f"bildiğim dil: {self.bildigi_dil}"

class yönetici (calisan):
    def __init__(self, isim, soyisim, maas,calisanlar = None):
          super().__init__(isim, soyisim, maas)
          if calisanlar == None:  #ben o parametre yerine herhangi bir şey girmediysem none olacak.
               self.calisanlar = []
          else:
               self.calisanlar = calisanlar
    def calisan_ekle(self,calisan):
         if calisan not in self.calisanlar:
              self.calisanlar.append(calisan)

    def calisan_sil(self,calisan):
         if calisan in self.calisanlar:
              self.calisanlar.remove(calisan)
    def calisanlari_goster(self):
         for calisan in self.calisanlar:
              print(calisan.bilgileri_goster())

yazilimci1 = yazilimci("ayşe","yıldız",7000, "python")    #yazılımcı classına hiçbir şey girmememe rağmen calisan classından geldiği için calisanda istenilen değerleri yazılımcı için de istiyor. (isim, soyisim, maaş)
yazilimci2 = yazilimci("fatma","ay",8000, "java")
"""

"""yonetici1 = yönetici("ali","metin",10000)

yonetici1.calisan_ekle(calisan1) #ali olan eklendi
yonetici1.calisan_ekle(yazilimci1) #ayşe olan eklendi
yonetici1.calisanlari_goster()"""

#ad:ali soyad:caliskan maas:5000 email:alicaliskan@sirket.com
# ad: ayşe, soyad: yıldız, maas: 7000, email: ayşeyıldız@sirket.com, bildiği dil: python
#sonucu geldi. ayırt edebilmek için yıldız atıyorum.

"""print("************")"""

"""yonetici1.calisan_sil(calisan1) #ali gitti
yonetici1.calisanlari_goster()"""
# ad: ayşe, soyad: yıldız, maas: 7000, email: ayşeyıldız@sirket.com, bildiği dil: python

"""yonetici2 = yönetici("feyyaz","beşiktaş",11000,[yazilimci1,yazilimci2,calisan1]) #calisanları ekledim.
yonetici2.calisanlari_goster()"""

# ad: ayşe, soyad: yıldız, maas: 7000, email: ayşeyıldız@sirket.com, bildiği dil: python
# ad: fatma, soyad: ay, maas: 8000, email: fatmaay@sirket.com, bildiği dil: java
# ad:ali soyad:caliskan maas:5000 email:alicaliskan@sirket.com
#çıktısı geldi.



"""print(calisan2.zam_orani)
print(yazilimci1.zam_orani)"""

#ikisinde de 1.1 yazıyor. yazılımcı classı şu durumda calisanla aynı. ama yazilimci kısmına farklı bir zam oranı tanımlarsam değişecektir. yazılımcı classına zam oranı eklemesini yapıyorum 1.2 olarak ve:
"""print(yazilimci1.zam_orani)"""
#1.2 yazdırmış oluyoruz.

#def bilgileri_göster eklemesinden sonra devam ediyorum:
"""print(calisan1.bilgileri_goster())"""
#ad:ali soyad:caliskan maas:5000 email:alicaliskan@sirket.com çıktısı.

"""print(yazilimci1.bilgileri_goster())"""
#yazilimci classında bilgileri göster şeklinde bir fonksiyon içermiyor ama calisanda olduğu için orada bulup çalıştırıyor. böylelikle calisandan miras almış oluyor.
#ad:ayşe soyad:yıldız maas:7000 email:ayşeyıldız@sirket.com çıktısı.

#yazılımcı classına return fonksiyonunu ekleyip string girdim ve tekrar çalıştırdığımda aldığım sonuç:

#ad:ali soyad:caliskan maas:5000 email:alicaliskan@sirket.com
#ben bir yazılımcıyım.

#yazılımcıdaki bilgileri_goster farklılığını fark etti ve ona göre çıktıyı değiştirdi.

#yazilimci için def init eklemesi yapıyorum, return ü kaldırıyorum. ekleme yaparken calisan için girdiğin değerleri birebir eksiksiz girmelisin. sırasını değiştirebilirsin ama genellikle kafa karıştırmaması için tercih edilmez.
#taba basınca hepsi geliyor zaten.

#ekstradan bildigi_dil ekledim ve tekrar yazdırdım:
"""print(yazilimci1.bilgileri_goster())"""

# ad:ali soyad:caliskan maas:5000 email:alicaliskan@sirket.com
# ad: ayşe, soyad: yıldız, maas: 7000, email: ayşeyıldız@sirket.com, bildiği dil: python çıktısı.

#------------------------ super() kullanımı -------------------
#kodu kısaltmaya, yukarıdaki kodu direkt olarak almaya yarıyor. mesela:
"""
def __init__(self, isim, soyisim, maas,bildigi_dil): 
             self.isim = isim
             self.soyisim = soyisim
             self.maas = maas
             self.email = isim + soyisim + "@sirket.com"
             self.bildigi_dil = 
"""
#bunlar zaten calisan classında var, sadece ekstradan bildiği dil i eklemek istiyorum. hepsini kopyala yapıştır yapabilirim ama bu direkt otomatik olarak atanıyor zaten. üstteki kod ile alttaki kod aynı işi yapıyor:

"""
def __init__(self, isim, soyisim, maas, bildigi_dil):
             super().__init__(isim, soyisim, maas)
             self.bildigi_dil = bildigi_dil
"""
#super burada üstten alıp parantez içindekileri direkt olarak getirmiş oluyor.
"""print(yazilimci2.bilgileri_goster())"""
#ad: fatma, soyad: ay, maas: 8000, email: fatmaay@sirket.com, bildiği dil: java

#def bildiğim dil eklemesi yaptım:

"""print (yazilimci1.bildigi_dil)"""
#pyhton çıktısı.

#üst kısım karışmış olabilir. burada listeliyorum:

#yönetici class'ını oluşturdum.
#calisan yoksa boş liste kalsın dedim
#calisan ekle'de calisan listede değilse ekle dedim.
#calisan sil' de calisan listedeyse kaldır dedim.
#en sonda da calisanları goster dedim. self,calisan yazmadım çünkü olanı istiyorum bir şey eklemicem etmicem.
#yönetici tanımladım
#yöneticiye calisan 1 ve yazilimci1  i atadım
#calisanları göster dediğimde calisanların bilgilerini görüntülüyorum.
#calisan ekledim ve görüntüledim.
#calisan sildim ve görüntüledim.
#yonetici2 oluşturuyorum.

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#dunder methods (magic methods)
#dunder = double underscore = __ = 2 alt çizgi
# __ içerenlerin ismi. arka planda gerçekleşen şeyleri ifade ediyor. örneğin:

"""print (3+5) 
print(int.__add__(3,5))"""
#aynı, 8 yani

"""print("ali"+"veli")
print(str.__add__("ali","veli"))"""
#aliveli

"""print([1,2,3]+[4,5,6])
print(list.__add__([1,2,3],[4,5,6]))"""
#[1, 2, 3, 4, 5, 6]

"""class mylist(list):
    pass

liste1 = mylist([1,2,3])
liste2 = mylist([4,5,6])

print(liste1 + liste2)"""
#[1, 2, 3, 4, 5, 6] çıktısı.
#pass i değiştirelim:

"""
class mylist(list):
    def __add__(self,other): #self 1. gönderdiğim, other ise 2. si. #listedeki sayıların alt alta toplanmasını (örneğin 1+4, 2+5 gibi) istiyorum. bunun için listedeki eleman sayılarının aynı olması gerekiyor ki açıkta sayı kalmasın.
        if len (self) != len (other): #eğer eşit değilse
            return f"bu elemanlar toplanamaz." #bunu yazdır
        else: #değilse
            result = mylist() #result adında nesne oluştur.
            for i in range (len(self)): #eleman sayısı kadar ziyaret etsin.
                    result.append(self[i]+ other[i]) #result'a appendle, ekle - self ve otherları. self[i] = ilk listenin ilk elemanı, other[i] = ikinci listenin ilk elemanı. 
        return result #result listesini döndür. Return Kullanımı: return, fonksiyonun çıktısını belirler ve fonksiyondan bir değer döndürüldüğünde, o değeri fonksiyonun çağrıldığı yere iletir. (gpt)

    def __sub__(self,other):
         if len(other) != len(self):
              return f"bu elamanlar cikartilamaz."
         else:
              results = mylist()
              for i in range (len(other)):
                   results.append(self[i] - other[i])
         return results          
            
    def __eq__(self,other):
         if sum(self) == sum(other):
              return f"birbirine eşitler."
         else:
              return f"birbirine eşit değiller."  

    def __abs__(self):
         result = mylist()
         for i in self:
              if i > 0 :
                   result.append(i)
              else:
                result.append(-1*i)
         return result

"""
              
             
            
    
"""liste1 = mylist([1, 2,-3])
liste2 = mylist([-4, 5,-6])"""

"""print(liste1 + liste2)"""
#[5, 7, 9]
#liste1'e 1 sayı daha ekledim çalıştırdım. değer adeti eşit olmadığından (ilk if) bu elemanlar toplanamaz yazdırdı.

#alta bir tane de __sub__ fonksiyonu oluşturdum.
"""print(liste1 - liste2)"""
#[-3, -3, -3]

#__eq__ = eşitklik methodu fonksiyonu ekledim.
"""print(liste1 == liste2)"""
#birbirine eşit değiller.

#mutlak değer =  __abs__ yazdık. #negatif sayılar koyduk ve pozitif yapmasını istedik.
"""print(abs(-2))"""
#2 sonucunu verir. mutlak değere çevirir içindekini. 
# ama liste için istiyorsam:
"""liste1 = mylist([1, 2,-3])
liste2 = mylist([-4, 5,-6])"""

"""print(abs(liste2))
print(abs(liste1))"""

# [4, 5, 6]
# [1, 2, 3]

#başka bir class oluşturalım.
"""
class futbolcu:
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas

    def __eq__(self,other):
        if self.isim == other.isim and self.soyisim == other.soyisim:
            return f"oyuncular birbirine esittir."
        else:
            return f"oyuncular birbirine esit değildir."

    def __add__(self,other):
        isim = self.isim[0]+other.isim[0]
        soyisim = self.soyisim[0] + other.soyisim[0]
        yas = self.yas + other.yas
        return futbolcu(isim,soyisim,yas)
    
    def __lt__(self,other):
        if self.yas < other.yas:
            return True
        else:
            return False
    
    def __gt__(self,other):
        if self.yas > other.yas:
            return True
        else:
            return False
""" 
"""
futbolcu1 = futbolcu("ali","veli",21)
futbolcu2 = futbolcu("hakan","metin", 14)
futbolcu3 = futbolcu1 + futbolcu2
"""
"""print(futbolcu1 == futbolcu2)"""
# oyuncular birbirne esit değildir.
#soyadı aynı yapıp printlersem oyuncular birbirine esittir der.

#toplama fonksiyonu ekledik. __add__

"""print(futbolcu3.isim)"""
#ah çıktısı

"""print(futbolcu3.soyisim)"""
#vm

"""print(futbolcu3.yas)"""
# 21+14. 35 yazdı ama direkt

#küçüktür methodunu ekledik. __lt__
"""print(futbolcu1 < futbolcu2)"""
#false

#büyüktür methodunu ekledik. __gt__
"""print(futbolcu2 > futbolcu1)"""
#false

#/////////////////////////////////////// DUNDER METHODS DEVAM AMA BU 2 Sİ İÇİN AYRI BİR BAŞLIK AÇIYORUM. ///////////////////////////////////
#__str__ ve __repr__

#__str__ = classtan ürettiğim nesnenin nasıl stringe dönüştürüleceği, yani printlediğimde ekrana nasıl yazılacağını gösteren fonksiyon.

#ufak bir farklılığını gösterelim:

"""a = "python" """

"""print(str(a))"""
#python yazarken:

"""print(repr(a))"""
#'python', kesmeli yazıyor.

#peki a sayı olsaydı?:
"""a = 2/11"""

"""print(str(a))"""
#0.18181818181818182

"""print(repr(a))"""
#0.18181818181818182

#fark etmedi.
#farklı şeyler deneyelim.

"""from datetime import date"""

"""bugun = date.today()"""
"""print(bugun)""" #2024-08-08 çıktısı.
"""print(str(bugun))""" #2024-08-08 çıktısı.  #kullanıcıya göstermek istediğin kısım için bu kulalnılmalı.
"""print(repr(bugun))""" #datetime.date(2024, 8, 8) çıktısı.   #yazılımcının kendisi için faydalı bir durum.

#ufak bir class ile anlaşılabilir yapalım.
"""
class futbolcu:
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
    
    def __str__(self): #sadece self yeterli oldu.
        return f"ad: {self.isim}, soyad: {self.soyisim} yas: {self.yas}"
    
    def __repr__(self):
        return f'futbolcu("{self.isim}","{self.soyisim}","{self.yas}")'
"""
"""futbolcu1 = futbolcu("ali","veli",20)"""

"""print(futbolcu1)"""
#<__main__.futbolcu object at 0x000001602AF90210> gibi alakasız bir şey verdi. #python bunu nasıl yazdıracağını bilemeyip adresini yazıyor.

#bundan kurtulmak için def __str__ eklemesi yapıyorum ve printlediğimde aldığım sonuç:
#ad: ali, soyad:veli 

#print fonksiyonu içerisindeki futbolcu1' e bakıyor ve nasıl yazması gerektiğini bilmiyor. bu yüzden class' a bakıyor. oradan str fonksiyonunu bulup oradan gelen değeri alıp ad soyad olarak yazmış oldu.
#kısacası ben "bu şekilde yazacaksın" diye fonksiyona yol göstermiş oluyorum.

#__repr__ ekleyelim.
#eklememe rağmen hala str çalışıyor. #str yi bulamadığı zaman repr çalıştırıyor.

#ekledikten sonra 2 farklı şekilde yazdırıyorum:

"""print(futbolcu1)""" #str için
#ad: ali, soyad: veli yas: 20 çıktısı.

"""print(futbolcu1.__repr__())""" #repr için:
#futbolcu(ali,veli,20) çıktısı aldık.

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#İLERİ DÜZEY FONKSİYONLAR - İÇ İÇE FONKSİYON KULLANIMI
#adı üstünde iç içe fonksiyon yazacağız.
"""
 def dis_fonksiyon():
         print("dis fonksiyon calisiyor.")
     def ic_fonksiyon():
         print("ic fonksiyon calisiyor.")
     print("dis fonksiyon sonlandı.")

dis_fonksiyon()""" #printle yazdırmıyorum diikkkaatt!!!
#dis fonksiyon calisiyor.
#dis fonksiyon sonlandı.
#çıktısı alıyorum.
#iç fonksiyonu yazdırmamasının sebebi yazdırmasını istememiş olmamız.o sadece o yazıyı oluşturuyor ama ekrana dökmüyor.
"""
def dis_fonksiyon():
    print("dis fonksiyon calisiyor.")
    def ic_fonksiyon():
        print("ic fonksiyon calisiyor.")
    ic_fonksiyon()
    print("dis fonksiyon sonlandi.")

dis_fonksiyon()"""
#dis fonksiyon calisiyor.
# ic fonksiyon calisiyor.
# dis fonksiyon sonlandi.
#böyle değiştirince oldu.
"""
def hesapla(sayi):
    if sayi == 1:
        return("1'in faktoriyeli mi var gerizekali")
    if sayi > 100:
        return("tamam bokunu cikarma da adam gibi sayi gir.")
    def karesinial(sayi):
        return sayi ** 2
    def kupunual(sayi):
        return sayi **3
    def karekokunual(sayi):
        return sayi ** 0.5
    def faktoriyelal(sayi):
        bunaugra = 1
        for i in range(1, sayi+1):
            bunaugra = bunaugra * i
        return bunaugra
    kare = karesinial(sayi)
    kup = kupunual(sayi)
    karekok = karekokunual(sayi)
    faktor = faktoriyelal(sayi)
    return f"sayinizin karesi {kare}, kupu {kup}, karekoku {karekok}, faktoriyeli {faktor} olmustur."

print(hesapla(85))
"""
#argsları da katacağız, ufak bir hatırlatma olsun.
"""
def toplamlaricarp(*args): # kaç tane sayı girileceğini bilmediğim ya da serbest bırakmak istediğim için args girdim.
    def toplama(demet): #toplama yazınca demet'i istesin benden. demet de zaten args'tan alacak args da bütün değerleri kapsıyor zaten.
        return sum(demet) #demeti toplam demet'e döndürmesini istiyorum.
    def carpma (demet): #carpma tahnımlıyorum ve demetten almasını istiyorum.
        carpim = 1 #bunu zaten tanımlıyorum her seferinde döngüde ziyaret edebilmesi için
        for i in demet:
            carpim *= i #i de değişken işte sayılar değiştikçe değişiyor. gelenlerle carpimi çarpıp eşitleyecek.
        return carpim #carpimi da çıkan sonuca benzetecek döndürecek yani
    return f"toplamları = {toplama(args)}, carpimlari = {carpma(args)}" #paranteze args yazmaliyim çünkü hangi sayıları kullanacak ne girildi bilmiyorum args'ta ne var ne yok direkt alsın işlem yapsın diye.
                                                                        # *args bir sürü parametre alıp demet olarak tutuyor. biz toplama işlemine demet gönderdik bir alım beklemiyoruz. bu yüzden yıldızsız args yazdık.
print(toplamlaricarp(2,3,4,5,6))
#toplamları = 20, carpimlari = 720 ciktisi.
"""
#////////////////////////////////////////////////////////////////////////////////////////////////////
 #fonksiyonları döndürme - ileri düzey fonksiyonlar
 #baya baya temelden gelerek ilerleyeceğiz.
"""
def fonk(x):
    return x*x
"""
"""a = fonk(3)
print(a)"""
#9 

"""b = fonk
print(b(5))"""
#25 olur.

"""
def islemsec(islem):
    def toplama(*args):
        toplam = 0
        for arg in args:
            toplam += arg
        return toplam           #return her zaman for döngüsü hizasında olmalı, yoksa çalışmaz ya da hata verir.
    def carpma(*args):
        carpim = 1
        for arg in args:
            carpim *= arg
        return carpim
    def ortalama(*args):
        return sum(args)/len(args) #herhangi bir değişken tanımlamama gerek olmadığı için direkt returnledim.

    if islem == "toplama":  #islem yerine islemsec yazdığım zaman print içerisindekiler için "object is not callable" hatası aldım. çağıramadı yani, bu yüzden ilk def'te parantez içerisine ne girdiysen onu gir. çünkü veriyi oradan çekecek.
        return toplama      #islemsec orada onu yazdığın zaman fonksiyonu çalıştıracağını ifade ediyor.
    elif islem == "carpma":
        return carpma
    elif islem == "ortalama":
        return ortalama

top_fonk = islemsec("toplama") #islemsec i tanımladığım için onu yazmasam da tanımladığım şeyi yazarak fonksiyonu yine çalıştırabiliyorum.
carp_fonk = islemsec("carpma") #fonksiyonu çalıştırmak için her zaman bir şeye tanımlamaya alış bir şeye dayandır yani, işini kolaylştırıyor.
ortalama_fonk = islemsec ("ortalama") #islemsec'in içine ortalama gönderildiğinde elde edilsin.
"""
"""
def kisisec(kisi):
    def takimsec(takim):
        return f"{kisi},{takim} takimini tutuyor."
    return takimsec

a = kisisec("ali")
b = kisisec("veli")

print(a("fenerbahçe"))
print(b("galatasaray"))

# ali,fenerbahçe takimini tutuyor.
# veli,galatasaray takimini tutuyor
"""
#///////////////////////////////////////////////////////////////////////////////////////////////
#FONKSİYONLARA PARAMETRE OLARAK FONKSİYON GÖNDERMEK
"""
def topla(x,y):
    return x+y
def carp(x,y):
    return x*y

def islemyap(fonk,a,b):
    return fonk(a,b)

print(islemyap(topla,3,5))
#8
print(islemyap(carp,3,4))
#12
"""
#islemyap parametresi göndermiş olduk.

#alttaki değerleri oluşturacak bir fonksiyon oluşturacağız.

#liste = [1,2,3,4,5,6,7,8]
#fonk = x * x
#sonuc = [1,4,9,16,25,36,49,64]

"""
liste1 =[1,2,3,4,5]
liste2 = [1,3,4,5,8,9,11]

def kareal(x):
    return x*x
def kupal(x):
    return x**3

def mapfonk(fonk,liste):
    sonuc = []
    for i in liste: #listeyle gelen bütün elemanları fonksiyona koyacak ve o fonksiyondan gelen sonucu sonuç listesini ekleyecek.
        sonuc.append(fonk(i))
    return sonuc

print(mapfonk(kareal,liste1))
#[1, 4, 9, 16, 25] çıktısı
print(mapfonk(kupal,liste2))
#[1, 27, 64, 125, 512, 729, 1331]
"""
#///////////////////////////////////////////
#PROPERTY, SETTER, DELETER DECORATOR

 #ilk olarak class oluşturalım
"""
class kisi:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
        #self.adsoyad = ad + " " + soyad
    
    @property

    def adsoyad(self):
        return f"{self.ad}{self.soyad}"
    @property
    def email(self):
        return f"{self.ad}{self.soyad}@sirket.com"
    
    @adsoyad.setter
    def adsoyad(self,isim):
        ad,soyad = isim.split (" ")
        self.ad = ad
        self.soyad = soyad
    @adsoyad.deleter
    def adsoyad(self):
        print("silindi")
        self.ad  = None
        self.soyad = None
"""
#bu eklemeyle tamamen düzeltmiş bulunuyoruz.        

"""
kisi1 = kisi("ali","veli")
kisi1.ad = "ahmet"
kisi1.adsoyad = "ayşe yıldız" #özellikmiş gibi yazdık ama bu bir özellik değil fonksiyon, methoddu, bunu setter decoratoru ile hallettik.
del kisi1.adsoyad
print(kisi1.ad)
print(kisi1.adsoyad)
print(kisi1.email) #emailin sonunda parantez var. çünkü üsttekiler kişi class ının özelliği olduğu için adını yazarak direkt erişebiliyorum ama email diye bir özellik yok bir metod (class'a ait fonksiyon) var. Anca çalıştırdığımda geliyor.
"""
# ali
# ali veli
# aliveli@sirket.com çıktısı

#kisi1.ad = ahmet eklemesi yapalım. yazdırıp farkı görelim
#ahmet
# ali veli
# ahmetveli@sirket.com                              #ad soyad değişmedi email değişti.

#selflerin hafızaları başka yerlerde olduğundan kaynaklanıyor.
#hepsinin değişmesi için def adsoyad eklemesi yapıp self.adsoyad'ı kaldırıyoruz. ve print kısmında adsoyad yanına () eklemesi yapıyoruz ve yazdırıyoruz:

# ahmet
# ahmetveli
# ahmetveli@sirket.com

# her ne kadar sonuca vsrsak da bu kullanım çok efektif değil. bunun yerine @property ekliyoruz ve adsoyad daki () 'i kaldırıyoruz. böyle de çalıştırabiliyoruz. () kaldırmazsan hata alırsın.
#email için de yapıyoruz.

#tam tersi olarak örneğin kisi1.adsoyad = "ali kısa" yazarsam hata alırım. bunun için de setter kullanacağız. nasıl kullanacağız şu şekilde: @adsoyad.setter ekliyorum. ve yine def yazıyorum, tanımlamak için de ayşe yıldız' ı ekliyorum.

#deleter için de del komutunu kullanmak yerine @adsoyad.deleter kullanacağım. yukarıya eklemesini yapıyorum. + del kisi1.adsoayad eklemesi yapıyorum.

#/////////////////////////////////////////////////////////////////////////
#değişkenlerin kapsama alanları - local ve global değişkenler

#bu değişkenleri kullanmaya başlamadan önce tanımlamalısınız.


"""x  ="globalx"""

"""def fonk():
    x ="localx" #bu x local bir değişkendir, yani sadece fonksiyondan erişebileceğiniz yerli bir değerdir. localx e #atıp bir daha yazdırsam ikisi de globalx olarak yazdıracak. fonksiyon içinde bulamayacağı için global yani tüm kod için geçerli olan x değerine gidecek.
    print(x)"""

"""fonk() #local x verir
print(x) #global x verir"""

"""x = "globalx"""

"""def outer():
    x = "enclosingx" #
    print(x)
    def inner():
        x = "localx"
        print(x)
    inner()

outer()
print(x)
"""
#enclosingx
# localx
# globalx çıktısı alıyorum. ilk olarak fonksiyonun en başından başlayarak fonksiyınu bitirene kadar iniyor, bittikten sonra dışarıdan alıyor. bu yüzden böyle bir sıralama oluşuyor.
# sadece x = "localx"'i kaldırırsam ilk olarak enclosingx daha sonrasında karşısına 2 defa print geleceği için 2 defa enclosingx yazdırıp fonksiyonu bitirecek. dışarı çıktığında tekrar yazdırmak istendiği için globax'i yazacaktır.
# enclosingx i kaldırırsam ilk printe denk geldiğinde henüz bir x tanımlamasına denk gelmediği için dışarıdan x çekecek ve global x i yazdıracak, sonra devam ettiğinde localx e denk geleceğinden onu yazdıracak, fonksiyondan çıktığında yine istediğim için yine globalx yazacaktır.
# sadece global x i bırakırsam kalanları kaldırırsam sadece global x yazdıracaktır 3 defa.

"""x = "globalx"

def fonk():
    global x
    x = 5

fonk()
print(x)"""
#globalx yazıyor. peki ben 5 yazdırmak istiyorsam ne yapacağım? global komutunu ekleyeceğim. ekledim
#yazdırınca artık 5 yazıyor
