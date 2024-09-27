#kod çalışıyor ama master_data tablosunda veri olmadığı için hata veriyor.

import openpyxl
from openpyxl import Workbook

data = openpyxl.load_workbook("C:\\Users\\kadir\\Desktop\\GeoProje\\GeoProje Openpyxl Tutorial\\master_data.xlsx")
names = data["data"]

is_data = True
row_count = 1

while is_data:
    row_count +=1
    first_name = names.cell(row=row_count, column=1.).value

    if first_name !=None:
        print(first_name)
    else:
        is_data = False

data.save("C:\\Users\\kadir\\Desktop\\GeoProje\\GeoProje Openpyxl Tutorial\\master_data.xlsx")

