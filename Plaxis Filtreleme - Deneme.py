import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os
import xlsxwriter
import matplotlib.pyplot as plt
import re  # Geçersiz karakterleri temizlemek için
from io import BytesIO  # Bellekte görüntüleri tutmak için
# from plxscripting.easy import *  # PLAXIS API modülü (aktif hale getirin)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("PLAXIS 2D Veri Aktarım Aracı")
root.configure(bg='white')

# Pencereyi ekranın ortasına yerleştirme fonksiyonu
def center_window(window, width, height):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/2))
    window.geometry(f'{width}x{height}+{x}+{y}')

center_window(root, 600, 200)

# Seçilen dosya yolu
file_path = ''

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("PLAXIS 2D Model Files", "*.p2dx")])
    if file_path:
        file_label.config(text=f"Seçilen Dosya: {os.path.basename(file_path)}")

def process_data():
    if not file_path:
        messagebox.showerror("Hata", "Lütfen bir model dosyası seçin.")
        return

    # İşlenecek grafiklerin listesi
    selected_graphs = [
        'Total Displacements |u| grafiği',
        'Güvenlik Sayısı Grafiği',
        'Total Displacements ux (yatay) Moment Diyagramı',
        'Envelope of Axial Forces N grafiği',
        'Envelope of Shear Forces Q grafiği',
        'Envelope of Bending Moment M grafiği',
        'Node-to-node anchors verileri',
    ]

    # PLAXIS 2D Output programına bağlanma ve model yükleme
    # s_o, g_o = new_server('localhost', 10000, password='your_password')
    # g_o.open(file_path)

    # Excel dosyası oluştur ve grafikleri belirtilen hücrelere yerleştir
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    excel_file = os.path.join(desktop, 'plaxis_output.xlsx')

    workbook = xlsxwriter.Workbook(excel_file)
    worksheet = workbook.add_worksheet()

    # Sütun genişliklerini ve satır yüksekliklerini ayarlarken değerleri saklamak için sözlükler oluşturuyoruz
    column_widths = {}
    row_heights = {}

    def char_width_to_pixels(char_width):
        # Karakter genişliğinden piksele dönüşüm (yaklaşık)
        pixels = int(char_width * 7 + 5)
        return pixels

    def points_height_to_pixels(points_height):
        # Nokta yüksekliğinden piksele dönüşüm
        pixels = int(points_height * 1.3333)
        return pixels

    default_column_width_chars = 8.43  # Excel varsayılanı
    default_column_width_pixels = char_width_to_pixels(default_column_width_chars)

    default_row_height_points = 15  # Excel varsayılanı
    default_row_height_pixels = points_height_to_pixels(default_row_height_points)

    # Sütun genişliklerini ayarlama ve piksel değerlerini saklama
    for col in range(0, 40):  # A'dan AN'ye kadar
        char_width = 9  # 9 karakter genişlik
        worksheet.set_column(col, col, char_width)
        pixel_width = char_width_to_pixels(char_width)
        column_widths[col] = pixel_width

    # Satır yüksekliklerini ayarlama ve piksel değerlerini saklama
    for row in range(0, 90):
        points_height = 20  # 20 nokta yükseklik
        worksheet.set_row(row, points_height)
        pixel_height = points_height_to_pixels(points_height)
        row_heights[row] = pixel_height

    # Hücre konumlarını tanımla (sol üst ve sağ alt hücreler)
    cell_positions = {
        'Total Displacements |u| grafiği': ('A1', 'M28'),
        'Güvenlik Sayısı Grafiği': ('O1', 'AA28'),
        'Total Displacements ux (yatay) Moment Diyagramı': ('AC1', 'AO28'),
        'Envelope of Axial Forces N grafiği': ('A30', 'M58'),
        'Envelope of Shear Forces Q grafiği': ('O30', 'AA58'),
        'Envelope of Bending Moment M grafiği': ('AC30', 'AO59'),
        'Node-to-node anchors verileri': ('L61', 'AD90'),
    }

    # Görüntüleri bellekte tutmak için sözlük
    images_in_memory = {}

    for graph_name in selected_graphs:
        # Dosya adını geçersiz karakterlerden arındırma
        sanitized_name = re.sub(r'[<>:"/\\|?*]', '_', graph_name)

        # PLAXIS 2D'den grafiği al ve bellekte sakla
        # Burada PLAXIS 2D API'sini kullanarak grafiği oluşturmanız gerekiyor
        # Örnek olarak, placeholder grafik oluşturacağız

        # Bellekte görüntüyü saklamak için BytesIO kullanıyoruz
        image_data = BytesIO()

        # Placeholder grafik oluşturma (PLAXIS API yerine)
        plt.figure()
        plt.title(graph_name)
        plt.plot([0, 1, 2], [0, 1, 0])  # Örnek veri
        plt.savefig(image_data, format='png')
        plt.close()
        image_data.seek(0)  # Başlangıca dön

        # Bellekteki görüntüyü sözlüğe ekle
        images_in_memory[graph_name] = image_data

    # Görüntüleri Excel dosyasına yerleştirme
    for graph_name in selected_graphs:
        image_data = images_in_memory[graph_name]

        # Hücre konumlarını al
        start_cell, end_cell = cell_positions.get(graph_name, ('A1', 'A1'))

        # Başlangıç ve bitiş hücrelerinin satır ve sütun indekslerini al
        start_row, start_col = xlsxwriter.utility.xl_cell_to_rowcol(start_cell)
        end_row, end_col = xlsxwriter.utility.xl_cell_to_rowcol(end_cell)

        # Hücre aralığının toplam piksel boyutlarını hesapla
        total_width = 0
        for col in range(start_col, end_col + 1):
            total_width += column_widths.get(col, default_column_width_pixels)

        total_height = 0
        for row in range(start_row, end_row + 1):
            total_height += row_heights.get(row, default_row_height_pixels)

        # Görüntü boyutlarını al
        image_data.seek(0)
        image = plt.imread(image_data, format='png')
        img_height, img_width, _ = image.shape

        # Görüntü ölçeklerini hesapla
        x_scale = total_width / img_width
        y_scale = total_height / img_height

        # Grafiği belirtilen hücreye ekle
        worksheet.insert_image(start_cell, '', {'image_data': image_data, 'x_scale': x_scale, 'y_scale': y_scale})

    workbook.close()

    # İşlem tamamlandıktan sonra mesaj göster
    show_completion_window()

