#işime yarayabilecek birkaç fonksiyonu tespit ettim ve bunların kullanım şekillerini buraya not edeceğim. 
#kodları çalıştırmadan koymuyorum. hepsi çalışıyor ama karışmaması için hepsini diyez yapıyorum. işine yarayacak olanı çeker kullanırsın.

#FOR DÖNGÜSÜ:
    #işi otoamtikleştiren yapılardır.

"""

liste = [1,2,3,4,5,6]                                               
for blalba in liste:     #blalba yerine istediğini yazabilirsin.       
    print(blalba)

1
2
3
4
5
6

"""
"""
isim = "Ahmet"
for poefjreo in isim: #sallıyorum o kısmı gördüğün üzere
    print(poefjreo)

 A
 h
 m
 e
 t    

"""
#genelde i kullanılıyor

"""
demet = (1,2,3,4,5,6)
for i in demet:
    print(demet)    

# (1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)

"""

# sonucunu verirken: 

"""
demet = (1,2,3,4,5,6)
for i in demet:
    print(i) 

1
2
3
4
5
6

"""

#sonucunu veriyor.

"""
for i in range (0,10): 
    print(i)
1
2
3
4
5
6
0
1
2
3
4
5
6
7
8
9

"""
#belirlediğim 2 sayı arasındaki değerleri verir, ilk sınır dahilken ikincisi değildir.

"""
for i in range (1,17,2):
    print(i)
1
3
5
7
9
11
13
15

"""
#burada ise 3 değer girerek sıralama yaptırdım. sonuncu değer aralığımı belirtir.

"""
sonuc = 1
for i in range(0,10):
    sonuc *=2
    print(sonuc)

2 #2 üzeri 1
4  #2 üzeri 2
8       ...
16
32
64
128
256
512
1024    

"""    
#direkt olarak 2 üzeri 10 yazdırmak istersem printi döngüden çıkarmam yeterli olur. böylelikle her sayıyı dönmek yerine sadece sona geldiğimde çıktı elde etmiş olurum:

"""
sonuc = 1
for i in range(0,10):
    sonuc *=2
print(sonuc)

1024

"""
# iç içe for döngüleri yazacak olursam:

"""

liste1 = ["a","b","c"]
liste2 = [1,2,3]

for harf in liste1:
    for rakam in liste2:
        print(harf,rakam)

a 1
a 2
a 3
b 1
b 2
b 3
c 1
c 2
c 3

"""

#BREAK VE CONTINUE ANAHTAR KELİMELERİ

# continue anahtar kelimesini kullanarak listede istemediğim özel bir veriyi atlayabilirim. aşağıda 3 ü atladım mesela:

"""

liste=[1,2,3,4,5,6]

for i in liste:
    if i==3:
        continue
    print(i)

1
2
4
5
6

"""
#break koysaydım döngüyü iptal edecektim yani döngüden çıkacaktı:

"""

liste = [1,2,3,4,5,6]
for i in liste:
    if i==3:
        break
    print(i)

1
2

"""

#sonucunu alıyorum çünkü 3 ü break yazarak 3 ü görünce bırakmasını istedim.

"""

liste = range(100) ----> 0 dan 99 a kadarki olan tüm sayılar demek """

# 1'den 100'e kadarki olan sayılar içerisinde 3 e bölümünden kalan 0 değilse continue yani atla devam et, es geç, bunu yazma demek. bunu dediğimde geriye sadece 3 e bölündüğünde kalanı sıfır olan sayıları yazdırmış olacak:

"""

liste = range(100)
for i in liste:
    if i %3 != 0:
        continue
    print(i)

0
3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48
51
54
57
60
63
66
69
72
75
78
81
84
87
90
93
96
99

"""  
# ! yerine = koyarsam bu sefer tam tersi, çünkü 3 e bölündüğünde kalan sıfır olan sayıları yazma atla demiş oluyorum bu sefer. çok farklı olmadıkları için tekrar yazıp notu boşu boşuna uzatmıyorum. ama ufak bir ekleme yapacağız:

"""

liste = range(100)
for i in liste:
    if i %3 !=0:
        continue
    if i ==81:
        break   
    print(i)        #81 e geldiğinde döngüden çık demiş oluyorum.

0
3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48
51
54
57
60
63
66
69
72
75
78

"""

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

#WHİLE DÖNGÜSÜ: Belirli bir koşul sağlandığı sürece çalışan bir döngüdür.

"""
x = 2 

while x < 10:
    print(x)
    x +=1
print("x =" ,x)

2
3
4
5
6
7
8
9
x = 10 #sondaki printin içerisi bunu yazdırıyor.

"""
"""
x = 2
y = 3
while x * y<1000:
    print(x,y)
    x +=2
    y +=2  #x ile y nin çarpımı 1000 den küçükse yaz dedim, sonrasında iki ekleye ekleye yaptırdım. 1000 den büyük olmaya başlayınca yazmadı.
2 3
4 5
6 7
8 9
10 11
12 13
14 15
16 17
18 19
20 21
22 23
24 25
26 27
28 29
30 31

"""

"""
i = 1
while True:
    print(i)
    i +=1
    if i == 1000:
        break       #burada çalıştırırsan sonsuza kadar 1 ekleyerek yazar. sonlandırmak için:
#999 da durur. upuzun olmasın diye sonucu koymuyorum.

"""

#tek sayıları yazdırıyorum.
#değişkeni bir yerlerde değiştirmeyi (artırmayı, azaltmayı) unutma.

