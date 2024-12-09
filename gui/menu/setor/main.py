from tkinter import  Canvas, Entry, Button, PhotoImage

from ...setelan import akses_aset_media

LOC = 'setor'

def setor(app, sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    app.geometry("687x549")
    app.configure(bg = "#EBF3FF")


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
    ################################################## HEADER
    #########################################
    
    # Buat Judul dengan Navigasi nya dan tampilkan di paling atas)
    
    image_image_1 = PhotoImage(
        file=akses_aset_media("image_1.png", LOC))
    image_1 = canvas.create_image(
        343.0,
        42.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=akses_aset_media("image_2.png", LOC))
    image_2 = canvas.create_image(
        88.0,
        47.0,
        image=image_image_2
    )

    canvas.create_text(
        550.0,
        11.0,
        anchor="nw",
        text="Setor",
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )

    canvas.create_text(
        295.0,
        180.0,
        anchor="nw",
        text="Setor",
        fill="#000000",
        font=("Poppins SemiBold", 28 * -1)
    )

    # Buat sapaan kepada user sesuai nama user yang telah melakukan autentikasi
    sapaan_img = PhotoImage(
        file=akses_aset_media("image_3.png", LOC))
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
        
        ######################################### 
        ################################################## HEADER
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    if auth == True:
        
        
        ################################################## BODY
        #########################################
        
        
        
        ######## #INPUT JUMLAH
        # Buat pembungkus untuk inputan jumlah
        inominal_img = PhotoImage(file=akses_aset_media("image_4.png", LOC))
        inominal_bg = canvas.create_image(
            351.0,
            313.5,
            image=inominal_img
        )

        # Buat inputan
        inominal = Entry(
            bd=0,
            bg="#DAE1EB",
            fg="#000716",
            highlightthickness=0,
            font=("Poppins Medium", 14 * -1)
        )
        inominal.place(
            x=97.0,
            y=294.0,
            width=548.0,
            height=37.0
        )

        # Buat keterangan tentang input
        canvas.create_text(
            63.0,
            245.0,
            anchor="nw",
            text="Nominal",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        
        canvas.create_text(
            47.0,
            301.0,
            anchor="nw",
            text="Rp",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        ############

        # Tampung nominal kedalam variabel inputs
        inputs = {
        'nominal': inominal,
        }
 
        ######################################### 
        ################################################## BODY
        
        
        
        ################################################## FOOTER
        ######################################### 
        
        

        # Buat tombol kembali dan tampilkan
        # Akan menjalankan fungsi kembali_ke_menu
        from .handler_tombol import setor_handler
        lanjut_img = PhotoImage(
            file=akses_aset_media("button_1.png", LOC))
        lanjut_btn = Button(
            image=lanjut_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: setor_handler(app,canvas, sesi, inputs),
            relief="flat"
        )
        lanjut_btn.place(
            x=466.0,
            y=464.0,
            width=213.0,
            height=67.0
        )

        from ..main import dashboard
        menu_img = PhotoImage(
            file=akses_aset_media("button_2.png", LOC))
        menu_btn = Button(
            image=menu_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: dashboard(app,sesi),
            relief="flat"
        )
        menu_btn.place(
            x=228.0,
            y=464.0,
            width=238.0,
            height=64.0
        )

        from ...awal.main import home
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
            x=15.0,
            y=462.0,
            width=213.0,
            height=67.0
        )
        
        
        # Buat tombol lanjut dan tampilkan
        # Akan menjalankan fungsi setor_handler untuk melanjutkan setor
        
        ######################################### 
        ################################################## FOOTER
    else:
        # Jika user belum atau tidak pernah autentikasi maka kembalikan ke home
        canvas.create_text(
            550.0,
            120.0,
            anchor="nw",
            text="ANDA BELUM MASUK",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        
    app.resizable(False, False)
    app.mainloop()