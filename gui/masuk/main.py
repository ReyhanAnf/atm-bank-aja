import customtkinter as ctk

from ..setelan import reset_frame


def formulir_masuk(app, frame):
    app.title("BANK AJA - GUI")
    
    reset_frame(frame['header'])
    reset_frame(frame['body'])
    reset_frame(frame['footer'])
    ###################################################### HEADER
    
    
    title = ctk.CTkButton(frame['header'], text="BANK AJA - MASUK", font=('Arial', 28, 'bold'))
    title.pack(side="top")
    ###################################################### HEADER
    
    
    
    ###################################################### BODY
    
    
    #Sapaan
    sapaan = ctk.CTkLabel(frame['body'], text="Halo! Selamat Datang Di BANK AJA. Silahkan Masuk")
    sapaan.pack(side="top", fill='x')
    ###################################################### BODY
    

    ###################################################### FOOTER
    masukBtn = ctk.CTkButton(frame['footer'], height=50,text="Masuk")
    masukBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    
    def kembali(app, frame):
        from ..awal.main import home
        home(app, frame)
    batalBtn = ctk.CTkButton(frame['footer'], height=50,text="Batal", command=lambda : kembali(app, frame))
    batalBtn.pack(side="left", fill='x', expand=True, padx=10)
    ###################################################### FOOTER
    
    
       


    