"""
i = 1
while True:
    if i %2==0:
        i +=1
        continue
    print(i)
    i +=1
    if i == 1000:
        break

"""
#999 a kadar yazdı.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////


#FONKSİYONLAR - FONKSİYON TANIMLAMA - DEF

#def  = fonksiyonu tanımlayacağımı belirttiğim anahtar kelime, bundan sonra gelecek olan şey benim fonksiyonumun tanımı olacaktır.

"""
def selamla():  #bundan sonra selamla yazmam print("Merhaba") ya denk olacak demek istiyorum.
    print("Merhaba")

selamla() #run dedim.
Merhaba

"""
#bir isim de eklemek istiyorum merhabanın yanına:

"""
def selamla(isim):
    print("Merhaba" + isim) #isim kısmına bir isim giriyorum.

def selamla(isim):
    print("Merhaba" + isim)

selamla(" Emir")

#Merhaba Emir

"""

"""
def topla(x,y):
    print(f"x + y = {x+y}")

topla(3,6)
x + y = 9

"""

#f koymazsan çalışmaz.

"""

def carp(x,y):
    print(f"x*y={x*y}")

carp(4,5)
x*y=20

"""
#sayıların ortalamasını hesaplayan bir fonksiyon oluşturalım.

"""

def ortalama_hesapla(liste):        #ortalama_hesapla yazdığımda listeyi çalıştırsın diyorum burada.
    toplam = sum(liste)         #SUM = TOPLAM
    adet = len(liste)           #LEN = LENGTH = UZUNLUK = ADET
    ortalama = toplam/adet          #tanımladıklarımla yapacağı işlem.
    print(f"girilen sayıların ortalaması: {ortalama}")

ortalama_hesapla([1,2,3,4,5,6,7]) #içerideki sayılarım liste oluyor ve çalıştırdığımda bunları hesaplıyor

girilen sayıların ortalaması: 4.0

"""

"""
#küçük harften büyük harfe çeviren bir fonksiyon örneği:

def buyuk_harfe_cevir(metin):
    metin = metin.upper()
    print(metin)

buyuk_harfe_cevir("hfl3rokf")

#HFL3ROKF

#sayı girersen hata alırsın çünkü integor yazmış oluyorsun ama string için bir komut girmiş oluyorsun.

"""
#bir fiyat ve indirim oranı verelim ve son indirimli tutarı hesaplayalım.

"""

def fiyat_hesapla(fiyat, yüzde):
    indirim = fiyat * yüzde/100
    son_fiyat = fiyat - indirim
    print(f"İndirimli tutar = {son_fiyat}")

a =200 
b =10 

fiyat_hesapla(a,b)

"""

#İndirimli tutar = 180.0

#mesela yüzde değerini vermediğimde sabit kabul edeceği bir yüzde değeri vermek istiyorum ki hata vermesin. bunun için de farklılık olarak:

"""

def fiyat_hesapla(fiyat, yüzde = 20):

"""

#eklemesi yapıyorum, böylelikle (200) girsem bile %20 indirim uygulayacak. yani parametreye varsayılan değeri atamış oluyorum.

#RETURN : 
        # pyhton' un herhangi bir değeri geri döndürmesine olanak tanıyor.

"""

def topla(x,y):
    print(x + y)

sonuc = topla(2,6)
print(sonuc)

8
None

"""

#yazdığımda 8 ve none şeklinde 2 sonuç alıyorum çünkü topla fonksiyonu çalışıyor ama sonucu yazdırdığımda bir şey yok elinde ondan none veriyor. ama return eklersem

"""

def topla(x,y):
    print (x + y)
    return x + y

sonuc = topla(2,6)

print(sonuc)

8
8
"""
#sonucunu alıyorum.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////


#LAMBDA FONKSİYONLARI: kodu kısaltmak için işe yarar, bunun sayesinde üstteki return'den bile kurtulacağız:

"""

def kare_al(x):
    return x * x
print(kare_al(5))

25

"""

#kare al şeklinde fonksiyon tanımlıyorum ve x değerini veriyorum. returnleyerek x * x i döndürmüş oluyorum. ama bu kodu şu şekilde de de elde edebiliyorum:

"""
kare_al = lambda x: x *x        # :' den önceki kısım fonksiyonun aldığı parametre, :' den sonra alacağı değer ise döndüreceği değer oluyor.
print(kare_al(4))

16

kup_al = lambda x: x **3         #---> üssü olarak değerler bu şekilde yazılıyor!
print(kup_al(6))

216

"""

#listedeki verileri ilk olarak harf sırasına göre daha sonrasında ise sayılara göre sıralayalım.

"""

liste =[("Ali",20),("Veli",42),("Emel",43), ("Hakan",20)]
liste.sort()                                                #buradan sortun sıralama için kullanılan bir komut olduğunu anlıyoruz.
print(liste)

"""

#[('Ali', 20), ('Emel', 43), ('Hakan', 20), ('Veli', 42)] sonucunu elde ediyoruz ve görüldüğü üzere alfabetik sıralamaya göre sıralanmış bir biçimde bir çıktı elde ediyoruz.

#peki bunu yaşlarına göre yani sayılara göre yapmak isteseydim?
 
"""

liste =[("Ali",20),("Veli",53),("Hakan",45),("Emel",69)]
liste.sort(key= lambda x : x[1])
print(liste)
                #burada key aslında içeriye bir fonksiyon tanımlamamı sağlıyor. ve lambda ile fonksiyonu tanımlıyorum. buradaki x dediğim şey aslında üstteki ali 20 yani ilk DEMETİM. 4 tane demete sahibiz. 
                # x[1] de 1. index yani 0 olan isim (ali), 1 olan ise sayılar. kısacası fonksiyonda anlatmaya çalıştığım şey x değerlerini 1 e bakarak sırala ve bunu döndür, sonra bana çıktısını ver.

#[('Ali', 20), ('Hakan', 45), ('Veli', 53), ('Emel', 69)]

"""
#soyada göre sıralamak istersem?

