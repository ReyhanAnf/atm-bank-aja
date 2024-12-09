# Import library eksternal yaitu library TKinter atau CustomTKinter
# import customtkinter as ctk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import customtkinter as ctk

from ..setelan import akses_aset_media
# Import module internal
# from ..setelan import reset_frame
# from .handler_tombol import kembali_ke_home, handle_daftar

LOC = "daftar"

# Fungsi untuk mengimput data dalam pendaftaran user
def formulir_daftar(app):
    
    # Buat judul aplikasi
    app.title("BANK AJA - GUI")
    
    
    
    # ###################################################### HEADER
    # ######################################################
    
    
    
    app.geometry("687x800")
    app.configure(bg = "#EBF3FF")
    canvas = Canvas(
        app,
        bg = "#EBF3FF",
        height = 800,
        width = 687,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)
    
    # # Buat tampilan judul untuk navigasi
    # # Tampilkan tampilan judul untuk navigasi
    
    header_img = PhotoImage(file=akses_aset_media("image_1.png", LOC))
    header = canvas.create_image(
        343.0,
        42.0,
        image=header_img
    )
    
    logo_img = PhotoImage(file=akses_aset_media("image_2.png", LOC))
    logo = canvas.create_image(
        88.0,
        47.0,
        image=logo_img
    )
    
    canvas.create_text(
        576.0,
        11.0,
        anchor="nw",
        text="Daftar",
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )
    
    sapaan_image =PhotoImage(file=akses_aset_media("image_3.png", LOC))
    sapaan = canvas.create_image(
        344.0,
        137.0,
        image=sapaan_image
    )
    canvas.create_text(
        181.0,
        125.0,
        anchor="nw",
        text="Selamat Datang Di Bank Bangun Mimpi",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    

    
    
    # ######################################################
    # ###################################################### HEADER
    



    
    # ###################################################### BODY
    # ######################################################


    ########### INPUT USERNAMA
    # Buat pembungkus untuk untuk inputan usernama
    iusernama_img = PhotoImage(
        file=akses_aset_media("image_4.png", LOC))
    iusernama_bg = canvas.create_image(
        185.0,
        227.0,
        image=iusernama_img
    )
    
    # Buat keterangan tentang input
    # Tampilkan keterangan tentang input
    canvas.create_text(
        45.0,
        175.0,
        anchor="nw",
        text="Usernama",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    # buat inputan
    iusernama = Entry(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0,
        font= ("Poppins", 16 * -1)
    )
    # Tampilkan inputan
    iusernama.place(
        x=49.0,
        y=209.0,
        width=272.0,
        height=35.28813552856445
    )


    ########### INPUT NAMA
    # Buat pembungkus untuk untuk inputan nama
    inama_img = PhotoImage(file=akses_aset_media("image_5.png", LOC))
    inama_bg = canvas.create_image(
        185.0,
        302.0,
        image=inama_img
    )
    # Tampilkan pembungkus untuk untuk inputan usernama
    
    # Buat keterangan tentang input
    canvas.create_text(
        45.0,
        256.0,
        anchor="nw",
        text="Nama Lengkap",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # Tampilkan keterangan tentang input

    # buat inputan
    inama = Entry(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0,
        font= ("Poppins", 16 * -1)
    )
    # tampilkan inputan
    inama.place(
        x=49.0,
        y=284.0,
        width=272.0,
        height=35.28813552856445
    )


    ######## #INPUT EMAIL
    # Buat pembungkus untuk inputan email
    iemail_img = PhotoImage(file=akses_aset_media("image_6.png", LOC))
    iemail_bg = canvas.create_image(
        185.0,
        377.0,
        image=iemail_img
    )
    # Tampilkan pembungkus untuk inputan email
    
    # Buat keterangan tentang input
    canvas.create_text(
        44.0,
        331.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # Tampilkan keterangan tentang input
    # Buat inputan
    iemail = Entry(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0,
        font= ("Poppins", 16 * -1)
    )
    # Tampilkan inputan
    iemail.place(
        x=49.0,
        y=359.0,
        width=272.0,
        height=35.28813552856445
    )

    
    ######## #INPUT No HP
    # Buat pembungkus untuk inputan nomor hp
    # Tampilkan pembungkus untuk inputan nomor hp
    inohp_img = PhotoImage(file=akses_aset_media("image_7.png", LOC))
    inohp = canvas.create_image(
        185.0,
        452.0,
        image=inohp_img
    )
        
    # Buat keterangan tentang input
    # Tampilkan keterangan tentang input
    canvas.create_text(
        45.0,
        406.0,
        anchor="nw",
        text="Nomor HP",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # Buat inputan
    inohp = Entry(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0,
        font= ("Poppins", 16 * -1)
    )
    # Tampilkan inputan
    inohp.place(
        x=49.0,
        y=434.0,
        width=272.0,
        height=35.28813552856445
    )
        
    
    ############# INPUT ANGGOTA
    canvas.create_text(
        45.0,
        482.0,
        anchor="nw",
        text="Anggota",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    # Buat dan tampilkan Pilihan
    anggota_var = ctk.StringVar(value='gold') # Variabel penampung
    # Pilihan 1
    a_silver = ctk.CTkRadioButton(app, text="Silver", width=90.0, height=35.28813552856445, value='silver', variable=anggota_var, text_color="black") # Inputan
    a_silver.place( x=49.0, y=509.0 )
    
    # Pilihan 2
    a_gold = ctk.CTkRadioButton(app, width=90.0, height=35.28813552856445, text="Gold", value='gold', variable=anggota_var, text_color="black") # Inputan
    a_gold.place( x=149.0, y=509.0 )
    # Pilihan 3
    a_platinum = ctk.CTkRadioButton(app, text="Platinum" , width=90.0, height=35.28813552856445, value='platinum', variable=anggota_var, text_color="black") # Inputan
    a_platinum.place( x=249.0, y=509.0 )



    ######## #INPUT TANGGAL LAHIR
    # Buat pembungkus untuk inputan tanggal lahir
    ilahir_img = PhotoImage(file=akses_aset_media("image_9.png", LOC))
    # Buat pembungkus untuk inputan tanggal lahir
    ilahir_bg = canvas.create_image(
        185.0,
        602.0,
        image=ilahir_img
    )
    # Buat keterangan tentang input
    # Tampilkan keterangan tentang input
    canvas.create_text(
        46.0,
        558.0,
        anchor="nw",
        text="Tanggal Lahir",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # Buat inputan
    ilahir = Entry(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0,
        font= ("Poppins", 16 * -1)
    )
    # Tampilkan inputan
    ilahir.place(
        x=49.0,
        y=584.0,
        width=272.0,
        height=35.28813552856445
    )



    ########### INPUT ALAMAT
    # Buat pembungkus untuk untuk inputan saldo
    # Tampilkan pembungkus untuk untuk inputan saldo

    # Buat keterangan tentang input
    # Tampilkan keterangan tentang input

    # buat inputan
    # Tampilkan inputan
    canvas.create_text(
        385.0,
        175.0,
        anchor="nw",
        text="Alamat",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    ialamat_img = PhotoImage(
        file=akses_aset_media("image_10.png", LOC))
    ialamat_bg = canvas.create_image(
        517.0,
        264.0,
        image=ialamat_img
    )

    ialamat = Text(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0
    )
    ialamat.place(
        x=386.0,
        y=219.0,
        width=266.0,
        height=89.0
    )


    # ######## #INPUT PIN
    # # Buat pembungkus untuk inputan pin
    ipin_img = PhotoImage( file=akses_aset_media("image_11.png", LOC))
    ipin_bg = canvas.create_image(
        517.0,
        373.0,
        image=ipin_img
    )
    # # Tampilkan pembungkus untuk inputan pin
    
    # # Buat keterangan tentang input
    canvas.create_text(
        385.0,
        326.0,
        anchor="nw",
        text="PIN",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # # Tampilkan keterangan tentang input
    
    # # Buat inputan
    ipin = Entry(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0,
        font= ("Poppins", 16 * -1)
    )
    # # Tampilkan inputan
    ipin.place(
        x=385.0,
        y=355.0,
        width=265.0,
        height=35.0
    )
    
    
    # ######## #INPUT KONFIRMASI PIN
    # # Buat pembungkus untuk inputan pin
    ikpin_img = PhotoImage(
        file=akses_aset_media("image_12.png", LOC))
    ikpin_bg = canvas.create_image(
        517.0,
        448.0,
        image=ikpin_img
    )
    # # Tampilkan pembungkus untuk inputan pin
    
    # # Buat keterangan tentang input
    canvas.create_text(
        385.0,
        399.0,
        anchor="nw",
        text="Konfirmasi PIN",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # # Tampilkan keterangan tentang input
    
    # # Buat inputan
    ikpin = Entry(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0,
        font= ("Poppins", 16 * -1)
    )
    # # Tampilkan inputan
    ikpin.place(
        x=385.0,
        y=430.0,
        width=265.0,
        height=35.0
    )
    

    ########### INPUT SALDO
    # Buat pembungkus untuk untuk inputan saldo
    isaldo_img = PhotoImage(file=akses_aset_media("image_13.png", LOC))
    isaldo_bg = canvas.create_image(
        517.0,
        602.0,
        image=isaldo_img
    )
    # Tampilkan pembungkus untuk untuk inputan saldo

    # Buat keterangan tentang input
    canvas.create_text(
        385.0,
        549.0,
        anchor="nw",
        text="Saldo Awal",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # Tampilkan keterangan tentang input
    canvas.create_text(
        378.0,
        591.0,
        anchor="nw",
        text="Rp",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # buat inputan
    isaldo = Entry(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0,
        font= ("Poppins", 16 * -1)
    
    )
    # Tampilkan inputan
    isaldo.place(
        x=414.0,
        y=584.0,
        width=236.0,
        height=35.0
    )

    # Bungkus semua inputan kedalam 1 variabel penampung bertipe dict
    inputs = {
        'nama': inama,
        'usernama': iusernama,
        'email' : iemail,
        'no_hp': inohp,
        'anggota': anggota_var,
        'lahir': ilahir,
        'alamat': ialamat,
        'pin': ipin,
        'kpin': ikpin,
        'saldo' : isaldo
    }
    
    ######################################################
    ###################################################### BODY

    
    ###################################################### FOOTER
    ###################################################### 
    
    # Buat tombol Keluar
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol batal di klik maka akan batal ke fungsi lambda yang mengeksekusi fungsi kembali ke home
    from ..awal.main import home
    keluar_img = PhotoImage(
        file=akses_aset_media("button_3.png", LOC))
    keluar_btn = Button(
        image=keluar_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: home(app),
        relief="flat"
    )
    keluar_btn.place(
        x=12.0,
        y=715.0,
        width=213.0,
        height=67.0
    )
    # Tampilkan tombol
    
    # Buat tombol daftar
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol daftar di klik maka akan daftar ke fungsi lambda yang mengeksekusi fungsi handle daftar
    from .handler_tombol import handle_daftar
    
    daftar_img = PhotoImage(
        file=akses_aset_media("button_1.png", LOC))
    daftar_btn = Button(
        image=daftar_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: handle_daftar(inputs, canvas),
        relief="flat"
    )
    daftar_btn.place(
        x=463.0,
        y=717.0,
        width=213.0,
        height=67.0
    )
    # Tampilkan tombol
    

    
    # Buat tombol masuk
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol daftar di klik maka akan daftar ke fungsi lambda yang mengeksekusi fungsi handle daftar
    from ..masuk.main import formulir_masuk
    
    masuk_img = PhotoImage(
        file=akses_aset_media("button_2.png", LOC))
    masuk_btn = Button(
        image=masuk_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: formulir_masuk(app),
        relief="flat"
    )
    masuk_btn.place(
        x=225.0,
        y=717.0,
        width=238.0,
        height=64.0
    )

    
    ###################################################### 
    ###################################################### FOOTER
    
    app.resizable(False, False)
    app.mainloop()