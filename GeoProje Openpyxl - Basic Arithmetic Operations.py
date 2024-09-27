#bu çalışmada sayıları yazıp a7 de formül kullanarak tek bir hücrede topladım.

import openpyxl
from openpyxl import Workbook
import openpyxl.workbook

Workbook = Workbook()

worksheet = Workbook.active

worksheet["A1"] = 100
worksheet["A2"] = 200
worksheet["A3"] = 300
worksheet["A4"] = 400
worksheet["A5"] = 500

worksheet["A7"] = "=sum(A1:A5)"

Workbook.save("sum.xlsx")

