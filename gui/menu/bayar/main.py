from tkinter import Canvas, PhotoImage, Button, Entry, StringVar, ttk

from ...setelan import akses_aset_media

LOC = 'bayar'

def bayar(app, sesi):
    
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
    
    
    heading_img = PhotoImage(file=akses_aset_media("image_1.png", LOC))
    heading = canvas.create_image(
        343.0,
        42.0,
        image=heading_img
    )

    logo_img = PhotoImage(file=akses_aset_media("image_2.png", LOC))
    logo = canvas.create_image(
        88.0,
        47.0,
        image=logo_img
    )

    # NAVIGASI
    canvas.create_text(
        566.0,
        11.0,
        anchor="nw",
        text="Bayar",
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )

    # NAVIGASI
    canvas.create_text(
        305.0,
        169.0,
        anchor="nw",
        text="Bayar",
        fill="#000000",
        font=("Poppins SemiBold", 28 * -1)
    )

    sapaan_img = PhotoImage(file=akses_aset_media("image_3.png", LOC))
    sapaan = canvas.create_image(
        344.0,
        137.0,
        image=sapaan_img
    )

    # TEKS SAPAAN
    canvas.create_text(
        181.0,
        125.0,
        anchor="nw",
        text="Selamat Datang Di Bank Bangun Mimpi",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    if auth == True:
        ################################################## BODY
        #########################################
        
        
        ############# TAMPILKAN LABEL INPUTAN NOMOR TUJUAN
        canvas.create_text(
            63.0,
            222.0,
            anchor="nw",
            text="Nomor Tujuan",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        # BUAT BACKGROUND UNTUK INPUTAN NOMOR TUJUAN
        itujuan_img = PhotoImage(file=akses_aset_media("image_4.png", LOC))
        itujuan_bg = canvas.create_image(
            240.0,
            290.0,
            image=itujuan_img
        )

        # BUAT INPUTAN NOMOR TUJUAN
        itujuan = Entry(
            bd=0,
            bg="#DAE1EB",
            fg="#000716",
            highlightthickness=0,
            font= ("Poppins", 14 * -1)
        )
        # TAMPILKAN INPUTAN NOMOR TUJUAN
        itujuan.place(
            x=48.0,
            y=271.0,
            width=387.0,
            height=37.0
        )
        
        
        ########### TAMPILKAN LABEL BAYAR
        canvas.create_text(
            466.0,
            222.0,
            anchor="nw",
            text="Bayar",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        # BUAT BACKGROUND UNTUK BAYAR
        ibayar_img = PhotoImage(
            file=akses_aset_media("image_5.png", LOC))
        ibayar_bg = canvas.create_image(
            560.0,
            290.0,
            image=ibayar_img
        )
        
        # BUAT DAFTAR MENU BAYAR
        menu = ['PLN Paska', 'PLN Token', 'PDAM',  'Virtual Account', 'Pulsa', 'BPJS', 'TopUp Gopay', 'TopUp Shopeepay', 'TopUp Ovo', 'Keluar']
        # BUAT SELECTION/PILIHAN BAYAR
        ibayar_var = StringVar(value=menu[0])
        ibayar = ttk.Combobox(
            canvas,
            textvariable=ibayar_var,
            background="#DAE1EB",
            foreground="#000716",
            font= ("Poppins", 14 * -1)
        )
        # SET VALUES IBAYAR DENGAN DAFTAR MENU
        ibayar['values'] = tuple(menu)
        # TAMPILKAN BAYAR
        ibayar.place(
            x=468.0,
            y=271.0,
            width=185.0,
            height=37.0
        )
        

        #############
        # TAMPILKAN LABEL INPUTAN NOMINAL
        canvas.create_text(
            63.0,
            334.0,
            anchor="nw",
            text="Nominal",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        # TAMPILKAN RP
        canvas.create_text(
            47.0,
            390.0,
            anchor="nw",
            text="Rp",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        
        # BUAT BACKGROUND UNTUK INPUTAN NOMINAL
        inominal_img = PhotoImage(
            file=akses_aset_media("image_6.png", LOC))
        inominal_bg = canvas.create_image(
            347.0,
            402.0,
            image=inominal_img
        )
        # BUAT INPUTAN NOMINAL
        inominal = Entry(
            bd=0,
            bg="#DAE1EB",
            fg="#000716",
            highlightthickness=0,
            font= ("Poppins", 14 * -1)
        )
        # TAMPILKAN INPUTAN NOMINAL
        inominal.place(
            x=97.0,
            y=383.0,
            width=548.0,
            height=37.0
        )
        
                

        # Tampung semua inputan kedalam variabel inputs
        inputs = {
            'bayar' : ibayar,
            'tujuan': itujuan,
            'nominal': inominal,
        }
 
        ######################################### 
        ################################################## BODY
        
        
        
        ################################################## FOOTER
        ######################################### 
        
        
        ## TOMBOL LANJUT
        from .handler_tombol import bayar_handle
        lanjut_img = PhotoImage(file=akses_aset_media("button_1.png", LOC))
        lanjut_btn = Button(
            image=lanjut_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: bayar_handle(app, canvas, sesi, inputs),
            relief="flat"
        )
        lanjut_btn.place(
            x=466.0,
            y=464.0,
            width=213.0,
            height=67.0
        )

        ## TOMBOL MENU
        from ..main import dashboard
        menu_img = PhotoImage(file=akses_aset_media("button_2.png", LOC))
        menu_btn = Button(
            image=menu_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: dashboard(app, sesi),
            relief="flat"
        )
        menu_btn.place(
            x=228.0,
            y=464.0,
            width=238.0,
            height=64.0
        )

        ## TOMBOL KELUAR
        from ...awal.main import home
        keluar_img = PhotoImage(file=akses_aset_media("button_3.png", LOC))
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