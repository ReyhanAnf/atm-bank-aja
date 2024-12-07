# Import library eksternal yaitu library TKinter atau CustomTKinter
# import customtkinter as ctk
from tkinter import Tk, Canvas, Button, PhotoImage
from .awal import main as awal
from .setelan import relative_to_assets
# Seting agar gui sesuai tema system - dark atau light
# ctk.set_appearance_mode("System") 

# Mendefaultkan tema menjadi berwarna hijau
# ctk.set_default_color_theme("green") 

# Variabel width dan height dari aplikasi saat dibuka
# appWidth, appHeight = 700, 700
LOC = "awal"
# Fungsi utama file ini
def main():
    # Deklarasi Aplikasi GUI
    # app = ctk.CTk()
    # # Seting aplikasi bisa responsive berubah ukuran
    # app.resizable(width=True, height=True)
    # # Set width dan height dari aplikasi saat dibuka
    # app.geometry(f"{appWidth}x{appHeight}")
    
    # # Buat frame header atau bagian header
    # frame_header = ctk.CTkFrame(app, corner_radius=10, fg_color="transparent")
    # frame_header.pack(side="top", fill="x", expand=True, ipadx=10, ipady=10)
    
    # # Buat frame body atau bagian body
    # frame_body = ctk.CTkFrame(app, corner_radius=10, fg_color="transparent")
    # frame_body.pack(side="top", fill="both", expand=True, ipadx=10, ipady=10)
    
    # # Buat frame footer atau bagian footer
    # frame_footer = ctk.CTkFrame(app, corner_radius=10, fg_color="transparent")
    # frame_footer.pack(side="bottom", fill="x", expand=True, ipadx=10, ipady=10)
    
    # Bungkus semua frame kedalam satu variabel untuk kebutuhan fungsi lain
    # frame = {
    #     'header': frame_header,
    #     'body': frame_body,
    #     'footer': frame_footer
    # }
    
    # Jalankan modul pertama (Folder) awal untuk masuk kedalam Home Aplikasi
    # membawa argumen app dan frame
    app = Tk()

    app.geometry("687x549")
    
    app.configure(bg = "#EBF3FF")
    
    
    awal.home(app)
    
    # Aplikasi dijalankan disini, selama app mainloop maka akan terus berjalan
        