def show_completion_window():
    completion_window = tk.Toplevel(root)
    completion_window.title("İşlem Tamamlandı")
    completion_window.configure(bg='white')

    center_window(completion_window, 300, 100)

    tk.Label(completion_window, text="İşlem Tamamlandı!", bg='white', fg='black').pack(expand=True)

# Arayüz elemanları
file_button = tk.Button(root, text="Model Dosyası Seç", command=select_file, bg='white', fg='black')
file_button.pack(pady=10)

file_label = tk.Label(root, text="Seçilen Dosya: Yok", bg='white', fg='black')
file_label.pack()

process_button = tk.Button(root, text="Verileri Aktar", command=process_data, bg='white', fg='black')
process_button.pack(pady=20)

root.mainloop()

"C:\\Users\\kadir\\Desktop\\GeoProje\\Geoproje 65'lik Kazık Betonarme Hesaplar\\Filtaş.p2dx"

ux = g_o.Plots[-1].ResultType = g_o.ResultTypes.Soil.Ux
renkli = g_o.Plots[-1].PlotType = "Shadings"
resim olarak aktarma exportlama = pil_image = g_o.Plots[-1].export()
aç kapa = s_i/s_o.open(uzantı)
s_i/s_o.close()

# geometric data for correct anchor: 
Xanchor = 40.0 
Yanchor = 27.0  

# start from Phase_3 since the anchors are
# not active before this phase 
for phase in g_o.Phases[3:]: 
    anchorF = g_o.getresults(phase, 
                             g_o.ResultTypes.NodeToNodeAnchor.AnchorForce2D, 
                             'node') 
    anchorX = g_o.getresults(phase, 
                              g_o.ResultTypes.NodeToNodeAnchor.X, 
                             'node') 
    anchorY = g_o.getresults(phase, 
                             g_o.ResultTypes.NodeToNodeAnchor.Y, 
                             'node') 
    
    for x,y,N in zip(anchorX,anchorY,anchorF): 
        # check for the correct anchor by location: 
        if abs(x - Xanchor) < 1E-5 and abs(y - Yanchor) < 1E-5: 
            print("Anchor force N in {}: {:.2f} kN/m".format(phase.Name,N))

soilX = g_o.getresults(g_o.Phase_6, g_o.ResultTypes.Soil.X, 'node') 
soilY = g_o.getresults(g_o.Phase_6, g_o.ResultTypes.Soil.Y, 'node') 

#max bending moment
plateM = g_o.getresults(phase, g_o.ResultTypes.Plate.M2D, 'node')



# # PLAXIS'ten gerekli 
# def get_plaxis_data(g_i, phase):
#     try:
#         # Total Displacement grafiği
#         total_displacements = g_i.getcurveresults(phase, g_i.ResultTypes.TotalDisplacement)

#         # Güvenlik Sayısı grafiği
#         safety_factor = g_i.getcurveresults(phase, g_i.ResultTypes.SafetyFactor)

#         # Yatay deplasman verisi
#         horizontal_displacements = g_i.getcurveresults(phase, g_i.ResultTypes.Displacement.Ux)

#         # Kuvvet grafikleri
#         axial_forces = g_i.getresults(phase, g_i.ResultTypes.StructuralForces.AxialForce, "node")
#         shear_forces = g_i.getresults(phase, g_i.ResultTypes.StructuralForces.ShearForce, "node")
#         bending_moments = g_i.getresults(phase, g_i.ResultTypes.StructuralForces.BendingMoment, "node")

