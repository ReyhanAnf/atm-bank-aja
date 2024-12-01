# Import library eksternal
import pandas as pd # Untuk olah data
import numpy as np # Untuk olah angka
import datetime # Untuk waktu

# Import library eksternal untuk GUI yaitu library TKinter atau CustomTKinter
import customtkinter as ctk

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
        return f"{identity} - None"


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
def konfirmasi_transaksi(app, frame, sesi, data, mutasi):
    # Reset frame body dan footer supaya bersih dari frame sebelumnya
    reset_frame(frame['body'])
    reset_frame(frame['footer'])
    
    # buat kode (id) menggunakan funsi generate_kode dengan argumen metode dan panjang angka acak
    kode = generate_kode(data['metode'], 10)
    # simpan kode kedalam data
    data['kode'] = kode
    
    # Jika data penerima bertipe string (tidak bertipe dict)
    if type(data['penerima']) == type('str'):
        penerima = data['penerima']
        # maka cek penerima tersebut ada dalam data atau tidak dan ubah nilai pada data['penerima'] menjadi dict
        data['penerima'] = cek_penerima(data['penerima'])
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
        'Jumlah' : f"Rp {data['jumlah']:,}",
        'Admin' : f"Rp {data['admin']:,}",
        'Total' : f"Rp {data['total']:,}",
    }

    # jika metode nya tidak transfer
    if data['metode'] != 'transfer':
        # maka hapus nilai data nama pengirim dan nama penerima
        del content['Nama_Pengirim']
        del content['Nama_Penerima']
        
        # ubah data yang dihapus dengan data nama
        nama = {'Nama': f"{data['pengirim']['nama']} - {data['pengirim']['nomor_kartu']}"}
        
        # gabungkan dict nama dengan dict content (nama didepan supaya nama paling atas)
        content = {**nama, **content}
    
    # ambil keys dari data dict content -> mengembalikan nilai list (kcontent => bertipe list)
    kcontent = content.keys()
    
    # petakan kcontent menjadi key
    for key in kcontent:
        # Setiap key dalam kontent akan dijadikan gui melalui perulangan ini sebanyak keys dalam content
        
        ########### TAMPILAN GUI
        # Buat pembungkus
        wrap = ctk.CTkFrame(frame['body'], fg_color='transparent') # Pembungkus
        wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
        
        # Buat label
        text_key = " ".join(key.split("_"))
        label = ctk.CTkLabel(wrap, text=text_key, text_color='white') # Label
        label.pack(side='left', padx=10, pady=5)
        
        # Buat isi atau kontent
        isian = ctk.CTkLabel(wrap, corner_radius=10, text=content[key], width=300, text_color='white') # isi
        isian.pack(side='right', padx=10, pady=5)
    
    
    
    
    ################################################## FOOTER
    ######################################### 
    
    # Fungsi untuk menghandel transaksi
    def transaksi_handle():
        # pertama lakukan mutasi dan tampung status keberhasilan mutasi tersebut kedalam variabel status
        status = mutasi(data)
        # Jika statusnya berhasil
        if status == True:
            # Maka buat GUI Sukses
            sukses = ctk.CTkLabel(frame['body'], text=f"{data['metode'].upper()} BERHASIL", fg_color="green")
            # Maka tampilkan GUI Sukses
            sukses.pack(side='top', fill='x', expand=True)
            
            # Buat tombol selesai untuk kembali ke dashboard
            from ..menu.main import dashboard
            # reset frame footer
            reset_frame(frame['footer'])
            
            # Buat tombol selesai
            selesaiBtn = ctk.CTkButton(frame['footer'], height=50,text="Selesai", command=lambda : dashboard(app, frame, sesi))
            # Tampilkan tombol selesai
            selesaiBtn.pack(side="left", fill='x', expand=True, padx=10)
            
        else:
            # Jika Statusnya gagal
            # Maka buat GUI Gagal
            gagal = ctk.CTkLabel(frame['body'], text=f"{data['metode'].upper()} GAGAL", fg_color="red")
            # Maka tampilkan GUI Gagal
            gagal.pack(side='top', fill='x', expand=True)
            
            # Buat tombol ulangi untuk kembali ke menecek transaksi
            from ..menu.transfer.main import transfer
            # reset frame footer
            reset_frame(frame['footer'])
            
            # Buat tombol Ulangi
            ulangBtn = ctk.CTkButton(frame['footer'], height=50,text="Ulangi", command=lambda : transfer(app, frame, sesi))
            # Tampilkan tombol ulangi
            ulangBtn.pack(side="left", fill='x', expand=True, padx=10)
            
    
    # Buat tombol mutasi untuk konfirmasi mutasi
    mutasiBtn = ctk.CTkButton(frame['footer'], height=50,text="Konfirmasi", command=transaksi_handle)
    # Tampilkan tombol mutasi untuk konfirmasi mutasi
    mutasiBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    ######################################### 
    ################################################## FOOTER
    
    