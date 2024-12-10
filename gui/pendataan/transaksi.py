# Import library eksternal
import pandas as pd # Untuk olah data
import numpy as np # Untuk olah angka
import datetime # Untuk waktu

# Import library eksternal untuk GUI yaitu library TKinter atau CustomTKinter
from tkinter import  Canvas, Button, PhotoImage

from ..setelan import akses_aset_media

# Import library internal
from ..setelan import reset_frame # untuk mereset tampilan GUI
from .user import data_user # Untuk mengambil data dari file user.csv

# Untuk menseting tabel pada pandas tak terbatas jumlah kolomnya
pd.set_option('display.max_columns', None)

# Fungsi untuk memanggil data transaksi dari file transaksi.csv
def data_transaksi():
    df = pd.read_csv('./data/transaksi.csv')
    return df

# Fungsi untuk menambah data transaksi dari transaksi yang dilakukan
# mengandung parameter data => yaitu data yang dibutuhkan untuk mengisi tabel transaksi
def tambah_transaksi(data):
    try:
        # ketika semua tahap transaksi telah mencapai disini, maka statusnya dari 'menunggu' menjadi 'suskes' menandakan transaksi sudah mencapai tahap akhir
        data['status'] = 'sukses'
        # Ketika transaksi sudah berhasil, maka ambil data waktu ketika status transaksinya sudah sukses
        data['waktu'] = datetime.datetime.now()
        
        # Ambil data transaksi dari fungsi data_transaksi
        # fungsi data_transaksi mengembalikan DataFrame
        df = data_transaksi()
        # Isi baris paling bawah dengan data transaksi terbaru
        df.loc[len(df)] = data
        
        # Simpan DataFrame terbaru kedalam file csv tanpa index
        df.to_csv('./data/transaksi.csv', index=False)
        # Kembalikan nilai True untukk menandakan bahwa transaksi berhasil
        return True
    except Exception:
        return False


# Fungsi untuk merubah transaksi tertentu jika suatu saat ada kesalahan
def update_transaksi(kode, kolom, nilai_baru):
    # ambil data dari fungsi data_transaksi
    df = data_transaksi()
    # ambil data spesifik dengan parameter kode (id)
    df_tujuan = df[df['kode'] == kode]
    
    # Jika data dengan kode (id) ditemukan atau tidak kosong
    if not df_tujuan.empty:
        # maka ganti data dengan kode (id) dengan kolom sesuai argumen dengan  argumen nilai_baru
        df.loc[df['kode'] == kode, kolom] = nilai_baru
        
        # simpan data terbaru kedalam file
        df.to_csv('./data/transaksi.csv', index=False)
        # cetak berhasil
        print('transaksi berhasil')
        # kembalikan True
        return True
        
    else:
        # Jika data kosong maka cetak Data tidak ditemukan
        print(f'Data dengan kode: {kode}, Tidak ditemukan')
        # kembalikan False
        return False
        

# Fungsi untuk mengecek apakah dalam suatu transaksi penerimanya ada
def cek_penerima(identity):
    # ambil data dari fungsi cek_penerima
    df = data_user()
    
    # Jika identitas usernama yang di inputkan ada didalam data atau tidak kosong
    if not df.loc[df['usernama'] == identity].empty:
        # maka ambil index dari data tersebut
        index = df.loc[df['usernama'] == identity].index[0]
        # lalu kembalikan data ke-index tersebut
        return df.iloc[index]
    elif not df.loc[df['nomor_kartu'] == identity].empty:
        # Jika identitas nomor kartu yang di inputkan ada didalam data atau tidak kosong
        # maka ambil index dari data tersebut
        # lalu kembalikan data ke-index tersebut
        index = df.loc[df['nomor_kartu'] == identity].index[0]
        return df.iloc[index]
    else:
        # jika benar benar tidak ditemukan makan kembalikan string "Nama identitas - None"
        return f"{identity} - xxx"


