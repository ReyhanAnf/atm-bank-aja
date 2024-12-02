# Import library eksternal yaitu library TKinter atau CustomTKinter
import customtkinter as ctk

# Import module internal untuk menu
from ...setelan import reset_frame
from ...daftar.proses import kartu_atm
from ...pendataan.user import cek_user_kartu
from ..proses import kembali_ke_home

# Buat fungsi info_rekening untuk menampilkan informasi rekening
def info_rekening(app, frame, sesi):
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
        title = ctk.CTkButton(frame['header'], text="BANK AJA - INFO REKENING", font=('Arial', 28, 'bold'))
        title.pack(side="top")
        
        # Buat sapaan kepada user sesuai nama user yang telah melakukan autentikasi
        halo = ctk.CTkLabel(frame['header'], text=f"Hai, {user['nama']}!", fg_color="white", text_color='black')
        halo.pack(side='top', fill='x', expand=True, ipadx=10, ipady=10, pady=10)
        
        ######################################### 
        ################################################## HEADER
        
        
        
        ################################################## BODY
        #########################################
        
        # Update saldo terlebih dahulu untuk mendapatkan saldo terbaru
        saldo_update = cek_user_kartu(user['usernama'])['saldo']
        user['saldo'] = saldo_update
        
        # Cetak ATM
        kartu_atm(app, frame, user)

 
        ######################################### 
        ################################################## BODY
        
        
        
        ################################################## FOOTER
        ######################################### 
        
        # Buat tombol kembali dan tampilkan
        # Akan menjalankan fungsi kembali_ke_menu
        reset_frame(frame['footer'])
        from ..proses import kembali_ke_menu
        kembaliBtn = ctk.CTkButton(frame['footer'], height=50, text="Kembali", fg_color='orange', text_color='black', command=lambda : kembali_ke_menu(app, frame, sesi))
        kembaliBtn.pack(side="left", fill='x', expand=True, padx=10)
        
        ######################################### 
        ################################################## FOOTER
    else:
        # Jika user belum atau tidak pernah autentikasi maka kembalikan ke home
        kembali_ke_home(app, frame)