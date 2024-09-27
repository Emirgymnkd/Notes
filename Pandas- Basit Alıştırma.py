"""import pandas as pd

data_sample = {"Employee":["John","Alice","Bob","Eve","Charlie","Dave"],
               "Department":["HR","IT","IT","HR","IT","HR"],
               "Salary":[50000,70000,80000,60000,75000,55000],
               "Bonus":[5000,7000,8000,6000,7500,5500],
               "Location":["New York","San Fransisco","New York","Chicago","Chicago","New York"]}

dataframe_sample = pd.DataFrame(data_sample)
total_sales_it_bonus_compensation = dataframe_sample[dataframe_sample["Department"]=="IT"][["Salary","Bonus"]].sum().sum()

print(total_sales_it_bonus_compensation)"""

#247500

#////////////////////////////////////////////////////
"""import pandas as pd

data_sample = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05", "2024-01-06"],
    "Product": ["Widget A", "Widget B", "Gadget C", "Widget A", "Widget B", "Gadget D"],
    "Category": ["Alpha", "Beta", "Gamma", "Alpha", "Beta", "Gamma"],
    "Sales": [120, 300, 180, 150, 220, 250],
    "Profit": [30, 70, 40, 50, 60, 80],
    "Region": ["North", "South", "East", "West", "North", "South"]
}

dataframe_sample = pd.DataFrame(data_sample)


filtered_data = dataframe_sample[(dataframe_sample["Region"] == "North") & (dataframe_sample["Category"] == "Alpha")]


total_sales_north_alpha = filtered_data["Sales"].sum()
total_profit_north_alpha = filtered_data["Profit"].sum()

print("Toplam Satış:", total_sales_north_alpha)
print("Toplam Kâr:", total_profit_north_alpha)"""

