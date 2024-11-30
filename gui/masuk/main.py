import customtkinter as ctk

from ..setelan import reset_frame
from .handler_tombol import kembali_ke_home, handle_masuk

def formulir_masuk(app, frame):
    app.title("BANK AJA - GUI")
    
    reset_frame(frame['header'])
    reset_frame(frame['body'])
    reset_frame(frame['footer'])
    
    
    ###################################################### HEADER
    ##############################################    
    
    title = ctk.CTkButton(frame['header'], text="BANK AJA - MASUK", font=('Arial', 28, 'bold'))
    title.pack(side="top")
    
    ##############################################    
    ###################################################### HEADER
    
    
    
    ###################################################### BODY
    ############################################## 
    
    ########### INPUT USER
    # Buat pembungkus untuk untuk inputan user kartu
    user_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    user_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
    
    # Buat keterangan tentang input
    user_Label = ctk.CTkLabel(user_wrap, text="Nomor Rekening atau User_input") # Label Inputan
    user_Label.pack(side='left', padx=10, pady=10)
    
    # buat inputan
    user_input = ctk.CTkEntry(user_wrap, corner_radius=10, placeholder_text="cth : 812347892174", width=300, height=40) # Inputan
    user_input.pack(side='right', padx=10, pady=10)
    ###########
    
    ######## #INPUT PIN
    # Buat pembungkus untuk inputan pin
    pin_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    pin_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
    
    # Buat keterangan tentang input
    pinLabel = ctk.CTkLabel(pin_wrap, text="PIN") # Label
    pinLabel.pack(side='left', padx=10, pady=10)
    
    # Buat inputan
    pin_input = ctk.CTkEntry(pin_wrap, corner_radius=10, placeholder_text="***", width=300, height=40) # Inputan
    pin_input.pack(side='right', padx=10, pady=10)
    ############
    
    
    inputs = {
        'usernama': user_input,
        'pin': pin_input,
    }
    ############################################## 
    ###################################################### BODY
    

    ###################################################### FOOTER
    ############################################ 
    
    masukBtn = ctk.CTkButton(frame['footer'], height=50,text="Masuk", command=lambda : handle_masuk(app, frame, inputs))
    masukBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    
    batalBtn = ctk.CTkButton(frame['footer'], height=50,text="Batal", fg_color='red', command=lambda : kembali_ke_home(app, frame))
    batalBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    ############################################ 
    ###################################################### FOOTER
    
    
       


    