# Fungsi untuk men generate kode secara otomatis untuk pembuatan id transaksi
# memiliki parameter metode -> 'transfer, tarik, setor' dan len -> int untuk seberapa panjang karakter kode yang diinginkan
def generate_kode(metode, len):
    # buat variabel kode dengan string kosong untuk menampug nomor acak
    kode = ''
    
    if metode.lower() == 'transfer':
        # jika metode nya transfer maka awali kode tersebut dengan trf-
        kode += 'TRF-'
    elif metode.lower() == 'setor':
        # jika metode nya setor maka awali kode tersebut dengan str-
        kode += 'STR-'
    elif metode.lower() == 'tarik':
        # jika metode nya tarik maka awali kode tersebut dengan tarik-
        kode += 'TRK-'
    else:
        # jika metode nya selain itu maka awali kode tersebut dengan A-
        kode += 'A-'
    
    # Buat len(misal 8) list angka random menggunakan modul numpy dengan range angka random dari 0 sampai 9
    random = np.random.randint(0,9, size=len)
    # Setiap nilai dari random akan di petakan kedalam variabel i
    for i in random:
        # variabel kode di tambah dengan angka acak yang telah diubah menjadi str
        kode += str(i)
    
    # kembalikan str kode
    return kode



# Fungsi untuk mengkonfirmasi transaksi
# mengandung parameter app -> windownya, frame -> frame aplikasi, sesi -> autentikasi user, mutasi -> fungsi untuk mengubah data

