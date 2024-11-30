
import customtkinter as ctk

from ...setelan import reset_frame
from .handler_tombol import transfer_handle


def transfer(app, frame, sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    # bersihkan frame
    reset_frame(frame['header'])
    reset_frame(frame['body'])
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    if auth == True:
        ################################################## HEADER
        #########################################
        
        title = ctk.CTkButton(frame['header'], text="BANK AJA - TRANSFER", font=('Arial', 28, 'bold'))
        title.pack(side="top")
        
        halo = ctk.CTkLabel(frame['header'], text=f"Hai, {user['nama']}! Masukan data dengan benar!", fg_color="white", text_color='black')
        halo.pack(side='top', fill='x', expand=True, ipadx=10, ipady=10, pady=10)
        
        ######################################### 
        ################################################## HEADER
        
        
        
        ################################################## BODY
        #########################################
        
        
        ########### INPUT USER
        # Buat pembungkus untuk untuk inputan user kartu
        penerima_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
        penerima_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
        
        # Buat keterangan tentang input
        penerima_Label = ctk.CTkLabel(penerima_wrap, text="Nomor Rekening atau Usernama Penerima") # Label Inputan
        penerima_Label.pack(side='left', padx=10, pady=10)
        
        # buat inputan
        penerima_input = ctk.CTkEntry(penerima_wrap, corner_radius=10, placeholder_text="usernama.. atau nomor kartu..", width=300, height=35) # Inputan
        penerima_input.pack(side='right', padx=10, pady=10)
        ###########
        
        ######## #INPUT JUMLAH
        # Buat pembungkus untuk inputan jumlah
        nominal_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
        nominal_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
        
        # Buat keterangan tentang input
        nominalLabel = ctk.CTkLabel(nominal_wrap, text="Nominal") # Label
        nominalLabel.pack(side='left', padx=10, pady=10)
        
        # Buat inputan
        nominal_input = ctk.CTkEntry(nominal_wrap, corner_radius=10, placeholder_text="50000", width=300, height=35) # Inputan
        nominal_input.pack(side='right', padx=10, pady=10)
        ############

        inputs = {
        'penerima': penerima_input,
        'nominal': nominal_input,
        }
 
        ######################################### 
        ################################################## BODY
        
        
        
        ################################################## FOOTER
        ######################################### 
        
        reset_frame(frame['footer'])
        from ..proses import kembali_ke_menu
        kembaliBtn = ctk.CTkButton(frame['footer'], height=50,text="Kembali", fg_color='orange', text_color='black', command=lambda : kembali_ke_menu(app, frame, sesi))
        kembaliBtn.pack(side="left", fill='x', expand=True, padx=10)
        
        lanjutBtn = ctk.CTkButton(frame['footer'], height=50,text="Lanjut Cek", command=lambda : transfer_handle(app, frame, inputs, sesi))
        lanjutBtn.pack(side="left", fill='x', expand=True, padx=10)
        
        ######################################### 
        ################################################## FOOTER
    else:
        pass