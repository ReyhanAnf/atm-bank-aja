# Import library eksternal
import hashlib # Hasing PIN
import pandas as pd # Olah data

# Untuk menseting tabel pada pandas tak terbatas jumlah kolomnya
pd.set_option('display.max_columns', None)

# Fungsi untuk memanggil data user dari file user.csv
def data_user():
    df = pd.read_csv('./data/user.csv')
    return df
 

# Fungsi untuk update data user dari user yang diubah
# mengandung parameter usernama, kolom, nilai_baru => yaitu data yang dibutuhkan untuk mengisi tabel user
def update_user(usernama, kolom, nilai_baru):
    df = data_user()
    # Menampung data usernama yang dimaksud
    df_tujuan = df[df['usernama'] == usernama]
    
    # Jika user yang dimaksud ada didalam data (tidak kosong)
    if not df_tujuan.empty:
        # maka ganti data dengan usernama (id) dengan kolom sesuai argumen dengan  argumen nilai_baru
        df.loc[df['usernama'] == usernama, kolom] = nilai_baru
        
        # simpan data terbaru kedalam file
        df.to_csv('./data/user.csv', index=False)
        # Kembalikan True
        return True
        
    else:
        # Jika data kosong maka cetak Data tidak ditemukan
        print(f'Data dengan usernama: {usernama}, Tidak ditemukan')
        # Kembalikan False
        return False


# Fungsi untuk menambah data user dari user yang ditambah
# mengandung parameter data => yaitu data yang dibutuhkan untuk mengisi tabel user
def tambah_user(data):
    # Ambil data user dari fungsi data_user
    # fungsi data_user mengembalikan DataFrame
    df = data_user()
    # Isi baris paling bawah dengan data transaksi terbaru
    df.loc[len(df)] = data

    # Simpan DataFrame terbaru kedalam file csv tanpa index
    df.to_csv('./data/user.csv', index=False)

# Fungsi untuk mengecek data user dari user yang dicek
# mengandung inputer berupa str 
def cek_user_kartu(inputer):
    # Ambil data user dari fungsi data_user
    # fungsi data_user mengembalikan DataFrame
    df = data_user()
    
    # Jika identitas usernama yang di inputkan ada didalam data atau tidak kosong
    if not df.loc[df['usernama'] == inputer].empty:
        # maka ambil index dari data tersebut
        index = df.loc[df['usernama'] == inputer].index[0]
        # lalu kembalikan data ke-index tersebut
        return df.iloc[index]
    elif not df.loc[df['nomor_kartu'] == int(inputer)].empty:
        # Jika identitas nomor kartu yang di inputkan ada didalam data atau tidak kosong
        # maka ambil index dari data tersebut
        # lalu kembalikan data ke-index tersebut
        index = df.loc[df['nomor_kartu'] == int(inputer)].index[0]
        return df.iloc[index]
    else:
        # jika benar benar tidak ditemukan makan kembalikan string "Nama identitas - None"
        return False



# Fungsi untuk mengecek pin yang diinputkan sama dengan pin yang ada didalam data
# mengandung inputer berupa pin dan user
def cek_pin(pin_input, user):
    # tampung user['pin'] kedalam variabel pin_user
    pin_user = user['pin']
    
    # Hashing pin_input menjadi sha256 dan kembalikan ke variabel tersebut lagi
    h = hashlib.new('sha256')
    h.update(bytes(pin_input, encoding='utf-8'))
    pin_input = h.hexdigest()   
    
    # Jika pin yang diinput sama dengan pin yang ada didalam data maka
    if pin_input == pin_user:
        # kembalikan data dict dengan berisi auth true dan data user
        return {'auth': True, 'data': user}
    else:
        # Jika pin tidak sama makan gagal melakukan login, maka auth bernilai false dan data None
        return {'auth': False, 'data': None}