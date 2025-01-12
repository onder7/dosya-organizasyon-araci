import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files(directory):
    try:
        # Dizindeki tüm dosyaları listele
        for filename in os.listdir(directory):
            # Dosyanın tam yolunu al
            file_path = os.path.join(directory, filename)
            
            # Eğer bu bir dosya değilse (örneğin bir klasörse) atla
            if os.path.isfile(file_path):
                # Dosya uzantısını al (örneğin .txt, .jpg)
                file_extension = filename.split('.')[-1].lower()
                
                # Uzantıya göre hedef klasörü belirle
                target_folder = os.path.join(directory, file_extension.capitalize() + " Dosyaları")
                
                # Eğer hedef klasör yoksa, oluştur
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                
                # Dosyayı hedef klasöre taşı
                shutil.move(file_path, os.path.join(target_folder, filename))
        
        # İşlem tamamlandığında kullanıcıya bilgi ver
        messagebox.showinfo("Başarılı", "Dosyalar başarıyla düzenlendi!")
    except Exception as e:
        # Hata durumunda kullanıcıya bilgi ver
        messagebox.showerror("Hata", f"Dosyalar düzenlenirken bir hata oluştu: {e}")

def select_directory():
    # Kullanıcıdan bir dizin seçmesini iste
    directory = filedialog.askdirectory()
    if directory:
        # Seçilen dizini organize et
        organize_files(directory)

def show_about():
    # Hakkında penceresi
    about_text = """
    Dosya Organizasyon Aracı

    Yazar: Önder Aköz
    E-posta: onder7@gmail.com
    GitHub: github.com/onder7

    Bu uygulama, dosyaları uzantılarına göre otomatik olarak klasörlere ayırır.
    """
    messagebox.showinfo("Hakkında", about_text)

# GUI oluştur
root = tk.Tk()
root.title("Dosya Organizasyon Aracı")
root.geometry("400x200")

# Menü çubuğu oluştur
menu_bar = tk.Menu(root)

# Yardım menüsü
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Hakkında", command=show_about)
menu_bar.add_cascade(label="Yardım", menu=help_menu)

# Menü çubuğunu pencereye ekle
root.config(menu=menu_bar)

# Başlık etiketi
title_label = tk.Label(root, text="Dosya Organizasyon Aracı", font=("Arial", 16))
title_label.pack(pady=10)

# Açıklama etiketi
description_label = tk.Label(root, text="Dosyaları uzantılarına göre otomatik olarak klasörlere ayırır.", font=("Arial", 12))
description_label.pack(pady=10)

# Dizin seç butonu
select_button = tk.Button(root, text="Dizin Seç ve Organize Et", command=select_directory, font=("Arial", 12))
select_button.pack(pady=20)

# Uygulamayı çalıştır
root.mainloop()