"""

liste2 = [{"Ad":"Ahmet","Soyad":"Calıskan","Yaş":25},{"Ad":"Mehmet","Soyad":"Uzun","Yaş":22},{"Ad":"Duru","Soyad":"Yıldız","Yaş":24},{"Ad":"Afife","Soyad":"Taşkesti","Yaş":52}]
liste2.sort(key= lambda x: x["Soyad"])
print(liste2)

#[{'Ad': 'Ahmet', 'Soyad': 'Calıskan', 'Yaş': 25}, {'Ad': 'Afife', 'Soyad': 'Taşkesti', 'Yaş': 52}, {'Ad': 'Mehmet', 'Soyad': 'Uzun', 'Yaş': 22}, {'Ad': 'Duru', 'Soyad': 'Yıldız', 'Yaş': 24}]
#istediğin şeyi örnneğin yaşa göre sıralamak istiyorsan yaş yazıp yazdırabilirsin.

"""

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

#HATA YAKALAMA - TRY VE EXCEPT BLOKLARI - 

#bu iki blok beraber çalışıyorlar. Öncelikle try komutunun içine istediğim kodu yazıyorum ve adı üstünde bunu denemesini istiyorum.
#daha sonrasında alt kısma except komutunu girerek bir şey yazdırıyorum ve şunu diyorum "üstteki kodda yazdığım harici bir durum varsa ya da hata oluşuyorsa excepte geç ve onu yazdır. eğer bir problem yoksa devam et."
#örnekleyelim:

"""

a = 5
b = 8
c = a/b
print(c)

try:
    a = 5
    b = 8
    c = a/b
except:
    print("bir hata oluştu")

print(c)

"""

#0.625 sonucunu alıyorum. çünkü try bloğunda hata oluşturabilecek bir durum görmediğinden excepti atlıyor. ama:

"""

try:
    a = 5
    b = 8
    c = a/b
    d = x #tanımlayamayacağı ve dolayısıyla hata vereceği bir değişken ekledim.
except:
    print("bir hata oluştu")
print(a,b,c,sep="-")

#bir hata oluştu
0.625           #sonucunu alıyorum. "bak burada bir hata var bunu yazıyorum ama işleme de devam ediyorum" diyor.
                #bu arada sep komutu çıktıların arasına koymak istediğin şeyi eklemeni sağlıyor. biz - koyduk. bu sefer de 5-8-0.625 sonucunu alıyoruz.

""" 
#kodun sonuna else: bloğu ekleyip örneğin print(else bloğu çalışıyor) tarzı bir ekleme yaparsan bunun çıktısını alman demek kodunda hata olmadığını gösteriyor demek.
#try da hata almazsan except çalışmaz ama else ve finally gibi bloklar çalışır. finally her türlü çalışır.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

#IF - ELSE - İS - ELİF

#aslında bildiğim şeyler ama bildiklerimin üstüne eklemeler yapacağım ve daha kapsamlı bir not defteri oluşmasını sağlamış olacağım.

"""
a=5
b=7
if a == b:          # == kullanmalısın evet.    # != eşit değildir demek oluyor.
    print("a=b")

"""

#buraya hiçbir şey yazmadı.
#if bloğunun koşulu doğru olunca yazıyor.

"""

a=5
b=5
if a!=b:
    print("a !=b")

"""

#yine sonuç alamayız, eşitler çünkü
#else için: kısacası eğer öyle değilse demek.

"""

a=6
b=8
if a==b:
    print("a=b")
else:
    print("a=!b")

"""

#a b ye eşite eşit yaz değilse eşit değil yaz diyorum. else i çalıştırırken if ile aynı hizada olmasına dikkat etmelisin.

#elif komutu da aslında ya öyle değil de böyleyse demek. bu yüzden yanına başka bir koşul yazman gerekiyor. örneğin:

"""

renk = "Siyah"
if renk=="Beyaz":
    print("Beyaz")  #eğer renk beyazsa beyaz yazdır.
elif renk==("Sarı"): #eğer renk beyaz değil de sarı ise sarı yazdır.
    print("Sarı")
elif renk=="Mavi":
    print("Mavi")
else:
    print("Hiçbiri") #hiçbiri olmazsa hiçbiri yazdır.

"""

#or komutuyla ilgili konuşalım. adı üstünde veya demek. if ile beraber kullanılıyor ve sunduğun iki koşuldan bir tanesi doğruysa onu doğru sanıyor:

"""

a = 5
b = 8
c = 10
if a<b or c ==a:
    print("koşul doğru")
else:
    print("koşul yanlış")

"""

#gördüğün gibi c a ya eşit olmamasına rağmen b a dan büyük olduğu için doğru sayıyor. ikisi de yanlış olsaydı else e geçecekti ve koşul yanlış yazacaktı.

#and bağlacında ise şöyle bir durum var. sunduğun seçeneklerin hepsinin doğru olması gerekiyor.

"""

a = 5
b = 9
c = 10
if a<b and c>a and b<a:
    print("koşul doğru")
else:
    print("koşul yanlış")

"""

#koşul yanlış yazacaktır çünkü sunduğum 3 seçenekten sonuncusu yanlış bir şey ifade ediyor.

