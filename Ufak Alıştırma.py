# liste = []
# for i in range (1,11):
#     liste.append(i)
#     print(i)

# [ilk önce ne istiyorum(karelerini yazmasını)/(sayıları bulacağı yeri tanımlıyorum)/koşullarımı koyuyorum]

# liste = [i for i in range(1,11)]
# print(liste)

# liste = []
# for i in range (1, 21):
#     if i %2 == 0:
#         liste.append(i)
#     else:
#         continue
# print(liste)

# liste = [i for i in range (1,21) if i %2 == 0]
# print(liste)

# cümle = str(input("Bir cümle giriniz: "))

# for i in cümle:
#     cümle_uzunluğu = len(cümle)
# print(f"Cümlenin karakter sayısı {cümle_uzunluğu} karakterdir.")

# cümle = "abifğpgkr"
            
# cümle_uzunluğu = [len(cümle) for kelime in cümle.split()]
# print(cümle_uzunluğu)

# liste = []
# for number in range (1,11):
#     liste.append(number*number)
# print(liste)

# liste = [number*number for number in range(1,11)]
# print(liste)

# liste = []
# for i in range (1,11):
#     if i %2 == 0:
#         liste.append(i*2)
#     else:
#         continue
# print(liste)

# liste = [i*2 for i in range (1,11)if i %2 == 0]
# print(liste)

# liste1 = [1,2,3,4]
# liste2 = [2,4,6,8]
# liste3 = []
# for i in liste1:
#     for j in liste2:
#         liste3.append(i*j)
# print(liste3)

# liste3 = [i*j for i in liste1 for j in liste2]
# print(liste3)

# cümle = str(input("Bir cümle giriniz: "))
# liste = []
# for harfler in cümle:
#     if harfler in 'aeıioöuü':
#         liste.append(harfler)
# print(liste)

# cümle = "deneme"
# liste = [harfler for harfler in cümle if harfler in 'aeıioöuü']
# print(liste)

# matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# liste = []
# for demet in matris:
#     for sayı in demet:
#         liste.append(sayı)
# print(liste)
    
# liste = [sayı for demet in matris for sayı in demet]
# print(liste)

# class kitaplar:
#     def __init__(self,isim,sayfa,yazar):
#         self.isim = isim
#         self.sayfa = sayfa
#         self.yazar = yazar
    
#     def bilgi(self):
#         return f"isim:{self.isim}, sayfa: {self.sayfa}, yazar: {self.yazar}"

# kitap1 = kitaplar("kkd",324,"okgeg")

# print(kitap1.isim)

# class kitap:
#     def __init__(self,ad, yazar, sayfa):
#         self.ad = ad
#         self.yazar = yazar
#         self.sayfa = sayfa
    
#     def bilgileri_goster(self):
#         return f"ad:{self.ad}, yazar: {self.yazar}, sayfa:{self.sayfa}"
    
#     def sayfa_arttir(self,ek_sayfa):
#         self.sayfa += ek_sayfa
#         return f"{self.sayfa} sayfa sayisi {ek_sayfa} kadar artirildi."
    
# kitap1= kitap("yüzük","fokf", 429)
# kitap2 = kitap ("heri", "jk", 344)

# kitap1.sayfa_arttir(100)
# print(kitap1.sayfa)

# class yayin:
#     def __init__(self,ad,yazar):
#         self.ad  =ad
#         self.yazar = yazar
#     def bilgileri_goster(self):
#         return f"ad:{self.ad}, yazar: {self.yazar}"
    
# class kitap(yayin):
#     def __init__(self, ad, yazar,sayfa):
#         super().__init__(ad, yazar)
#         self.sayfa = sayfa

#     def bilgileri_goster(self):
#         return f"kitap adı: {self.ad}, yazar: {self.yazar}, sayfa: {self.sayfa}"

# class dergi(yayin):
#     def __init__(self, ad, yazar,cilt, sayi):
#         super().__init__(ad, yazar)
#         self.cilt = cilt
#         self.sayi = sayi
    
#     def bilgileri_goster(self):
#         return f"dergi adı: {self.ad}, yazar: {self.yazar}, cilt: {self.cilt}, sayi: {self.sayi}"
    
# kitap1 = kitap("ye", "pegk" ,3583)
# dergi1 = dergi("bilim","tibtak",43,523)

# print(kitap1.bilgileri_goster())
# print(dergi1.bilgileri_goster())