#         # Node-to-node anchors tablosu
#         node_to_node_stresses = g_i.getresults(phase, g_i.ResultTypes.Stresses.NodeToNodeAnchorForce, "node")

#         return {
#             'total_displacements': total_displacements,
#             'safety_factor': safety_factor,
#             'horizontal_displacements': horizontal_displacements,
#             'axial_forces': axial_forces,
#             'shear_forces': shear_forces,
#             'bending_moments': bending_moments,
#             'node_to_node_stresses': node_to_node_stresses
#         }
#     except Exception as e:
#         print(f"Veri çekilirken hata oluştu: {e}")
#         return None

# # Veriler PNG formatında bellekte tutuluyor
# def save_plaxis_graphics(data):
#     try:
#         img_data = {}
#         for key, value in data.items():
#             imgdata = BytesIO()
#             plt.figure()
#             plt.plot(value)  # Grafik çizimi (PLAXIS'ten alınan veri gösterilecek)
#             plt.savefig(imgdata, format='png')
#             imgdata.seek(0)  # Bellekte başa dön
#             img_data[key] = imgdata
#             plt.close()

#         return img_data
#     except Exception as e:
#         print(f"Grafikler oluşturulurken hata oluştu: {e}")
#         return None

# # Grafikleri Excel'e yerleştir
# def insert_graphics_to_excel(img_data, output_file_path):
#     try:
#         with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
#             workbook = writer.book

#             # Her bir grafiği belirlenen hücre aralıklarına yerleştir
#             worksheet = workbook.active  # İlk sayfa seçildi
#             img_positions = {
#                 'total_displacements': 'A1',
#                 'safety_factor': 'O1',
#                 'horizontal_displacements': 'AC1',
#                 'axial_forces': 'A30',
#                 'shear_forces': 'O30',
#                 'bending_moments': 'AC30',
#                 'node_to_node_stresses': 'L61'
#             }

#             for key, start_cell in img_positions.items():
#                 img = Image(img_data[key])
#                 worksheet.add_image(img, start_cell)

#             workbook.save(output_file_path)

#         print(f"Grafikler {output_file_path} konumuna kaydedildi.")
#     except Exception as e:
#         print(f"Grafikler Excel'e kaydedilirken hata oluştu: {e}")

# # Tkinter GUI: Dosya seçimi ve işlem ilerlemesi
# def select_file():
#     file_path = filedialog.askopenfilename(filetypes=[("PLAXIS files", "*.p2dx")])
#     if file_path:
#         process_file(file_path)

# def process_file(file_path):
#     progress_popup = tk.Toplevel()
#     progress_popup.title("Dosya İşleniyor")
#     progress_popup.geometry("300x100")
#     progress_popup.configure(bg='white')

#     label = tk.Label(progress_popup, text="Dosya İşleniyor...", bg='white', fg='black')
#     label.pack(pady=10)

#     progress = ttk.Progressbar(progress_popup, orient='horizontal', mode='indeterminate', length=250)
#     progress.pack(pady=10)
#     progress.start()

#     # PLAXIS API bağlantısı ve veri çekme
#     s_i, g_i = connect_to_plaxis_server('localhost', 'password')
#     if not g_i:
#         label.config(text="Sunucuya bağlanılamadı!")
#         progress.stop()
#         progress_popup.destroy()
#         return
    
#     # Uygun phase'i bulalım
#     phase = find_suitable_phase(g_i)
#     if not phase:
#         label.config(text="Uygun Phase bulunamadı!")
#         progress.stop()
#         progress_popup.destroy()
#         return
    
#     # Verileri uygun phase'den çek
#     data = get_plaxis_data(g_i, phase)

#     if data:
#         img_data = save_plaxis_graphics(data)

#         # Masaüstü yolunu belirle ve kaydet
#         desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
#         output_file = os.path.join(desktop_path, "plaxis_output.xlsx")
#         insert_graphics_to_excel(img_data, output_file)

#     progress.stop()
#     progress_popup.destroy()

#     # İşlem tamamlandığında bilgi mesajı
#     completion_popup = tk.Toplevel()
#     completion_popup.title("İşlem Tamamlandı")
#     completion_popup.geometry("300x100")
#     completion_popup.configure(bg='white')

#     label = tk.Label(completion_popup, text="İşlem başarıyla tamamlandı!", bg='white', fg='black')
#     label.pack(pady=20)

#     ok_button = tk.Button(completion_popup, text="Tamam", command=completion_popup.destroy)
#     ok_button.pack(pady=10)

# # Ana Tkinter penceresi
# root = tk.Tk()
# root.title("PLAXIS Dosya İşleme")
# root.geometry("400x200")
# root.configure(bg='white')

# select_button = tk.Button(root, text="Dosya Seç", command=select_file, bg='white', fg='black')
# select_button.pack(pady=20)

# root.mainloop()