#in anahtar kelimesi: yapının içerisinde bir şeyin varlığını kontrol etmeye yarıyor.

"""

liste = [1,2,3,4,5,6]

a=4
if a in liste: #eğer listenin içerisinde a varsa..
    print("listede var")
else:
    print("listede yok")

"""
#listede var diyor haliyle.

"""

isim = "Pyhton"
a = "p"
if a in isim:
    print("listede var")
else:
    print("listede yok")

"""

#buna listede yok der çünkü p ile P bir değil. python büyük harf küçük harfe dikkat eder.

#not anahtar kelimesi: var olan koşulu olumsuza çevirmeye yarıyor.

"""

a = 8
b = 10
if not a == b: # a==b değil ise demiş oluyorum dolayısıyla koşul doğru dönütünü alıyorum.
    print("koşul doğru")
else:
    print("koşul yanlış")

"""

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

# LİST COMPREHENSİON :
                    #  elimizdeki listeyi belirli kurallara göre yeni bir liste oluşturma yöntemidir. 

#olabildiğince eski ve yeni stil olarak kıyaslayacağız.

#liste oluşturmaya çalışalım.

#list3 = [ilk önce ne istiyorum(karelerini yazmasını)/(sayıları bulacağı yeri tanımlıyorum)/koşullarımı koyuyorum]


"""

numbers = [1,2,3,4,5,6,7,8,9]
list2 = []
for number in numbers:
    list2.append(number)
print(list2)

"""

#[1, 2, 3, 4, 5, 6, 7, 8, 9] sonucunu elde ediyorum. ama aynı sonucu şu şekilde de elde edebiliyorum:

"""

numbers = [1,2,3,4,5,6,7,8,9]

list3 = [number for number in numbers] #listeyi oluşturuyor, for döngüsüyle elemanları tek tek ziyaret ediyor ve oluşturduğu listeye ekliyor.
print(list3)

"""
#yine aynı sonuç.

#verilen listedeki rakamların karelerinden oluşan yeni bir liste oluşturalım. ilk olarak eski stilde gerçekleştirelim:

"""

numbers = [1,2,3,4,5,6,7,8,9]
list2 = []
for number in numbers:
    list2.append(number*number)
print(list2)

#[1, 4, 9, 16, 25, 36, 49, 64, 81] sonucunu elde ediyorum. ama şöyle de yapabiliriz:

list3 = [number*number for number in numbers]
print(list3)

"""
#yine aynı sonuç.

#listedeki çift rakamlardan bir liste oluşturalım.
"""

numbers = [1,2,3,4,5,6,7,8,9]
list2 = []
for number in numbers:
    if number %2 == 0:
        list2.append(number)
print(list2)

#[2, 4, 6, 8]

list3 = [number %2 == 0 for number in numbers]

"""
#aynı sonuç

#listedeki çift rakamların karesinden oluşan bir liste oluşturalım:

"""

list2 = []
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number %2 == 0:
        list2.append(number*number)
print(list2)

#[4, 16, 36, 64]

"""

#daha pratiği:

"""

numbers = [1,2,3,4,5,6,7,8,9]

list3 = [number * number for number in numbers if number %2 ==0]
print(list3)

"""

#listedeki 4'ten büyük sayıların karelerinden oluşan bir liste:

"""

numbers = [1,2,3,4,5,6,7,8,9]
list2 = []

for number in numbers:
    if number > 4 and number %2 == 0:
        list2.append(number*number)
print(list2)

#[36, 64]

"""

#yeni stil:

"""

numbers = [1,2,3,4,5,6,7,8,9]

#list3 = [ilk önce ne istiyorum(karelerini yazmasını)/(sayıları bulacağı yeri tanımlıyorum)/koşullarımı koyuyorum]

list3 = [number*number for number in numbers if number > 4 and number %2 ==0 ]

print(list3)

"""
#aynı sonuç.

#(1,a),(1,b),(1,c).. şeklinde bir liste oluşturalım.

"""

numbers = [1,2,3,4,]
letters = "abcd"

list2 = []

for number in numbers:
    for letter in letters:
        list2.append((number,letter))
print(list2)

list3 = [ (number,letter) for number in numbers for letter in letters ]
print(list3)

sonuç: [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd'), (3, 'a'), (3, 'b'), (3, 'c'), (3, 'd'), (4, 'a'), (4, 'b'), (4, 'c'), (4, 'd')]

"""
#birinci listede bulunup ikinci listede bulunmayan sayıların karelerinden oluşan bir liste oluşturalım.

"""

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,3,6,9,5]

list3 = []
for number in list1:
    if number not in list2:
        list3.append(number*number)

print(list3)

"""
#[1, 16, 49, 64] sonucunu elde ediyorum. daha kısa şekilde deneyelim:

"""                                                                                                                                               sep = "-" ---> maddeleri - ile ayırmak için kullanılır.

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,3,6,9,5]

list3 = [number*number for number in list1 if number not in list2]
print(list3)

"""
#aynı sonucu elde ediyorum.

#verilen listeden elemanları tek tek alıp [1,2,3,4,5,6,7,8,9,10,11,12] listesini oluşturalım.

