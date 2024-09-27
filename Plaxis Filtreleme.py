#Modeli seçebiliyor, yeni Excel dosyası oluşturarak istenilen grafikleri istenilen konumlara akarabiliyorum. GUI de de herhangi bir problem yok. PLAXIS API entegrasyonu yapılacak.

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