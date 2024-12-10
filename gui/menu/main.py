# Import library eksternal yaitu library TKinter atau CustomTKinter
import customtkinter as ctk
from tkinter import Canvas, PhotoImage, Button

# Import module internal
from ..setelan import akses_aset_media
from .proses import kembali_ke_home

# Import module internal untuk menu
from .info_rekening.main import info_rekening
from .cek_saldo.main import cek_saldo
from .transfer.main import transfer
from .setor.main import setor
from .tarik.main import tarik
from .bayar.main import bayar
from .riwayat_transaksi.main import riwayat_transaksi

LOC = 'menu'

# Fungsi utama ketika telah di authentikasi
def dashboard(app, sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    
    # Konfigurasi ukuran dan warna aplikasi
    app.geometry("687x725")
    app.configure(bg = "#EBF3FF")


    # Buat frame canvas
    canvas = Canvas(
        app,
        bg = "#EBF3FF",
        height = 725,
        width = 687,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    # Letakan dan tampilkan frame canvas
    canvas.place(x = 0, y = 0)
    
    
    
    # ################################################## HEADER
    # #########################################
    
    
    # # Pada frame header akan memunculkan tampilan judul dan sapaan
    # # Tampikan Judul dan sapaan halo
    # Buat HEADER
    header_img = PhotoImage(file=akses_aset_media("image_1.png", LOC))
    header = canvas.create_image(
        343.0,
        45.19659423828125,
        image=header_img
    )

    # Buat Judul dan Navigasi MENU
    canvas.create_text(
        581.0,
        11.0,
        anchor="nw",
        text="Menu",
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )

    # Tampilkan LOGO
    logo_img = PhotoImage(file=akses_aset_media("image_2.png", LOC))
    logo = canvas.create_image(
        88.0,
        47.0,
        image=logo_img
    )

    sapaan_img = PhotoImage(file=akses_aset_media("image_3.png", LOC))
    sapaan = canvas.create_image(
        341.0,
        137.0,
        image=sapaan_img
    )

    
    # ######################################### 
    # ################################################## HEADER


    
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    if auth == True:
        # Tampilkan pesan SAPAAN
        canvas.create_text(
            181.0,
            125.0,
            anchor="nw",
            text="Selamat Datang,  Reyhan Andrea Firdaus",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        
        ################################################## BODY
        #########################################
        
        # Pada frame body akan memunculkan menu menu
        
        # Tombol Info Rekening
        # Ketika di Klik akan menjalankan fungsi lamda yang menjalankan fungsi untuk ke menu info rekening
        from .info_rekening.main import info_rekening
        inforek_img = PhotoImage(file=akses_aset_media("button_1.png", LOC))
        inforek_btn = Button(
            image=inforek_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: info_rekening(app, sesi),
            relief="flat"
        )
        inforek_btn.place(
            x=18.0,
            y=179.0,
            width=321.0,
            height=115.0
        )

        
        # Tombol Cek Saldo
        # Ketika di Klik akan menjalankan fungsi lamda yang menjalankan fungsi untuk ke menu cek saldo
        from .cek_saldo.main import cek_saldo
        ceksaldo_img = PhotoImage(file=akses_aset_media("button_2.png", LOC))
        ceksaldo_btn = Button(
            image=ceksaldo_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: cek_saldo(app, sesi),
            relief="flat"
        )
        ceksaldo_btn.place(
            x=18.0,
            y=294.0,
            width=321.0,
            height=115.0
        )

        # Tombol Riwayat Transaksi
        # Ketika di Klik akan menjalankan fungsi lamda yang menjalankan fungsi untuk ke menu riwayat transaksi
        from .riwayat_transaksi.main import riwayat_transaksi
        riwayat_img = PhotoImage(file=akses_aset_media("button_3.png", LOC))
        riwayat_btn = Button(
            image=riwayat_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: riwayat_transaksi(app, sesi),
            relief="flat"
        )
        riwayat_btn.place(
            x=18.0,
            y=409.0,
            width=321.0,
            height=115.0
        )

        
        # Tombol Keluar
        # Ketika di Klik akan menjalankan fungsi lamda yang menjalankan fungsi untuk ke menu keluar
        from ..awal.main import home
        keluar_img = PhotoImage(file=akses_aset_media("button_4.png", LOC))
        keluar_btn = Button(
            image=keluar_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: home(app),
            relief="flat"
        )
        keluar_btn.place(
            x=18.0,
            y=524.0,
            width=321.0,
            height=115.0
        )

        # Tombol Transfer
        # Ketika di Klik akan menjalankan fungsi lamda yang menjalankan fungsi untuk ke menu transfer
        from .transfer.main import transfer
        transfer_img = PhotoImage(file=akses_aset_media("button_5.png", LOC))
        transfer_btn = Button(
            image=transfer_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: transfer(app, sesi),
            relief="flat"
        )
        transfer_btn.place(
            x=351.0,
            y=179.0,
            width=321.0,
            height=115.0
        )

        
        # Tombol Setor
        # Ketika di Klik akan menjalankan fungsi lamda yang menjalankan fungsi untuk ke menu setor
        setor_img = PhotoImage(file=akses_aset_media("button_6.png", LOC))
        setor_btn = Button(
            image=setor_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: setor(app,sesi),
            relief="flat"
        )
        setor_btn.place(
            x=351.0,
            y=294.0,
            width=321.0,
            height=115.0
        )

        
        # Tombol Tarik
        # Ketika di Klik akan menjalankan fungsi lamda yang menjalankan fungsi untuk ke menu tarik
        tarik_img = PhotoImage(file=akses_aset_media("button_7.png", LOC))
        tarik_btn = Button(
            image=tarik_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: tarik(app, sesi),
            relief="flat"
        )
        tarik_btn.place(
            x=351.0,
            y=409.0,
            width=321.0,
            height=115.0
        )

        
        # Tombol Bayar
        # Ketika di Klik akan menjalankan fungsi lamda yang menjalankan fungsi untuk ke menu bayar
        from .bayar.main import bayar
        bayar_img = PhotoImage(file=akses_aset_media("button_8.png", LOC))
        bayar_btn = Button(
            image=bayar_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: bayar(app, sesi),
            relief="flat"
        )
        bayar_btn.place(
            x=351.0,
            y=524.0,
            width=321.0,
            height=115.0
        )

        
        ######################################### 
        ################################################## BODY
        
        
        
        
        
        
        
        
        ################################################## FOOTER
        ######################################### 
        
        ######################################### 
        ################################################## FOOTER
    else:
        # Jika user belum atau tidak pernah autentikasi maka kembalikan ke home
        # kembali_ke_home(app, frame)
        canvas.create_text(
            181.0,
            125.0,
            anchor="nw",
            text="Anda Belum Login",
            fill="red",
            font=("Poppins Medium", 16 * -1)
        )
        
    
    
    app.resizable(False, False)
    app.mainloop()