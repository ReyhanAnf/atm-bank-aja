# Import library eksternal yaitu library TKinter atau CustomTKinter
import customtkinter as ctk

# Import module internal
from ..setelan import reset_frame
from .proses import kembali_ke_home

# Import module internal untuk menu
from .info_rekening.main import info_rekening
from .cek_saldo.main import cek_saldo
from .transfer.main import transfer
from .setor.main import setor
from .tarik.main import tarik

# Fungsi utama ketika telah di authentikasi
def dashboard(app, frame, sesi):
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
        
        # Pada frame header akan memunculkan tampilan judul dan sapaan
        # Tampikan Judul dan sapaan halo untuk user yang telah masuk
        
        title = ctk.CTkButton(frame['header'], text="BANK AJA - DASHBOARD", font=('Arial', 28, 'bold'))
        title.pack(side="top")
        
        halo = ctk.CTkLabel(frame['header'], text=f"Hai, {user['nama']}!", fg_color="white", text_color='black')
        halo.pack(side='top', fill='x', expand=True, ipadx=10, ipady=10, pady=10)
        
        ######################################### 
        ################################################## HEADER
        
        
        
        ################################################## BODY
        #########################################
        
        # Pada frame body akan memunculkan menu menu
        ## Frame dibagi menjadi dua untuk memisahkan tombol supaya bisa tampil 2 kolom 4 baris
        
        # Frame 1 untuk menu bagian kiri
        frame1 = ctk.CTkFrame(frame['body'], corner_radius=15, fg_color='transparent')
        frame1.pack(side='left', fill='both', expand=True,  padx=10, pady=10)
        ######### MENU FRAME 1
        # Tombol INfo rekening
        inforek_btn = ctk.CTkButton(frame1, text='Info Rekening', command=lambda : info_rekening(app, frame, sesi))
        inforek_btn.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        
        # Tombol cek saldo
        ceksaldo_btn = ctk.CTkButton(frame1, text='Cek Saldo', command=lambda : cek_saldo(app, frame, sesi))
        ceksaldo_btn.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        
        # Tombol riwayat transaksi
        riwayat_btn = ctk.CTkButton(frame1, text='Riwayat Transaksi')
        riwayat_btn.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        
        # Tombol untuk keluar
        keluar_btn = ctk.CTkButton(frame1, text='Keluar', fg_color='red', command=lambda : kembali_ke_home(app, frame))
        keluar_btn.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        ########## MENU FRAME 1
        
                
        # Frame 2 untuk menu bagian kanan
        frame2 = ctk.CTkFrame(frame['body'], corner_radius=15, fg_color='transparent')
        frame2.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        ######### MENU FRAME 2
        # Tombol transfer
        transfer_btn = ctk.CTkButton(frame2, text='Transfer', command=lambda: transfer(app, frame, sesi))
        transfer_btn.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        
        # Tombol setor
        setor_btn = ctk.CTkButton(frame2, text='Setor Tunai', command=lambda: setor(app, frame, sesi))
        setor_btn.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        
        # Tombol tarik
        tarik_btn = ctk.CTkButton(frame2, text='Tarik Tunai', command=lambda : tarik(app, frame, sesi))
        tarik_btn.pack(side='top', fill='both', expand=True, padx=10, pady=10)
         
        # Tombol bayar
        bayar_btn = ctk.CTkButton(frame2, text='Pembayaran')
        bayar_btn.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        ######### MENU FRAME 2

        
        ######################################### 
        ################################################## BODY
        
        
        
        ################################################## FOOTER
        ######################################### 
        
        ######################################### 
        ################################################## FOOTER
    else:
        pass