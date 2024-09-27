from plxscripting.easy import *
import math
import pyautogui
from PIL import Image
import openpyxl
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from io import BytesIO

# PLAXIS sunucusuna bağlanma
s_i, g_i  = new_server("localhost", 10000, password="hDuviP7EnXxwYCUN")
s_o, g_o = new_server("localhost", 10001, password="hDuviP7EnXxwYCUN")

# PLAXIS modelini aç
s_i.open("C:\\Users\\kadir\\Desktop\\GeoProje\\Geoproje 65'lik Kazık Betonarme Hesaplar\\Filtaş.p2dx")
s_o.open("C:\\Users\\kadir\\Desktop\\GeoProje\\Geoproje 65'lik Kazık Betonarme Hesaplar\\Filtaş.p2dx")


# Fazları tanımla (Input fazları)
phases = g_i.Phases  
target_keywords = ["Statik S.A.", "Dinamik S.A.", "S.A."]  # Aranacak faz isimleri

# Hedef fazı bulma ve Output API'de o faza geçiş yapma
selected_phase = None
for phase in phases:
    phase_name = phase.Identification  # Fazın kimlik bilgisi (ID)

    # Eğer fazın ismi hedef isimlerden biriyle eşleşirse
    if phase_name in target_keywords:
        print(f"İstenilen faz bulundu: {phase_name}")
        selected_phase = phase  # Bulunan fazı kaydet
        break

# Eğer faz bulunduysa, Output'ta o faza geçiş yap
if selected_phase is not None:
    # Output fazları üzerinde fazı bulalım
    for output_phase in g_o.Phases:
        if output_phase.Identification == selected_phase.Identification:
             ux = g_o.getresults(output_phase, g_o.ResultTypes.Soil.Ux, 'node')





                               

 




        





    
    
    



# g_o.Plots[0].ResultType = g_o.ResultTypes.Soil.Ux
# g_o.Plots[0].PlotType = 'shadings'


# left = 346
# top = 126
# width = 2208
# height = 689

# screenshot = pyautogui.screenshot(region=(left,top,width,height))
# buffer = BytesIO()
# screenshot.save(buffer, format="PNG")

# workbook = Workbook()
# worksheet = workbook.active

# image=Image.open(buffer)

# with BytesIO as img_buf:
#     image.save(img_buf, format="PNG")
#     img_buf.seek(0)
#     img_excel = Image(img_buf)

# worksheet.add_image(img_excel, ('A1','M28'))
# workbook.save("deneme.xlsx")