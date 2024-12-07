# Import library eksternal yaitu library TKinter atau CustomTKinter
from tkinter import PhotoImage, Button, Canvas
# import customtkinter as ctk
# from pathlib import Path

# Import modul internal dari folder lain
# from ..masuk.main import formulir_masuk
# from ..daftar.main import formulir_daftar
# from ..setelan import reset_frame,
from ..setelan import relative_to_assets, reset_frame
from ..masuk.main import formulir_masuk
from ..daftar.main import formulir_daftar

LOC = "awal"

# Fungsi Home - Tampilan awal aplikasi
def home(app):
    # Buat judul aplikasi
    # app.title("BANK AJA - GUI")
    # app.geometry("687x549")
    # app.configure(bg = "#EBF3FF")
    
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
    
    # Reset semua frame utama agar bersih dari widget lain
    # reset_frame(frame['header'])
    # reset_frame(frame['body'])
    # reset_frame(frame['footer'])
    
    header_img = PhotoImage(file=relative_to_assets("image_1.png", LOC))
    header = canvas.create_image(
        343.0,
        42.0,
        image=header_img
    )

    logo_img = PhotoImage(file=relative_to_assets("image_2.png", LOC))
    logo = canvas.create_image(
        88.0,
        47.0,
        image=logo_img
    )
    
    sapaan_image =PhotoImage(file=relative_to_assets("image_3.png", LOC))
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

    
    masuk_img =PhotoImage(
        file=relative_to_assets("button_1.png", LOC))
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

    
    daftar_img =PhotoImage(
        file=relative_to_assets("button_2.png", LOC))
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

    
    keluar_img = PhotoImage(
        file=relative_to_assets("button_3.png", LOC))
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

    
    about_img =PhotoImage(
        file=relative_to_assets("button_4.png", LOC))
    about_btn= Button(
        image=about_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("about_btn clicked"),
        relief="flat"
    )
    about_btn.place(
        x=293.0,
        y=477.0,
        width=101.0,
        height=76.0
    )
    
    app.mainloop()
    ###################################################### HEADER
    ###################################################### 
    
    
    # Buat tampilan judul untuk navigasi
    # title = ctk.CTkButton(frame['header'], text="BANK AJA - HOME", font=('Arial', 28, 'bold'))
    # # Tampilkan tampilan judul untuk navigasi
    # title.pack(side="top")
    
    ###################################################### 
    ###################################################### HEADER
    
    
    
    ###################################################### BODY
    ###################################################### 
    
    #Sapaan
    # sapaan = ctk.CTkLabel(frame['body'], text="Halo! Selamat Datang Di BANK AJA. Silahkan Masuk atau Mendaftar")
    # # Tampilkan Sapaan
    # sapaan.pack(side="top", fill='x')
    
    ###################################################### 
    ###################################################### BODY
    
    
    
    ###################################################### FOOTER
    ###################################################### 
    
    # Buat tombol masuk
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol masuk di klik maka akan masuk ke fungsi lambda yang mengeksekusi fungsi formulir masuk
    # masukBtn = ctk.CTkButton(frame['footer'], height=50,text="Masuk", command=lambda : formulir_masuk(app, frame))
    # # Tampilkan tombol
    # masukBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    # Buat tombol daftar
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol daftar di klik maka akan menjalankan ke fungsi lambda yang mengeksekusi fungsi formulir daftar
    # daftarBtn = ctk.CTkButton(frame['footer'], height=50,text="Daftar", fg_color='blue', command=lambda : formulir_daftar(app, frame))
    # # Tampilkan tombol
    # daftarBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    # Buat tombol keluar
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol keluar di klik maka akan menjalankan ke fungsi lambda yang mengeksekusi fungsi formulir keluar
    # keluarBtn = ctk.CTkButton(frame['footer'], height=50,text="Keluar", fg_color='red', command=exit)
    # # Tampilkan tombol
    # keluarBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    ###################################################### 
    ###################################################### FOOTER


    