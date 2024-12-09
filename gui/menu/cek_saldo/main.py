# Import library eksternal yaitu library TKinter atau CustomTKinter
from tkinter import Canvas, Button, PhotoImage

# Import module internal untuk menu
from ...setelan import akses_aset_media
from ...kartu import saldo
from ...pendataan.user import cek_user_kartu

LOC = 'cek_saldo'

# Buat fungsi info_rekening untuk menampilkan informasi rekening
def cek_saldo(app, sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    app.geometry("687x702")
    app.configure(bg = "#EBF3FF")


    canvas = Canvas(
        app,
        bg = "#EBF3FF",
        height = 702,
        width = 687,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    
    ################################################## HEADER
    #########################################
    # Buat Judul dengan Navigasi nya dan tampilkan di paling atas
    # Buat sapaan kepada user sesuai nama user yang telah melakukan autentikasi
    
    header_img = PhotoImage(file=akses_aset_media("image_1.png", LOC))
    header = canvas.create_image(
        343.0,
        44.0,
        image=header_img
    )

    canvas.create_text(
        398.0,
        11.0,
        anchor="nw",
        text="Informasi Rekening",
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )

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
    
    
    ######################################### 
    ################################################## HEADER
    
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    if auth == True:
           
        canvas.create_text(
            181.0,
            125.0,
            anchor="nw",
            text=f"Selamat Datang,  {user.nama}",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )

        
        ################################################## BODY
        #########################################
        
        # Update saldo terlebih dahulu untuk mendapatkan saldo terbaru
        saldo_update = cek_user_kartu(user['usernama'])['saldo']
        user['saldo'] = saldo_update
        
        # BUAT KARTUU
        kartu_img = PhotoImage(file=akses_aset_media("atm.png", 'kartu'))
        kartu = canvas.create_image(
            365.0,
            377.0,
            image=kartu_img
        )
        saldo(canvas, user)

 
        # ######################################### 
        # ################################################## BODY
        
        
        
        # ################################################## FOOTER
        # ######################################### 
        
        # Buat tombol kembali dan tampilkan
        # Akan menjalankan fungsi kembali_ke_menu
        # BUAT TOMBOL KELUAR
        from ...awal.main import home
        keluar_img = PhotoImage(file=akses_aset_media("button_1.png", LOC))
        keluar_btn = Button(
            image=keluar_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: home(app),
            relief="flat"
        )
        keluar_btn.place(
            x=17.0,
            y=569.0,
            width=321.0,
            height=115.0
        )

        # BUAT TOMBOL KEMBALI KE MENU
        from ..main import dashboard
        menu_img = PhotoImage(
            file=akses_aset_media("button_2.png", LOC))
        menu_btn = Button(
            image=menu_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: dashboard(app, sesi),
            relief="flat"
        )
        menu_btn.place(
            x=350.0,
            y=569.0,
            width=321.0,
            height=115.0
        )
        
        ######################################### 
        ################################################## FOOTER
    else:
        # Jika user belum atau tidak pernah autentikasi maka kembalikan ke home
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