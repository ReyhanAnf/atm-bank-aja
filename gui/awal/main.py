# Import library eksternal yaitu library TKinter atau CustomTKinter
import customtkinter as ctk

# Import modul internal dari folder lain
from ..masuk.main import formulir_masuk
from ..daftar.main import formulir_daftar
from ..setelan import reset_frame

# Fungsi Home - Tampilan awal aplikasi
def home(app, frame):
    # Buat judul aplikasi
    app.title("BANK AJA - GUI")
    
    # Reset semua frame utama agar bersih dari widget lain
    reset_frame(frame['header'])
    reset_frame(frame['body'])
    reset_frame(frame['footer'])
    
    
    
    ###################################################### HEADER
    ###################################################### 
    
    # Buat tampilan judul untuk navigasi
    title = ctk.CTkButton(frame['header'], text="BANK AJA - HOME", font=('Arial', 28, 'bold'))
    # Tampilkan tampilan judul untuk navigasi
    title.pack(side="top")
    
    ###################################################### 
    ###################################################### HEADER
    
    
    
    ###################################################### BODY
    ###################################################### 
    
    #Sapaan
    sapaan = ctk.CTkLabel(frame['body'], text="Halo! Selamat Datang Di BANK AJA. Silahkan Masuk atau Mendaftar")
    # Tampilkan Sapaan
    sapaan.pack(side="top", fill='x')
    
    ###################################################### 
    ###################################################### BODY
    
    
    
    ###################################################### FOOTER
    ###################################################### 
    
    # Buat tombol masuk
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol masuk di klik maka akan masuk ke fungsi lambda yang mengeksekusi fungsi formulir masuk
    masukBtn = ctk.CTkButton(frame['footer'], height=50,text="Masuk", command=lambda : formulir_masuk(app, frame))
    # Tampilkan tombol
    masukBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    # Buat tombol daftar
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol daftar di klik maka akan menjalankan ke fungsi lambda yang mengeksekusi fungsi formulir daftar
    daftarBtn = ctk.CTkButton(frame['footer'], height=50,text="Daftar", fg_color='blue', command=lambda : formulir_daftar(app, frame))
    # Tampilkan tombol
    daftarBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    # Buat tombol keluar
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol keluar di klik maka akan menjalankan ke fungsi lambda yang mengeksekusi fungsi formulir keluar
    keluarBtn = ctk.CTkButton(frame['footer'], height=50,text="Keluar", fg_color='red', command=exit)
    # Tampilkan tombol
    keluarBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    ###################################################### 
    ###################################################### FOOTER


    