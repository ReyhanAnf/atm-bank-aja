# Import library eksternal yaitu library TKinter atau CustomTKinter
# import customtkinter as ctk
from tkinter import PhotoImage, Button, Entry, Canvas

from ..setelan import relative_to_assets


LOC = 'masuk'

# Fungsi untuk mengimput data dalam login user
def formulir_masuk(app):
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
    
    # ###################################################### HEADER
    # ##############################################    
    
    # # Buat tampilan judul untuk navigasi
    # title = ctk.CTkButton(frame['header'], text="BANK AJA - MASUK", font=('Arial', 28, 'bold'))
    # title.pack(side="top")
    
    
    header_img = PhotoImage(
    file=relative_to_assets("image_1.png", LOC))
    header = canvas.create_image(
        343.0,
        42.0,
        image=header_img
    )

    logo_img = PhotoImage(
        file=relative_to_assets("image_2.png", LOC))
    logo = canvas.create_image(
        88.0,
        47.0,
        image=logo_img
    )

    canvas.create_text(
        575.0,
        11.0,
        anchor="nw",
        text="Masuk",
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )

    canvas.create_text(
        300.0,
        180.0,
        anchor="nw",
        text="Masuk",
        fill="#000000",
        font=("Poppins SemiBold", 28 * -1)
    )

    
    
    sapaan_img = PhotoImage(
        file=relative_to_assets("image_3.png", LOC))
    sapaan = canvas.create_image(
        344.0,
        137.0,
        image=sapaan_img
    )

    canvas.create_text(
        181.0,
        125.0,
        anchor="nw",
        text="Selamat Datang Di Bank Bangun Mimpi",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # ##############################################    
    # ###################################################### HEADER
    
    
    # ###################################################### BODY
    # ############################################## 
    
    
    # ########### INPUT USER
    # # Buat pembungkus untuk untuk inputan user kartu
    iusernama_img = PhotoImage(file=relative_to_assets("image_4.png", LOC))
    iusernama_bg = canvas.create_image(
        347.0,
        290.0,
        image=iusernama_img
    )
    # # Buat keterangan tentang input
    canvas.create_text(
        67.0,
        222.0,
        anchor="nw",
        text="Usernama atau Nomor Kartu",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # # buat inputan
    iusernama = Entry(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 20)
    )
    iusernama.place( x=54.0,
        y=271.0,
        width=591.0,
        height=37.0
    )
    # ###########

    
    
    
    ######## #INPUT PIN
    # Buat pembungkus untuk inputan pin
    ipin_img = PhotoImage(file=relative_to_assets("image_5.png", LOC))
    ipin_bg = canvas.create_image(
        347.0,
        402.0,
        image=ipin_img
    )
    # Buat keterangan tentang input
    canvas.create_text(
        63.0,
        334.0,
        anchor="nw",
        text="PIN",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # Buat inputan
    ipin = Entry(
        bd=0,
        bg="#DAE1EB",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 20)
    )
    ipin.place(
        x=54.0,
        y=383.0,
        width=591.0,
        height=37.0
    )
    
    # ############
    
    # # Bungkus semua inputan kedalam 1 variabel penampung bertipe dict
    inputs = {
        'usernama': iusernama,
        'pin': ipin,
    }
    # ############################################## 
    # ###################################################### BODY

    
    # ###################################################### FOOTER
    # ############################################ 
    
    ## TOMBOL MASUK
    from .handler_tombol import handle_masuk
    masuk_img = PhotoImage(file=relative_to_assets("button_1.png", LOC))
    masuk_btn = Button(
        image=masuk_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: handle_masuk(inputs),
        relief="flat"
    )
    masuk_btn.place(
        x=466.0,
        y=464.0,
        width=213.0,
        height=67.0
    )

    
    ## TOMBOL DAFTAR
    from ..daftar.main import formulir_daftar
    daftar_img = PhotoImage(file=relative_to_assets("button_2.png", LOC))
    daftar_btn = Button(
        image=daftar_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: formulir_daftar(app),
        relief="flat"
    )
    daftar_btn.place(
        x=228.0,
        y=464.0,
        width=238.0,
        height=64.0
    )

    
    ## TOMBOL KELUAR
    from ..awal.main import home
    keluar_img = PhotoImage(file=relative_to_assets("button_3.png", LOC))
    keluar_btn = Button(
        image=keluar_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: home(app),
        relief="flat"
    )
    keluar_btn.place(
        x=15.0,
        y=462.0,
        width=213.0,
        height=67.0
    )
    
    
    # ############################################ 
    # ###################################################### FOOTER
    
    
    app.resizable(False, False)
    app.mainloop()
    