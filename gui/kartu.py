from tkinter import Tk, Canvas, Button, PhotoImage, ttk, Scrollbar, Frame


def atm(canvas, user):

    # BUAT TAMPILAN NOMOT KARTU
    canvas.create_text(
        341.0,
        434.0,
        anchor="nw",
        text= ' '.join(f"{user.nomor_kartu}"),
        fill="#000000",
        font=("Poppins SemiBold", 32 * -1)
    )
    
    # BUAT TAMPILAN NOMOT SERI
    canvas.create_text(
        104.0,
        479.0,
        anchor="nw",
        text= user.kode_seri,
        fill="#000000",
        font=("Poppins SemiBold", 24 * -1)
    )

    # BUAT TAMPILAN SALDO
    canvas.create_text(
        104.0,
        371.0,
        anchor="nw",
        text=f"Rp {user.saldo:,}".replace(",", "."),
        fill="#000000",
        font=("Poppins SemiBold", 24 * -1)
    )

    # BUAT TAMPILAN USERNAMA
    canvas.create_text(
        467.0,
        479.0,
        anchor="nw",
        text= user.usernama,
        fill="#000000",
        font=("Poppins Medium", 20 * -1)
    )

    # BUAT TAMPILAN NOMOR HP
    canvas.create_text(
        104.0,
        297.0,
        anchor="nw",
        text= user.no_hp,
        fill="#000000",
        font=("Poppins Light", 14 * -1)
    )

    # BUAT TAMPILAN ALAMAT
    canvas.create_text(
        104.0,
        330.0,
        anchor="nw",
        text= user.alamat,
        fill="#000000",
        font=("Poppins Light", 14 * -1)
    )

    # BUAT TAMPILAN TANGGAL LAHIR
    canvas.create_text(
        493.0,
        297.0,
        anchor="nw",
        text= user.kelahiran,
        fill="#000000",
        font=("Poppins Light", 14 * -1)
    )

    # BUAT TAMPILAN ANGGOTA
    canvas.create_text(
        493.0,
        262.0,
        anchor="nw",
        text= user.keanggotaan,
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # BUAT TAMPILAN NAMA LENGKAP
    canvas.create_text(
        104.0,
        257.0,
        anchor="nw",
        text=user.nama,
        fill="#000000",
        font=("Poppins Medium", 24 * -1)
    )



def saldo(canvas, user):


    # BUAT TAMPILAN SALDO
    canvas.create_text(
        104.0,
        408.0,
        anchor="nw",
        text=f"Rp {user.saldo:,}".replace(",", '.'),
        fill="#000000",
        font=("Poppins SemiBold", 40 * -1)
    )

    # BUAT TAMPILAN USERNAMA
    canvas.create_text(
        467.0,
        479.0,
        anchor="nw",
        text= user.usernama,
        fill="#000000",
        font=("Poppins Medium", 20 * -1)
    )

    # BUAT TAMPILAN ANGGOTA
    canvas.create_text(
        493.0,
        262.0,
        anchor="nw",
        text= user.keanggotaan,
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # BUAT TAMPILAN NAMA LENGKAP
    canvas.create_text(
        104.0,
        257.0,
        anchor="nw",
        text=user.nama,
        fill="#000000",
        font=("Poppins Medium", 24 * -1)
    )
    



def tabel(app, data, width, height):

    frame = Frame(app, width=1300, height=500)
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



    tv = ttk.Treeview(frame1)
    tv.place(relheight=1, relwidth=1)
    # x=55, y=200

    treescrolly = Scrollbar(frame1, orient='vertical', command=tv.yview)
    treescrollx = Scrollbar(frame1, orient='horizontal', command=tv.xview)
    tv.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)

    # treescrollx.pack(side="bottom", fill='x')
    # treescrolly.pack(side='right', fill='y')

    tv['columns'] = ('pengirim', 'penerima')

    tv.column('#0', width=430)
    tv.column('#1', width=430)
    tv.column('#2', width=430)

    tv.heading('#0', text="ID")
    tv.heading('#1', text="Pengirim")
    tv.heading('#2', text="Penerima")


    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyahan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyashan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhfaan", "Reasdyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyshan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhsdan"))
    tv.insert("", 'end', text ="0", values =( "reydfdhan", "Reyhasdan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyshan", "Reydhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reydhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhasan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "freyshan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyadshan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reysdhan", "Rasdeyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyhan"))
    tv.insert("", 'end', text ="0", values =( "reyhan", "Reyasdhan"))

    # scroll.place(x=55, y=200)



    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=377.0,
        y=564.0,
        width=321.0,
        height=115.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=710.0,
        y=564.0,
        width=321.0,
        height=115.0
    )