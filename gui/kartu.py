from tkinter import Tk, Canvas, Button, PhotoImage, ttk, Scrollbar, Frame


def atm(canvas, user):

    # BUAT TAMPILAN NOMOT KARTU
    canvas.create_text(
        341.0,
        434.0,
        anchor="nw",
        text= ' '.join(f"{int(user.nomor_kartu)}"),
        fill="#000000",
        font=("Poppins SemiBold", 32 * -1)
    )
    
    # BUAT TAMPILAN NOMOT SERI
    canvas.create_text(
        104.0,
        479.0,
        anchor="nw",
        text= int(user.kode_seri),
        fill="#000000",
        font=("Poppins SemiBold", 24 * -1)
    )

    # BUAT TAMPILAN SALDO
    canvas.create_text(
        104.0,
        371.0,
        anchor="nw",
        text=f"Rp {int(user.saldo):,}".replace(",", "."),
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
        text=f"Rp {int(user.saldo):,}".replace(",", '.'),
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
    