"""

list1 = [[1,2,3,],[4,5,6,7],[8,9,10,11,12]]
list2 = []

for liste in list1:             #list1  in içindeki liste için diyorum ve o virgülden hemen önceki tanımlamış olduğum [1,2,3]'ü esas alıyor bu satırda.
    for sayı in liste:          #daha sonrasında liste içerisindeki sayıları almasını istediğim için [1,2,3,] içerisine girip oradaki değerleri sayı olarak tanımlamış oluyorum.
        list2.append(sayı)      #bu sayıları sıra sıra uğrayıp çekmesini ve list2 ye yazmasını istiyorum.
print(list2)

veya

list3 = [sayı for liste in list1 for sayı in liste] #sayı olarak tanımladığım şeyi yazdırmasını istediğimden ilk sayı yazdım daha sonrasında sayı olarak tanımladığım değerleri bulması için sırasıyla for döngüsü yazdım.
        #sağdan sola oku: sayı için listeye gitmek istiyorsan liste için list1 e git, baştaki sayı da dediğim gibi tanımlıyorsun.
print(list3)

"""
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

#ENUMERATE : NUMARALANDIRMAK

#liste içerisindeki elemanları numaralandırmak amacıyla kullanılıyor.

"""

enum = enumerate("Kadir Emir")
print(list(enum))

"""
#[(0, 'K'), (1, 'a'), (2, 'd'), (3, 'i'), (4, 'r'), (5, ' '), (6, 'E'), (7, 'm'), (8, 'i'), (9, 'r')] elemanları numaralandırdı.

#kadir emir'de k nin sırasını öğrenmek istiyorum:

"""

for index, harf in enumerate("Kadir Emir"): #index = sıralamak gibi düşün. örneğin k, 0. indekste deniyor. bu satırda da numaralandırılmış "kadir emir"'in içerisinde sayılarla sıralanmış harfler için: diyorum aslında.
    if harf =="k" or harf == "K":                
        print("{} harfi {}. sırada bulunmaktadır.".format(harf,index))
        break
        
"""
        #format komutuyla boşluklara hangi sırada nasıl yerleştireceğini ayarlıyorum. koymazsam çıktı alırım ama parantezleri dolduramayacağı için anlamsız bir çıktı olur. 
        #bunu sağladıktan sonra döngüden çıkmasını istiyorum.  çünkü istediğimi elde etmiş oluyorum. koymasam da oluyor. koymaya alış ama.
        # indexe de aşağıdaki sonuçts görebileceğin gibi 0 koyuyor.

#K harfi 0. sırada bulunmaktadır. sonucunu elde ediyorum.

#numaralandırılmasını istediğin stringin yanına girdiğin sayısal değer aslında girdiğin derğerden başlamasını istediğini ifade ediyor:

"""

enum = enumerate("kadiremir",4)
print(list(enum))                                                                                                   #tuple demet demek.

"""
#sadece print(enum dersen işine yaramayacak bir sayı dizisi çıkarır)
# sonuç: [(4, 'k'), (5, 'a'), (6, 'd'), (7, 'i'), (8, 'r'), (9, 'e'), (10, 'm'), (11, 'i'), (12, 'r')]


#BURAYA YOUTUBE'DA DİKKATİMİ ÇEKEN BİR ÇALIŞMAYI BIRAKMAK İSTİYORUM. 1 AYDAKİ 31 GÜNÜN HANGİ GÜNE DENK GELDİĞİNİ SÖYLEYEN PROGRAM YAZACAĞIZ.

"""

günler = ["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]

i = 0
while i < 7:
    print(günler[i], end=" ")
    j = i + 1
    while j <= 31:
        print(j, end= " ")
        j += 7
    i +=1
    print()

"""    

# Pazartesi 1 8 15 22 29 
# Salı 2 9 16 23 30
# Çarşamba 3 10 17 24 31
# Perşembe 4 11 18 25
# Cuma 5 12 19 26
# Cumartesi 6 13 20 27
# Pazar 7 14 21 28

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

#STRİNGLER - bir videodan hepsini değil, bilmediğimi düşündüğüm extra durumları ekleme yapacağım.

"""

print('Ali'nin evi)          #bu haldeyken olmaz ama:
print('Ali\'nin evi')           #yazarsam olur. \ burada kaçış karakteri olarak adlandırılıyor. ondan sonraki gelecek işaretin önemli olmadığını ve pas geçebileceğini gösteriyor.

"""
"""

print("""               #araya yazdığın alt alta kelimeler alt alta olarak çıktı verecektir.
""")

"""

#\n ----> yeni bir satır ekler, yani yukarıdakiyle aynı sonucu şu şekilde elde edebiliriz:
#\t -----> 1 tab a yani 7 karaktere tekabul eder.

"""
print("merhaba\ndünya")

"""
#merhaba        #şeklinde çıktı alırsın.
#dünya      

#bir stringten bir harfi çekmek istiyorum. haliyle bir indeks belirtmem gerekiyor. örneğin:

""" mesaj = "Merhaba" """
""" mesaj2 = "Dünya" """

""" print(mesaj[1]) """   #mesaj stringinin 1. indeksini yazdırıyorum. 0'dan başladığı için e 1. oluyor. ama işin ilginci şu:
""" print(mesaj[-2]) """  #bu sefer tersten ve 0 eklemeden sayarak 2. karakteri yazdırıyorum. bu durumda b harfini yazdırmış oluyorum.

#mesaj ı yazdırmak istiyorum ama tamamını istemiyorum:

""" print(mesaj[0:4])"""  #mesaj'ın 0 dahil 4 dahil olmamak üzere kısacası ilk 4 karakterini yazdırmış oluyorum: Merh çıktısı alıyorum.

#bir değeri ikişer veya üçer yazdırmak istiyorum:
""" print(mesaj[::2])"""  # : 'lar boş bırakılarak aslında en baş ve en son stringi kabul ettirdim. 2 de ikişer ikişer yazdırmamı söylüyor.
#Mraa 0,2,4 ve 6. karakterleri yazdı.