def konfirmasi_transaksi(app, sesi, data, mutasi):

    LOC = 'status_transaksi'
    # Reset frame body dan footer supaya bersih dari frame sebelumnya
    ############################################### HEADER
    ############################################### 
    
    
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

    # NAVIGASI
    canvas.create_text(
        287.0,
        169.0,
        anchor="nw",
        text=data['metode'].capitalize(),
        fill="#000000",
        font=("Poppins SemiBold", 28 * -1)
    )

    # NAVIGASI
    canvas.create_text(
        570.0,
        11.0,
        anchor="nw",
        text=data['metode'].capitalize(),
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )

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
            text=f"Selamat Datang, {data['pengirim'].nama}",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
    )
    
    ############################################### 
    ############################################### HEADER
    
    # buat kode (id) menggunakan funsi generate_kode dengan argumen metode dan panjang angka acak
    kode = generate_kode(data['metode'], 10)
    # simpan kode kedalam data
    data['kode'] = kode
    
    # cek penerima tersebut ada dalam data atau tidak dan ubah nilai pada data['penerima'] menjadi dict
    data['penerima'] = cek_penerima(data['penerima'])
    
    # Jika data penerima bertipe string (tidak bertipe dict)
    if type(data['penerima']) == type('str'):
        penerima = data['penerima']
    else:
        # Jika data penerima tiak bertipe string (bertipe dict)
        penerima = data['penerima']
        # dan buat variabel penerima untuk di tampilkan ke layar
        penerima = f"{penerima['nama']} - {penerima['nomor_kartu']}"
    
    # Yang diharapkan disini yaitu
    # data['penerima'] -> bertipe dict => untuk di upload ke database
    # variabel penerima -> bertipe str => untuk dicetak kelayar
    
    # buat variabel content untuk dicetak
    content = {
        'Nama_Pengirim' : f"{data['pengirim']['nama']} - {data['pengirim']['nomor_kartu']}",
        'Nama_Penerima' : penerima,
        'Metode': data['metode'],
        'Status': data['status'],
        'Jumlah' : f"Rp {data['jumlah']:,}",
        'Admin' : f"Rp {data['admin']:,}",
        'Total' : f"Rp {data['total']:,}",
    }

    # TAMPILKAN STATUS KARTU
    status_img = PhotoImage(file=akses_aset_media("menunggu.png", LOC))
    status_bg = canvas.create_image(
        344.0,
        337.0,
        image=status_img
    )
    
    
    # jika metode nya tidak transfer
    if data['metode'] != 'transfer' and data['metode'] != 'bayar':
        # maka hapus nilai data nama pengirim dan nama penerima
        del content['Nama_Pengirim']
        del content['Nama_Penerima']
        
        # ubah data yang dihapus dengan data nama
        nama = {'Nama': f"{data['pengirim']['nama']} - {data['pengirim']['nomor_kartu']}"}
        
        # gabungkan dict nama dengan dict content (nama didepan supaya nama paling atas)
        content = {**nama, **content}
        
        # TAMPILKAN LABEL NAMA PENGIRIM
        canvas.create_text(
            45.0,
            242.0,
            anchor="nw",
            text="Nama",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )

        # TAMPILKAN NAMA PENGIRIM
        canvas.create_text(
            653.0,
            242.0,
            anchor="ne",
            text=content['Nama'],
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
    else:
        # TAMPILKAN LABEL NAMA PENGIRIM
        canvas.create_text(
            45.0,
            242.0,
            anchor="nw",
            text="Nama Pengirim",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )

        # TAMPILKAN NAMA PENGIRIM
        canvas.create_text(
            653.0,
            242.0,
            anchor="ne",
            text=content['Nama_Pengirim'],
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        
        # TAMPILKAN LABEL NAMA PENERIMA
        canvas.create_text(
            44.0,
            274.0,
            anchor="nw",
            text="Nama Penerima",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        # TAMPILKAN NAMA PENERIMA
        canvas.create_text(

            653.0,
            274.0,
            anchor="ne",
            text=content['Nama_Penerima'],
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
    
    
    # TAMPILKAN TOTAL
    canvas.create_text(
        45.0,
        392.0,
        anchor="nw",
        text="Total",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN LABEL ADMIN
    canvas.create_text(
        44.0,
        363.0,
        anchor="nw",
        text="Admin",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    # TAMPILKAN ADMIN
    canvas.create_text(
        653.0,
        362.0,
        anchor="ne",
        text=content['Admin'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    

    # TAMPILKAN LABEL METODE
    canvas.create_text(
        44.0,
        303.0,
        anchor="nw",
        text="Metode",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # TAMPILKAN METODE TRANSAKSI
    canvas.create_text(
        653.0,
        304.0,
        anchor="ne",
        text=content['Metode'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN LABEL NOMINAL
    canvas.create_text(
        44.0,
        333.0,
        anchor="nw",
        text="Nominal",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # TAMPILKAN JUMLAH NOMINAL
    canvas.create_text(
        653.0,
        333.0,
        anchor="ne",
        text=content['Jumlah'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    # TAMPILKAN GARIS
    canvas.create_rectangle(
        44.0,
        386.00000004358606,
        652.9999980747743,
        389.0,
        fill="#000000",
        outline="")

    
    # TAMPILKAN TOTAL TRANSAKSI
    canvas.create_text(
        653.0,
        392.0,
        anchor="ne",
        text=content['Total'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN ID TRANSAKSI
    canvas.create_text(
        286.0,
        211.0,
        anchor="nw",
        text=data['kode'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    

    # TAMPILKAN STATUS TRANSAKSI
    status = canvas.create_text(
        300.0,
        425.0,
        anchor="nw",
        text=content['Status'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    
    ################################################## FOOTER
    #########################################
    
    # TOMBOL LANJUT
    lanjut_img = PhotoImage(file=akses_aset_media("konfirmasi.png", LOC))
    lanjut_btn = Button(
        image=lanjut_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: sukses_transaksi(app,sesi, data, content) if mutasi(data) else gagal_transaksi(app, sesi, data, content) ,
        relief="flat"
    )
    lanjut_btn.place(
        x=466.0,
        y=464.0,
        width=213.0,
        height=67.0
    )

    # TOMBOL MENU
    from ..menu.main import dashboard
    menu_img = PhotoImage(
        file=akses_aset_media("button_1.png", LOC))
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

    # TOMBOL KELUAR
    from ..awal.main import home
    keluar_img = PhotoImage(file=akses_aset_media("button_2.png", LOC))
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
    
    app.resizable(False, False)
    app.mainloop()
    
    ######################################### 
    ################################################## FOOTER
    
    
    
def sukses_transaksi(app, sesi, data, content):

    LOC = 'status_transaksi'
    # Reset frame body dan footer supaya bersih dari frame sebelumnya
    ############################################### HEADER
    ############################################### 
    
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

    # NAVIGASI
    canvas.create_text(
        287.0,
        169.0,
        anchor="nw",
        text=data['metode'].capitalize(),
        fill="#000000",
        font=("Poppins SemiBold", 28 * -1)
    )

    # NAVIGASI
    canvas.create_text(
        550.0,
        11.0,
        anchor="nw",
        text=data['metode'].capitalize(),
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )
    
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
            text=f"Selamat Datang, {data['pengirim'].nama}",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
    )
    
    ############################################### 
    ############################################### HEADER
    
    
    # TAMPILKAN STATUS KARTU
    status_img = PhotoImage(file=akses_aset_media("sukses.png", LOC))
    status_bg = canvas.create_image(
        344.0,
        337.0,
        image=status_img
    )
    
    # jika metode nya tidak transfer
    if data['metode'] != 'transfer' and data['metode'] != 'bayar':
        
        # TAMPILKAN LABEL NAMA PENGIRIM
        canvas.create_text(
            45.0,
            242.0,
            anchor="nw",
            text="Nama",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )

        # TAMPILKAN NAMA PENGIRIM
        canvas.create_text(
            653.0,
            242.0,
            anchor="ne",
            text=content['Nama'],
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
    else:
        # TAMPILKAN LABEL NAMA PENGIRIM
        canvas.create_text(
            45.0,
            242.0,
            anchor="nw",
            text="Nama Pengirim",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )

        # TAMPILKAN NAMA PENGIRIM
        canvas.create_text(
            653.0,
            242.0,
            anchor="ne",
            text=content['Nama_Pengirim'],
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        
        # TAMPILKAN LABEL NAMA PENERIMA
        canvas.create_text(
            44.0,
            274.0,
            anchor="nw",
            text="Nama Penerima",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        # TAMPILKAN NAMA PENERIMA
        canvas.create_text(

            653.0,
            274.0,
            anchor="ne",
            text=content['Nama_Penerima'],
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
    
    
    # TAMPILKAN TOTAL
    canvas.create_text(
        45.0,
        392.0,
        anchor="nw",
        text="Total",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN LABEL ADMIN
    canvas.create_text(
        44.0,
        363.0,
        anchor="nw",
        text="Admin",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # TAMPILKAN ADMIN
    canvas.create_text(
        653.0,
        362.0,
        anchor="ne",
        text=content['Admin'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN LABEL METODE
    canvas.create_text(
        44.0,
        303.0,
        anchor="nw",
        text="Metode",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # TAMPILKAN METODE TRANSAKSI
    canvas.create_text(
        653.0,
        304.0,
        anchor="ne",
        text=content['Metode'].capitalize(),
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN LABEL NOMINAL
    canvas.create_text(
        44.0,
        333.0,
        anchor="nw",
        text="Nominal",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # TAMPILKAN JUMLAH NOMINAL
    canvas.create_text(
        653.0,
        333.0,
        anchor="ne",
        text=content['Jumlah'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    # TAMPILKAN GARIS
    canvas.create_rectangle(
        44.0,
        386.00000004358606,
        652.9999980747743,
        389.0,
        fill="#000000",
        outline="")

    # TAMPILKAN TOTAL TRANSAKSI
    canvas.create_text(
        653.0,
        392.0,
        anchor="ne",
        text=content['Total'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN ID TRANSAKSI
    canvas.create_text(
        286.0,
        211.0,
        anchor="nw",
        text=data['kode'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    # TAMPILKAN STATUS TRANSAKSI
    status = canvas.create_text(
        300.0,
        425.0,
        anchor="nw",
        text="SUKSES",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    
    
    ################################################## FOOTER
    #########################################
    

    from ..menu.main import dashboard
    menu_img = PhotoImage(
        file=akses_aset_media("button_1.png", LOC))
    menu_btn = Button(
        image=menu_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dashboard(app,sesi),
        relief="flat"
    )
    menu_btn.place(
        x=466.0,
        y=464.0,
        width=213.0,
        height=67.0
    )

    # TOMBOL KELUAR
    from ..awal.main import home
    keluar_img = PhotoImage(file=akses_aset_media("button_2.png", LOC))
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
    
    app.resizable(False, False)
    app.mainloop()
    
    ######################################### 
    ################################################## FOOTER


 
def gagal_transaksi(app, sesi, data, content):

    LOC = 'status_transaksi'
    # Reset frame body dan footer supaya bersih dari frame sebelumnya
    ############################################### HEADER
    ############################################### 
    
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

    # NAVIGASI
    canvas.create_text(
        287.0,
        169.0,
        anchor="nw",
        text=data['metode'].capitalize(),
        fill="#000000",
        font=("Poppins SemiBold", 28 * -1)
    )

    # NAVIGASI
    canvas.create_text(
        550.0,
        11.0,
        anchor="nw",
        text=data['metode'].capitalize(),
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )
    
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
            text=f"Selamat Datang, {data['pengirim'].nama}",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
    )
    
    ############################################### 
    ############################################### HEADER
    
    
    # TAMPILKAN STATUS KARTU
    status_img = PhotoImage(file=akses_aset_media("gagal.png", LOC))
    status_bg = canvas.create_image(
        344.0,
        337.0,
        image=status_img
    )
    
    # jika metode nya tidak transfer
    if data['metode'] != 'transfer' and data['metode'] != 'bayar':
        
        # TAMPILKAN LABEL NAMA PENGIRIM
        canvas.create_text(
            45.0,
            242.0,
            anchor="nw",
            text="Nama",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )

        # TAMPILKAN NAMA PENGIRIM
        canvas.create_text(
            653.0,
            242.0,
            anchor="ne",
            text=content['Nama'],
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
    else:
        # TAMPILKAN LABEL NAMA PENGIRIM
        canvas.create_text(
            45.0,
            242.0,
            anchor="nw",
            text="Nama Pengirim",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )

        # TAMPILKAN NAMA PENGIRIM
        canvas.create_text(
            653.0,
            242.0,
            anchor="ne",
            text=content['Nama_Pengirim'],
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        
        # TAMPILKAN LABEL NAMA PENERIMA
        canvas.create_text(
            44.0,
            274.0,
            anchor="nw",
            text="Nama Penerima",
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
        # TAMPILKAN NAMA PENERIMA
        canvas.create_text(

            653.0,
            274.0,
            anchor="ne",
            text=content['Nama_Penerima'],
            fill="#000000",
            font=("Poppins Medium", 16 * -1)
        )
    
    # TAMPILKAN TOTAL
    canvas.create_text(
        45.0,
        392.0,
        anchor="nw",
        text="Total",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN LABEL ADMIN
    canvas.create_text(
        44.0,
        363.0,
        anchor="nw",
        text="Admin",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # TAMPILKAN ADMIN
    canvas.create_text(
        653.0,
        362.0,
        anchor="ne",
        text=content['Admin'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN LABEL METODE
    canvas.create_text(
        44.0,
        303.0,
        anchor="nw",
        text="Metode",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # TAMPILKAN METODE TRANSAKSI
    canvas.create_text(
        653.0,
        304.0,
        anchor="ne",
        text=content['Metode'].capitalize(),
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN LABEL NOMINAL
    canvas.create_text(
        44.0,
        333.0,
        anchor="nw",
        text="Nominal",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    # TAMPILKAN JUMLAH NOMINAL
    canvas.create_text(
        653.0,
        333.0,
        anchor="ne",
        text=content['Jumlah'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    # TAMPILKAN GARIS
    canvas.create_rectangle(
        44.0,
        386.00000004358606,
        652.9999980747743,
        389.0,
        fill="#000000",
        outline="")

    # TAMPILKAN TOTAL TRANSAKSI
    canvas.create_text(
        653.0,
        392.0,
        anchor="ne",
        text=content['Total'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    # TAMPILKAN ID TRANSAKSI
    canvas.create_text(
        286.0,
        211.0,
        anchor="nw",
        text=data['kode'],
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    # TAMPILKAN STATUS TRANSAKSI
    status = canvas.create_text(
        300.0,
        425.0,
        anchor="nw",
        text="GAGAL",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    
    
    
    ################################################## FOOTER
    #########################################
    

    from ..menu.main import dashboard
    menu_img = PhotoImage(
        file=akses_aset_media("button_1.png", LOC))
    menu_btn = Button(
        image=menu_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dashboard(app,sesi),
        relief="flat"
    )
    menu_btn.place(
        x=466.0,
        y=464.0,
        width=213.0,
        height=67.0
    )

    # TOMBOL KELUAR
    from ..awal.main import home
    keluar_img = PhotoImage(file=akses_aset_media("button_2.png", LOC))
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
    
    app.resizable(False, False)
    app.mainloop()
    
    ######################################### 
    ################################################## FOOTER
    