#/////////////////////////////////////////////////////////
"""
import pandas as pd
data_sample ={
    "Şirket Adı": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"],
    "Yıl": [2019, 2019, 2019, 2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022, 2023, 2023, 2023],
    "Gelir": [100000, 200000, 300000, 110000, 210000, 310000, 120000, 220000, 320000, 130000, 230000, 330000, 140000, 240000, 340000],
    "Gider": [50000, 150000, 350000, 55000, 155000, 355000, 60000, 160000, 360000, 65000, 165000, 365000, 70000, 170000, 370000],
    "Net Kar": [50000, 50000, -50000, 55000, 55000, -45000, 60000, 60000, -40000, 65000, 65000, -35000, 70000, 70000, -30000]}

dataframe_sample = pd.DataFrame(data_sample)
dataframe_sample_filtered = dataframe_sample[(dataframe_sample["Yıl"]>=2019) & (dataframe_sample["Yıl"]<=2023)]     # and yazdım & yerine hata aldım. pandasta & kullanmalısın.
net_kar_sum = dataframe_sample_filtered.groupby("Şirket Adı")["Net Kar"].sum() #ilk neyi, sonra neye göre filtreleyeceğimi yazıyorum. () = içerisinden [] = buna göre diyorum.
pozitif_net_kar = net_kar_sum[net_kar_sum > 0]                                  #sum ()' da () = fonksiyonu çağırıyorum kısacası. çalıştırılması gerektiğinde koyman şart.
print(pozitif_net_kar)  
"""
#///////////////////////////////////////////////////////////////
"""
import pandas as pd
data_senaryo = {
    "Ürün Kodu": ["P001", "P002", "P003", "P004", "P005", "P006"],
    "Kategori": ["Elektronik", "Ev Aletleri", "Elektronik", "Mobilya", "Elektronik", "Ev Aletleri"],
    "Fiyat": [150, 250, 180, 300, 120, 90],
    "Stok Durumu": ["Evet", "Hayır", "Hayır", "Evet", "Hayır", "Evet"],
    "Satış Adedi": [60, 40, 70, 20, 90, 55]
}

dataframe_senaryo = pd.DataFrame(data_senaryo)
dataframe_filtered = dataframe_senaryo[(dataframe_senaryo ["Fiyat"] > 100) & (dataframe_senaryo ["Fiyat"] < 200) & (dataframe_senaryo ["Satış Adedi"] >= 50) & (dataframe_senaryo ["Stok Durumu"] == "Hayır")]
toplam_satis_geliri = dataframe_filtered["Fiyat"] * dataframe_filtered["Satış Adedi"] #çarpma da böyle yapılıyor, tek tek yazacak, exact konumunu belirteceksin.
print(toplam_satis_geliri)
"""
#//////////////////////////////////////////////////////////////
#bir sonraki örneğe geçmeden önce zaman ile ilgili kütüphaneyi bir gözden geçirelim:
"""
from datetime import datetime, timedelta

# Geçerli tarihi alıyoruz
current_date = datetime.now()

# Bir yıl öncesine gitmek için 365 gün çıkarıyoruz
one_year_ago = current_date - timedelta(days=365)

# Örneğin, 30 gün önceyi hesaplama
thirty_days_ago = current_date - timedelta(days=30)

# Bu tarihlerden biri ile işlem yapma
print("Bugünkü tarih:", current_date)
print("Bir yıl önceki tarih:", one_year_ago)
print("30 gün önceki tarih:", thirty_days_ago)

#bunu her zaman bu şekilde kullanabilirsin.
"""
"""
import pandas as pd
from datetime import datetime, timedelta

# Geçerli tarihi al ve bir yıl öncesine git
current_date = datetime.now()
one_year_ago = current_date - timedelta(days=365)

# Örnek veri oluşturma
data = {
    "Müşteri ID": ["M001", "M002", "M003", "M004", "M005", "M006", "M007", "M008", "M009", "M010"],
    "Satın Alım Tarihi": [
        current_date - timedelta(days=30) , current_date - timedelta(days=200), #30 gün önce diyorum ilkinde, diğerinde 200 gün önce diyorum.
        current_date - timedelta(days=400), current_date - timedelta(days=10),
        current_date - timedelta(days=50), current_date - timedelta(days=300),
        current_date - timedelta(days=90), current_date - timedelta(days=150),
        current_date - timedelta(days=60), current_date - timedelta(days=250)
    ],
    "Ürün Kategorisi": ["Elektronik", "Giyim", "Elektronik", "Mobilya", "Elektronik", "Gıda", "Elektronik", "Elektronik", "Giyim", "Elektronik"],
    "Harcanan Tutar": [1500, 200, 2500, 1000, 3000, 50, 500, 700, 120, 1500],
    "Sadakat Puanı": [150, 20, 250, 100, 300, 5, 50, 70, 12, 150] }

dataframe = pd.DataFrame(data)
kriter = dataframe[(dataframe["Satın Alım Tarihi"]> one_year_ago) & (dataframe["Ürün Kategorisi"] == "Elektrik")]
sadakat = dataframe.groupby("Müşteri ID")["Sadakat Puanı"].sum()
ilk5musteri = sadakat.nlargest(5) #bu sekilde kullaniliyor.

print(ilk5musteri)
"""
"""
import pandas as pd
from datetime import datetime, timedelta

# Geçerli tarihi al
current_date = datetime.now()

# Farklı bir senaryo için yeni bir örnek veri oluşturma
data = {
    "Müşteri ID": ["M011", "M012", "M013", "M014", "M015", "M016", "M017", "M018", "M019", "M020"],
    "Satın Alım Tarihi": [
        current_date - timedelta(days=40),  # 40 gün önce
        current_date - timedelta(days=180), # 180 gün önce
        current_date - timedelta(days=300), # 300 gün önce
        current_date - timedelta(days=5),   # 5 gün önce
        current_date - timedelta(days=80),  # 80 gün önce
        current_date - timedelta(days=270), # 270 gün önce
        current_date - timedelta(days=120), # 120 gün önce
        current_date - timedelta(days=140), # 140 gün önce
        current_date - timedelta(days=90),  # 90 gün önce
        current_date - timedelta(days=220)  # 220 gün önce
    ],
    "Ürün Kategorisi": ["Mobilya", "Elektronik", "Gıda", "Elektronik", "Elektronik", "Giyim", "Elektronik", "Mobilya", "Gıda", "Elektronik"],
    "Harcanan Tutar": [2000, 2500, 500, 3000, 1800, 200, 1200, 2500, 700, 1300],
    "Sadakat Puanı": [200, 250, 50, 300, 180, 20, 120, 250, 70, 130]
}

dataframe = pd.DataFrame(data)
kriter = dataframe[(dataframe["Ürün Kategorisi"] =="Elektronik") & (dataframe["Harcanan Tutar"] >= 1500 )]
dataframe_grouped = kriter.groupby("Müşteri ID").agg({"Harcanan Tutar": "sum","Sadakat Puanı": "sum"}).reset_index()
                    #müşteri id değerine sahip satırlar bir araya getiriliyor
                    #.agg = aggregation = gruplandırılmış veriler üzerinde toplu işlem yapmayı sağlar.
                    #harcanan tutar : sum() topla diyorsun işte ve hepsinde yapmış oluyorsun grupldıklarının agg sayesinde.
                    #reset index tamamen görsellik için.

print(dataframe_grouped)
"""
"""
import pandas as pd

data = {
    "Bölge": ["Bölge A", "Bölge B", "Bölge C", "Bölge A", "Bölge B", "Bölge C", "Bölge A", "Bölge B", "Bölge C"],
    "Zemin Türü": ["Kil", "Kum", "Çakıl", "Kil", "Kum", "Çakıl", "Kil", "Kum", "Çakıl"],
    "Temel Türü": ["Radye Temel", "Kazık Temel", "Radye Temel", "Kazık Temel", "Radye Temel", "Kazık Temel", "Radye Temel", "Kazık Temel", "Radye Temel"],
    "Zemin Taşıma Kapasitesi (kN/m^2)": [150, 200, 250, 160, 190, 240, 155, 205, 245]
}

dataframe = pd.DataFrame(data)

# Zemin taşıma kapasitesini "mean" (ortalama) ile gruplama
grupla = dataframe.groupby(["Bölge", "Zemin Türü","Temel Türü"]).agg({
    "Zemin Taşıma Kapasitesi (kN/m^2)": "mean"
}).reset_index()

# Her bölge ve zemin türü için en yüksek ortalama taşıma kapasitesine sahip temel türünü bulma
en_iyi_temel = grupla.loc[grupla.groupby(["Bölge","Zemin Türü"])["Zemin Taşıma Kapasitesi (kN/m^2)"].idxmax()]

print(en_iyi_temel)
"""
"""
import pandas as pd

data = {
    "Su/Çimento Oranı": [0.4, 0.45, 0.5, 0.4, 0.45, 0.5, 0.4, 0.45, 0.5],
    "Agrega Türü": ["Kum", "Kum", "Kum", "Çakıl", "Çakıl", "Çakıl", "Karışık", "Karışık", "Karışık"],
    "Basınç Dayanımı (MPa)": [40, 38, 35, 42, 40, 37, 45, 43, 41]
}

dataframe = pd.DataFrame(data)

grupla = dataframe.groupby(["Su/Çimento Oranı","Agrega Türü"]).agg({
    "Basınç Dayanımı (MPa)":"mean"}).reset_index()

en_iyisi = grupla.loc[grupla["Basınç Dayanımı (MPa)"].idxmax()]
print(en_iyisi)
"""
"""
import pandas as pd

data = {
    "Zemin Türü": ["Kil", "Kil", "Kil", "Kum", "Kum", "Kum", "Çakıl", "Çakıl", "Çakıl"],
    "İyileştirme Yöntemi": ["Jet Grout", "Stone Column", "Lime Stabilization", 
                            "Jet Grout", "Stone Column", "Lime Stabilization", 
                            "Jet Grout", "Stone Column", "Lime Stabilization"],
    "Taşıma Kapasitesi Artışı (%)": [50, 40, 30, 45, 35, 25, 55, 50, 40],
    "Zemin Oturması Azalması (%)": [30, 35, 25, 40, 30, 20, 45, 40, 35] }

dataframe = pd.DataFrame(data)

# Her zemin türü için en yüksek taşıma kapasitesi artışı sağlayan iyileştirme yöntemini bulma
en_iyi_tka = dataframe.loc[dataframe.groupby("Zemin Türü")["Taşıma Kapasitesi Artışı (%)"].idxmax()]
en_az_otur = dataframe.loc[dataframe.groupby("Zemin Türü")["Zemin Oturması Azalması (%)"].idxmax()]

print("En az oturma değerine sahip yöntemler:")
for index, row in en_az_otur.iterrows():
    print(f"Zemin Türü: {row['Zemin Türü']}, İyileştirme Yöntemi: {row['İyileştirme Yöntemi']}, Zemin Oturması Azalması: %{row['Zemin Oturması Azalması (%)']}")

print("\nEn iyi taşıma kapasitesine sahip yöntemler:")
for index, row in en_iyi_tka.iterrows():
    print(f"Zemin Türü: {row['Zemin Türü']}, İyileştirme Yöntemi: {row['İyileştirme Yöntemi']}, Taşıma Kapasitesi Artışı: %{row['Taşıma Kapasitesi Artışı (%)']}")
"""