#tersten yazdıracağım:
""" (mesaj[::-1]) """  #abahreM

#büyük harflerle:
""" print(mesaj.upper())"""  #upper yanındaki boş parantezi unutma.

#bu şekilde geçici olarak büyük harfli bir çıktı elde edersin ama her printlediğinde her seferinde upper yazmak istemiyorsan:

""" mesaj = mesaj.upper() """   #olarak depolayıp daha sonrasında:
""" print(mesaj) """     #yazdırırsan sorun olmaz.

#birebir kullanımda harfleri küçültmek için de lower() kullanılıyor. daha fazla uzamaması için yazmıyorum.

#capitalize() = baş harfini büyütmek için kullanılıyor.

# .startswith("") metodu metnin girilen string ile başlayıp başlamadığını kontrol etmek için kullanılıyor.
""" print(mesaj.startswith("Me")) """
#True olarak çıktı alıyorum yani evet Me ile başlıyor diyor bana.

# .endswith("") te bitişi kontrol etmek için kullanılıyor.
""" print(mesaj.endswith("a")) """
#True

# len() ise karakter sayısını gösterir.
""" print(mesaj.__len__()) """  #veya:
""" print(len(mesaj)) """
#olarak kullanabilirsin.

""" print(len(mesaj + mesaj2)) """
#12 sonucu.

#format methodunun kullanımı:
#değişkenlerin yerlerini belirterek parantezleri doldurmuş oluyorum.

""" isim = "Ali" """
""" yaş = "20" """

""" print("{},{} yaşındadır".format(isim,yaş)) """
#Ali,20 yaşındadır

""" isim = "Ahmet" """
""" mesaj = "Merhaba" """

""" print("{}, {} dedi.".format(isim,mesaj)) """
#veya:
""" print(f"{isim}, {mesaj} dedi.") """
#Ahmet, Merhaba dedi.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

#INTEGER VE FLOAT FONKSİYONLARI:
        #integer = tam sayılar
        #float = ondalık sayılara karşılık geliyor.

#matematiksel işlemleri zaten biliyorsun +,-*,/ ama farklı olarak şunu göstermeliyim:
# // = tamsayı bölmesi, yani küsuratsız bölme sonucu veriyor:
""" print(16/3) """
#5.333333333333333 ama:
""" print(16//3) """
#sadece 5 yazıyor.

#yukarıda yazmıştım aslında ama tekrar olması açısından tekrar belirteyim:

# ** = üssü demek
""" print(3**4) """ 
# 3 üssü 4 = 81 yazdı.

#abs: mutlak değer demek
""" print(abs(-2)) """
#-2' nin mutlak değerini istedim 2 yazdı.

# round = yuvarlamak demek.
""" print(22/7) """
#3.142857142857143 yazdı. ama:

""" print(round(22/7)) """
#veya:
""" print((22/7).__round__()) """ 
#veya:
""" sayı1 = 22/7 """
""" print(round(sayı1)) """
#sadece 3 yazdırır.

#belirli bir küsüratı istiyorum:
""" print(round(22/7,2)) """
#veya:
""" print((22/7).__round__(2)) """
#veya:
""" sayı1 = 22/7 """
""" print(round(sayı1,2)) """
#bunların hepsi virgülden sonraki 2 rakamı yani 3.14'ü verir. dilediğin gibi 2 yerine istediğini yazabilirsin.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

#STRING VE INTEGERLARI BİRBİRİNE ÇEVİRME:

#integer yapmak istiyorsan yani yazılı bir değeri (string) sayısal yapmak istiyorsan "int" koyacaksın:

"""

sayı1 = "100"
sayı2 = 100
print(sayı1 == sayı2)

"""

#False dedi çünkü biri string biri integer. ama şöyle bir ekleme yapsam?:

""" sayı3 = int(sayı1) """
""" print(sayı2 == sayı3) """
#True alıyorum çünkü stringi integer yaptım.
#çevirmeye çalıştığın şeyin çevrilebilir olması önemli, her şey dönüşmez.

#ufak bir bilgilendirme:

""" i = 30 """
""" i /= 5 """
""" print(i) """ #i yi 5'e bölüyorum ve sonucu i ye eşitliyorum. yani aslında şununla aynı:

""" i = i / 5 """

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

#INPUT FONKSİYONU VE BİRKÇ ALIŞTIRMA ÖRNEKLER.
        #input fonksiyonu, ekranda kalacak ve bir giriş bekleyecek çıktılar oluşturmaya yarayan bir fonksiyondur.

""" 
sayı1 = input("Bir sayı giriniz: ")
print(sayı1)

"""
#terminalde Bir sayı giriniz: yazacak ve benden bir sayı bekleyecek. Sayıyı aldığında tekrar yazdıracak ve bitmiş olacak.

#ekrandan alınan bir sayının faktöriyelini hesaplayalım.

"""

sayı =int(input("Bir Sayı Giriniz: "))
faktöriyel = 1

for i in range (1, sayı+1):
    faktöriyel *= i
print(f"{sayı}! = {faktöriyel}")

"""

#ekrandan alınan bir sayının asal olup olmadığını kontrol edelim.

"""

sayi = int(input("Bir Sayı Giriniz: "))                                                                         

if sayi < 2:    
    print(f"{sayi} sayısı asal değildir.")
else:
    for burayaneistersemgirebiliyormuyumgercekten in range(2, sayi):
        if sayi % burayaneistersemgirebiliyormuyumgercekten == 0:
            print(f"{sayi} sayısı asal değildir.")
            break
    else:
        print(f"{sayi} sayısı asaldır.")

"""        

