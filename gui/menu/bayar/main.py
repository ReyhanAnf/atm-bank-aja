
import customtkinter as ctk

from ...setelan import reset_frame
from .handler_tombol import bayar_handle


def bayar(app, frame, sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    # bersihkan frame
    reset_frame(frame['header'])
    reset_frame(frame['body'])
    reset_frame(frame['footer'])
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    if auth == True:
        ################################################## HEADER
        #########################################
        
        title = ctk.CTkButton(frame['header'], text="BANK AJA - BAYAR", font=('Arial', 28, 'bold'))
        title.pack(side="top")
        
        halo = ctk.CTkLabel(frame['header'], text=f"Hai, {user['nama']}! Masukan data dengan benar!", fg_color="white", text_color='black')
        halo.pack(side='top', fill='x', expand=True, ipadx=10, ipady=10, pady=10)
        
        ######################################### 
        ################################################## HEADER
        
        
        
        ################################################## BODY
        #########################################
        
        
        menu = ['PLN Paska', 'PLN Token', 'PDAM',  'Virtual Account', 'Pulsa', 'BPJS', 'TopUp Gopay', 'TopUp Shopeepay', 'TopUp Ovo', 'Keluar']
        
        ########### INPUT USER
        # Buat pembungkus untuk untuk inputan user kartu
        menu_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
        menu_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
        
        # Buat keterangan tentang input
        menu_Label = ctk.CTkLabel(menu_wrap, text="Menu") # Label Inputan
        menu_Label.pack(side='left', padx=10, pady=10)
        
        pilihan_bayar = ctk.StringVar(value="PLN Paska")
        menu_bayar = ctk.CTkComboBox(menu_wrap, values=menu, variable=pilihan_bayar)
        menu_bayar.pack(side='right', padx=10, pady=10)
        
        
        ########### INPUT USER
        # Buat pembungkus untuk untuk inputan user kartu
        tujuan_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
        tujuan_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
        
        # Buat keterangan tentang input
        tujuan_Label = ctk.CTkLabel(tujuan_wrap, text="Nomor Tujuan") # Label Inputan
        tujuan_Label.pack(side='left', padx=10, pady=10)
        
        # buat inputan
        tujuan_input = ctk.CTkEntry(tujuan_wrap, corner_radius=10, placeholder_text="nomor tujuan sesuai bayar yang kamu pilih...", width=300, height=35) # Inputan
        tujuan_input.pack(side='right', padx=10, pady=10)
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
        'bayar' : pilihan_bayar,
        'tujuan': tujuan_input,
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
        
        lanjutBtn = ctk.CTkButton(frame['footer'], height=50,text="Lanjut Cek", command=lambda : bayar_handle(app, frame, inputs, sesi))
        lanjutBtn.pack(side="left", fill='x', expand=True, padx=10)
        
        ######################################### 
        ################################################## FOOTER
    else:
        pass