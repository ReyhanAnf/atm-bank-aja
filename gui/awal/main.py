import customtkinter as ctk

from ..masuk.main import formulir_masuk
from ..daftar.main import formulir_daftar
from ..setelan import reset_frame

def home(app, frame):
    app.title("BANK AJA - GUI")
    
    reset_frame(frame['header'])
    reset_frame(frame['body'])
    reset_frame(frame['footer'])
    ###################################################### HEADER
    
    
    title = ctk.CTkButton(frame['header'], text="BANK AJA - HOME", font=('Arial', 28, 'bold'))
    title.pack(side="top")
    ###################################################### HEADER
    
    
    
    ###################################################### BODY
    
    
    #Sapaan
    sapaan = ctk.CTkLabel(frame['body'], text="Halo! Selamat Datang Di BANK AJA. Silahkan Masuk atau Mendaftar")
    sapaan.pack(side="top", fill='x')
    ###################################################### BODY
    
    
    
    ###################################################### FOOTER
    
    
    masukBtn = ctk.CTkButton(frame['footer'], height=50,text="Masuk", command=lambda : formulir_masuk(app, frame))
    masukBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    daftarBtn = ctk.CTkButton(frame['footer'], height=50,text="Daftar", fg_color='blue', command=lambda : formulir_daftar(app, frame))
    daftarBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    keluarBtn = ctk.CTkButton(frame['footer'], height=50,text="Keluar", fg_color='red', command=exit)
    keluarBtn.pack(side="left", fill='x', expand=True, padx=10)
    ###################################################### FOOTER


    