# Buradaki burayaneistersemgirebiliyormuyumgercekten aslında bir değişken adı. Programlamada, değişkenler bilgi saklamak için kullanılır. Genellikle i, j, k gibi kısa ve basit isimler kullanılır, ancak uzun ve anlamlı isimler de kullanabilirsiniz.

# Bu kodda, burayaneistersemgirebiliyormuyumgercekten değişkeni, 2'den başlayarak girdiğiniz sayıya kadar olan tüm sayıları sırayla temsil ediyor.

# İlkokul çocuğuna anlatır gibi açıklayacak olursak:

# Diyelim ki bir torbamız var ve içinde 2'den başlayarak sayınıza kadar olan sayılar var. Örneğin, sayı 10 ise torbada 2, 3, 4, 5, 6, 7, 8 ve 9 var.
# burayaneistersemgirebiliyormuyumgercekten bu torbadaki sayıları sırayla alıyor ve her seferinde sayınıza bölüp, kalan sıfır mı değil mi diye bakıyor.
# Eğer kalan sıfırsa, yani sayı tam bölünüyorsa, sayınız asal değil.
# Eğer hiçbiri tam bölünmezse, sayınız asal.


#ekrandan alınan bir sayının kaç tane pozitif tam böleni olduğunu hesaplayalım.

"""

sayı=int(input("Bir Sayı Giriniz: "))

bölensayısı = 0                                 #tanımladım
for i in range(1,sayı+1):                       # 1'den girdiğim sayının bir fazlasına kadarki aralıkta: (sayının 1 fazlası diyorum çünkü sayı kendisine de tam bölünüyor.)
    if sayı %i == 0:                            # girdiğim sayı, sayılar sırasıyla bölünürken kalan olmadığında yani sıfır olduğunda:
        bölensayısı = bölensayısı + 1           #bölen sayısını bir arttır.
print("{} sayısının {} tane tam böleni vardır.".format(sayı,bölensayısı))

"""
#örneğin 10 giriyorum, +1 eklediğimden 11 alıyor ve for döngüsü gereği 10 ile 1 i 10 ile 2 yi 3 ü 4 ü böyle böyle sırayla deniyor. 10 ile 10 u da deniyor ve devam ediyor.

#ekrandan alınan bir sayının rakamları toplamını hesaplayan bir program yazınız.

"""

sayı = (input("Bir Sayı Giriniz: "))

# Rakamların toplamını hesaplamak için değişken oluşturuyoruz.
rakamlar_toplami = 0

# Sayının her bir rakamını toplama ekliyoruz
for rakam in sayı:
    rakamlar_toplami += int(rakam)

# Sonucu ekrana yazdırıyoruz
print("Rakamların toplamı:", rakamlar_toplami)
        
"""
#ekrana yazılan 5 sayının en küçüğünü ve en büyüğünü ekrana yazdıran bir program yazınız.

"""

liste = []

for i in range (1,6):
    sayılar = input(f"{i}. sayıyı giriniz: ")
    liste.append(sayılar)

print(f"girilen sayılardan en küçüğü = {min(liste)}")
print(f"girilen sayılardan en büyüğü = {max(liste)}")

"""

#ekrandan alınan sayının herhangi bir sayının karesi olup olmadığını kontrol edelim.

"""

sayı = int(input("Karesinin Kontrol Edilmesini İstediğiniz Sayıyı Giriniz: "))

for i in range(1, sayı):
     if i*i == sayı:                                                #HİÇ BAKMADAN KENDİM YAZDIM!!!!!
        print (f"{i}² = {sayı}")
        break
else:
    print(f"{sayı}, herhangi bir sayının karesine eşit değildir.")

"""

#ekrandan alınan bir metinde hangi harfin kaç kere kullanıldığını yazan bir program oluşturalım.

"""

metin = str(input("Bir Metin Giriniz: "))
sözlük = {}

for harf in metin:
    if harf in sözlük:
        sözlük[harf] +=1
    else:
        sözlük[harf] = 1
for harf,adet in sözlük.items():
    print(harf, adet)

"""

#ekrandan alınan bir metinde a harflerini büyük yapan bir program yazınız. bu sefer kendimi denemek adına list comprehension ile yazdım. (yazamadım :/ )

"""

metin  =str(input("Bir Metin Giriniz: "))
yenimetin = "".join([harf.upper() if harf == "a" else harf for harf in metin])
print(yenimetin)

"""
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

#JOIN KOMUTU:
    #stringleri birleştirmeye yarar.

"""

kelimeler = ["python", "öğrenmek", "bir", "inşaat mühendisliği", "2. sınıf", "öğrencisi", "için", "gerçekten","çok zor."]
cümle = "" #boşluk verirsem "" arasına, cümle bir boşluk ile başlıyor. o "" sadece cümlenin temelini oluşturmuş oluyor.

for kelime in kelimeler: #kelimeler listesindeki içerikler (ki ben kelime diye adlandırdım) için:
    cümle += kelime.capitalize() + " " #cümle ekle ve eşitle(+=) oradaki içerikleri yani kelimeyi ekle sonra boşluk ekle sonra diğer içeriğe geç sıra sıra döndür.
print(cümle) #sonucu yazdır.

"""
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

