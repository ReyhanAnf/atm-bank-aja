# Import library eksternal yaitu library TKinter atau CustomTKinter
from tkinter import PhotoImage, Button, Canvas
# import customtkinter as ctk
# from pathlib import Path

# Import modul internal dari folder lain
# from ..masuk.main import formulir_masuk
# from ..daftar.main import formulir_daftar
# from ..setelan import reset_frame,
from ..setelan import akses_aset_media, reset_frame
from ..masuk.main import formulir_masuk
from ..daftar.main import formulir_daftar

LOC = "awal"

# Fungsi Home - Tampilan awal aplikasi
def home(app):
    # Buat judul aplikasi
    app.title("BANK AJA - GUI")
    app.geometry("687x549")
    # app.geometry("687x549")
    
    # Buat Frame Canvas
    canvas = Canvas(
        app,
        bg = "#EBF3FF",
        height = 549,
        width = 687,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )
    canvas.place(x = 0, y = 0)
    
    ###################################################### HEADER
    ###################################################### 
    
    # Buat tampilan judul untuk navigasi
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
    sapaan_image =PhotoImage(file=akses_aset_media("image_3.png", LOC))
    sapaan = canvas.create_image(
        344.0,
        137.0,
        image=sapaan_image
    )

    # # Tampilkan tampilan judul untuk navigasi
    canvas.create_text(
        181.0,
        125.0,
        anchor="nw",
        text="Selamat Datang Di Bank Bangun Mimpi",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    

    
    ###################################################### 
    ###################################################### HEADER

    
    
    ###################################################### BODY
    ###################################################### 
    
    # Tampilkan Tombol MASUK
    masuk_img =PhotoImage(
        file=akses_aset_media("button_1.png", LOC))
    masuk_btn= Button(
        image=masuk_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: formulir_masuk(app),
        relief="flat"
    )
    masuk_btn.place(
        x=71.0,
        y=215.0,
        width=269.0,
        height=128.0
    )

    
    # Tampilkan Tombol DAFTAR
    daftar_img =PhotoImage(
        file=akses_aset_media("button_2.png", LOC))
    daftar_btn= Button(
        image=daftar_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: formulir_daftar(app),
        relief="flat"
    )
    daftar_btn.place(
        x=340.0,
        y=215.0,
        width=269.0,
        height=128.0
    )

    
    # Tampilkan Tombol KELUAR
    keluar_img = PhotoImage(
        file=akses_aset_media("button_3.png", LOC))
    keluar_btn = Button(
        image=keluar_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: exit(),
        relief="flat"
    )
    keluar_btn.place(
        x=71.0,
        y=351.0,
        width=538.0,
        height=126.0
    )
    ###################################################### 
    ###################################################### BODY

    
    
    
    ###################################################### FOOTER
    ###################################################### 
    
    from ..about import about
    about_img =PhotoImage(
        file=akses_aset_media("button_4.png", LOC))
    about_btn= Button(
        image=about_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: about(app),
        relief="flat"
    )
    about_btn.place(
        x=293.0,
        y=477.0,
        width=101.0,
        height=76.0
    )
    
    ###################################################### 
    ###################################################### FOOTER
    
    app.mainloop()

    