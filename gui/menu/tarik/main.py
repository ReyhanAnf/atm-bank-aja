
import customtkinter as ctk

from ...setelan import reset_frame
from .handler_tombol import tarik_handler
from ..proses import kembali_ke_home

def tarik(app, frame, sesi):
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
        
        # Buat Judul dengan Navigasi nya dan tampilkan di paling atas
        title = ctk.CTkButton(frame['header'], text="BANK AJA - TARIK TUNAI", font=('Arial', 28, 'bold'))
        title.pack(side="top")
        
        # Buat sapaan kepada user sesuai nama user yang telah melakukan autentikasi
        halo = ctk.CTkLabel(frame['header'], text=f"Hai, {user['nama']}! Masukan data dengan benar!", fg_color="white", text_color='black')
        halo.pack(side='top', fill='x', expand=True, ipadx=10, ipady=10, pady=10)
        
        ######################################### 
        ################################################## HEADER
        
        
        
        ################################################## BODY
        #########################################
        
        
        
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

        # Tampung nominal kedalam variabel inputs
        inputs = {
        'nominal': nominal_input,
        }
 
        ######################################### 
        ################################################## BODY
        
        
        
        ################################################## FOOTER
        ######################################### 
        
        # Buat tombol kembali dan tampilkan
        # Akan menjalankan fungsi kembali_ke_menu
        reset_frame(frame['footer'])
        from ..proses import kembali_ke_menu
        kembaliBtn = ctk.CTkButton(frame['footer'], height=50,text="Kembali", fg_color='orange', text_color='black', command=lambda : kembali_ke_menu(app, frame, sesi))
        kembaliBtn.pack(side="left", fill='x', expand=True, padx=10)
        
        # Buat tombol lanjut dan tampilkan
        # Akan menjalankan fungsi setor_handler untuk melanjutkan setor
        lanjutBtn = ctk.CTkButton(frame['footer'], height=50,text="Lanjut Cek", command=lambda : tarik_handler(app, frame, inputs, sesi))
        lanjutBtn.pack(side="left", fill='x', expand=True, padx=10)
        
        ######################################### 
        ################################################## FOOTER
    else:
        # Jika user belum atau tidak pernah autentikasi maka kembalikan ke home
        kembali_ke_home(app, frame)