#ARGS VE KWARGS KULLANIMI:
#bazen fonksiyon tanımlarken içerisine ne kadar değişken gireceğimi bilemiyorum ya da çok fazla girmem gerekebiliyor veya farklı farklı sürekli tanımlama yapmam gerekiyor. bundan kurtulabilmek için args kullanıyoruz.
#dolayısıyla istediğim kadar değer gönderebilirim.
#arguments kelimesinin kısaltılmışıdır.

#mesela:

#def carp (x,y,z,t,...) yerine:

"""

def çarp(*args): #çarp yazdığımda aşağıdakileri yap diyorum ve çarp' ın içine gireceğim değerleri args olarak tanımlıyorum.
    çarpım = 1   #böyle bir değişken oluşturuyorum.
    for arg in args: #args içindeki değerler için:
        çarpım *= arg # sırayla ziyaret et çarpım ile yani 1 ile çarp sonucu da çarpıma eşitle
    return(çarpım) #çarpımı döndür

print(çarp(2,3,4))

"""
#ortalama hesaplayalım.

"""

def ortalama (*args):
    return sum(args) / len(args)        # çeviriyorum, returnlüyorum. neye? girdiklerimin toplamı/girdiklerimin sayısına

print(ortalama(6,8))

"""

"""

def selamla(mesaj, *args):  #selamla'yı içine mesaj ve virgülden sonra değişik ve sınırsız parametreler alacak şekilde tanımlıyorum.
    sonuç = ""              #sonuç adında boş bir string tanımlıyorum. yazı yazabileceğim bir alan olmalı.
    sonuç += mesaj          #selamla' nın içerisine yazılan mesajı sonuç' a eklemesini söylüyorum
    sonuç += " "            #ekledikten sonra da boşluk vermesini istiyorum.
    for i in args:          #args kısmına kaç tane değişken girdiğim belli olmadığı için args içerisindeki girilmiş bütün değerleri ziyaret etmesini ve:   
        sonuç += i          #neye denk geliyorsa da sonuç'a eklemesini istiyorum.
        sonuç += " "        # daha sonra da boşluk vermesini istiyorum.
    return sonuç            # bu aşamalar başarılı olduktan sonra çıktı alabilmek için sonuç'un geldiği hale döndürüyorum ve çıktıyı elde ediyorum.

print(selamla("merhba","ali","nabr"))

"""
#videodaki örnekler bu kadardı da ben yapay zekadan örnek alıp buraya daha fazla örnek ekleyeceğim.

"""

def topla(*args):
    sonuç = 0    #buraya sonuç = "" yazarsam bir string gireceğimi düşünür. ama topla diyerek sayı yani integer giriyorum bu yüzden şöyle bir hata alıyorum: TypeError: can only concatenate str (not "int") to str
    for arg in args:        #yazıyla ilgili bir şey gireceksem "" kullanmalıyım ve her seferinde bir şey tanımlayarak başlamayı akıl etmeliyim.
        sonuç += arg        # çünkü args'tan çektiğim bilgileri yazabileceğim ve çıktı alabileceğim bir değişken olması şart.
    return sonuç
print(topla(2,5,6))

"""
# bir şeyleri birleştireceğim:

"""

def birlestir (*args):
    liste = ""          #bu sefer isimleri birleştireceğim yani string gireceğim için "" koydum.
    for arg in args:
        liste += str(arg)
    return(liste)

print(birlestir("2","3","5"))

"""
# en büyük sayıyı bulduralım:
"""

def sayılar (*args):
    liste = ""
    for arg in args:
        liste += str(arg)
    return (liste)

def enbüyüksayı(*args):
    return(max(int(arg)for arg in args))

print(enbüyüksayı(2,434,674363))

"""
#args ı normal parametrelerle beraber kullanma:

"""

def öğrenciçağır (okulismi,*öğrenciler):
    print(f"{okulismi} okulunun öğrencileri: ")
    for öğrenci in öğrenciler:
        print(öğrenci)

öğrenciçağır("osmangazi ortaokulu", "mehmet")

"""
#ortalama hesabı:

"""

def notlar(*args):
    return sum(args)/len(args)
print(notlar(2,3,5))

"""

#KWARGS:
#keyword argument
#girdiğim argumentleri sözlük olarak saklamama yarıyor kwargs.

"""

def fonksiyon(**kwargs):
    print(kwargs)

fonksiyon(ad ="ali", soyad ="çalışkan", yaş = "45")

"""

"""

def fonksiyon2(zorunlu,*args,**kwargs):
    print(zorunlu)
    print("***********")
    for arg in args:
        print(arg)
    print("*************")
    for kwarg in kwargs:
        print(kwarg)

fonksiyon2(2,3,4,5,6,7,ad = "ali", yaş = 23)

2
***********
3
4
5
6
7
*************
ad
yaş

"""

#cevabı incelediğimizde ilk virgülden önceki kısmın zorunluya, daha sonrakilerilerin keyworde yani stringe denk gelene kadar argsa, keywordler başlayınca da kwargssa geçtiğini görebiliyoruz.
#ama sadece keyleri yani ad ve yaş yazdı. bunu değiştirmek için:

"""

def fonksiyon2(zorunlu,*args,**kwargs):
    print(zorunlu)
    print("***********")
    for arg in args:
        print(arg)
    print("*************")
    for k,v in kwargs.items():
        print(k,v)

fonksiyon2(2,3,4,5,6,7,ad = "ali", yaş = 23)

2
***********
3
4
5
6
7
*************
ad ali
yaş 23

"""

#bu sefer hepsini yazdırdım. k = key ve v = value(girilen değer) oluyor.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////\\\\\\\\\\\\\\\\\/////////////////////////////////

    



























































































































