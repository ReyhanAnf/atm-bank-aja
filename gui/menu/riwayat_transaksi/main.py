# Import library eksternal yaitu library TKinter atau CustomTKinter
from tkinter import  Canvas, PhotoImage, ttk, Scrollbar, Frame, Button

# Import module internal untuk menu
from ...pendataan.transaksi import data_transaksi
from ...setelan import akses_aset_media

LOC = "riwayat_transaksi"

# Buat fungsi Riwayat Transaksi untuk menampilkan transaksi dalam bentuk tabel
def riwayat_transaksi(app, sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    app.geometry("1418x702")
    app.configure(bg = "#EBF3FF")


    canvas = Canvas(
        app,
        bg = "#EBF3FF",
        height = 702,
        width = 1418,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    
    ################################################## HEADER
    #########################################
    
    # Buat Judul dengan Navigasi nya dan tampilkan di paling atas
    image_image_1 = PhotoImage(
        file=akses_aset_media("image_1.png", LOC))
    image_1 = canvas.create_image(
        709.0,
        44.0,
        image=image_image_1
    )

    canvas.create_text(
        1127.0,
        11.0,
        anchor="nw",
        text="Riwayat Transaksi",
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )

    image_image_2 = PhotoImage(
        file=akses_aset_media("image_2.png", LOC))
    image_2 = canvas.create_image(
        88.0,
        47.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=akses_aset_media("image_3.png", LOC))
    image_3 = canvas.create_image(
        703.0,
        132.0,
        image=image_image_3
    )

    ######################################### 
    ################################################## HEADER
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    if auth == True:
        
        ################################################## BODY
        #########################################
        
        canvas.create_text(
            550.0,
            120.0,
            anchor="nw",
            text=f"Selamat Datang,  {user.nama}",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        
        # Ambil data transaksi dari module pendataan
        df = data_transaksi()
        
        # Sorting data
        # Ambil data ketika data tersebut mengandung user ini (user yang telah login)
        # Baik itu sebagai penerima atau pengirim dalam transaksi
        # Jadi data akan menampilkan data yang pengirim atau penerimanya user ini saja
        df = df[(df['pengirim'] == user['usernama']) | (df['penerima'] == user['usernama'])].reset_index(drop=True)

        # Urutkan dari yang terbaru dengan metode descending
        df = df.sort_values(by=['waktu'], ascending=False).reset_index(drop=True)
        
        # Ubah Data yang bersifat uang menjadi tipe mata uang
        def uang(nominal):
            if type(nominal) == type(1):
                return f'Rp {int(nominal):,}'.replace(',','.')
            else:
                return nominal
        
        # Masukan fungsi uang kedalam data (MIRIP EXCEL)
        # fungsi apply map bertujuan untuk meng apply fungsi kesetiap data
        df = df.map(uang)
        
        # Ambil jumlah baris dan kolom
        n_rows = df.shape[0] 
        n_cols = df.shape[1] 
        
        # Ambil data list dari kolom yang ada pada database atau data
        column_names = df.columns

        # Buat tampilan Frame yang bisa di scroll untuk diisi oleh tabel data
        wframe = 1300
        hframe = 500
        
        frame = Frame(app, width=wframe, height=hframe)
        frame.place(x=55, y=200, height=340, width=1300)

        style = ttk.Style(frame)
        style.theme_use("clam")
        # Menambahkan gaya khusus
        style.configure(
            "Treeview",
            font=("Poppins", 10),
            rowheight=30,  # Tinggi baris
            borderwidth=0,
            background="#EBF3FF",
            fieldbackground="#EBF3FF",
        )
        style.configure(
            "Treeview.Heading",
            font=("Poppins", 11, "bold"),
            background="#56D1BF",
            foreground="black",
            relief="flat",
        )
        style.map(
            "Treeview.Heading",
            background=[("active", "#56D1BF")],
        )


        # BUAT TABEL
        tabel = ttk.Treeview(frame)
        tabel.place(relheight=1, relwidth=1)
        # x=55, y=200

        treescrolly = Scrollbar(frame, orient='vertical', command=tabel.yview)
        treescrollx = Scrollbar(frame, orient='horizontal', command=tabel.xview)
        tabel.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)

        # Masukan data kolom ke dalam display tabel
        tabel['columns'] = column_names
        
        # Lebar kolom adalah lebar tabel dibagi jumlah kolom
        wcol = int(wframe/n_cols)
        
        # Setiap kolom dicetak didalam satu baris yang sama
        for c in range(n_cols):
            tabel.column("#{}".format(c), width=wcol)
            tabel.heading('#{}'.format(c), text=column_names[c])
        
        # Buat perulangan sesuai jumlah baris untuk menampilkan isi data
        for r in range(n_rows):
            data = []
            for j in df.iloc[r]:
                data.append(j)
            
            kode = data[0]
            data.pop(0)
            tabel.insert("", 'end', text = kode, values = tuple(data))
         
        ######################################### 
        ################################################## BODY
        
        
        
        ################################################## FOOTER
        ######################################### 
        
        # Buat tombol kembali dan tampilkan
        # Akan menjalankan fungsi yang mengarah kembali ke menu atau keluar
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
            x=377.0,
            y=564.0,
            width=321.0,
            height=115.0
        )

        # TO<MBOL KE MENU
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
            x=710.0,
            y=564.0,
            width=321.0,
            height=115.0
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
