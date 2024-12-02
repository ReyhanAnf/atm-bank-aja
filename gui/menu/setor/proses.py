
from ...pendataan.user import update_user
from ...pendataan.transaksi import tambah_transaksi


def mutasi(data):
    ## Copy data kedalam variabel supaya data asli tidak berubah
    data_transaksi = data.copy()
    
    # Dalam data_transaksi ubah dalam key pengirimnya yang asalnya dict user menjadi string nama user
    data_transaksi['pengirim'] = data_transaksi['pengirim']['usernama']
    
    # Jika dalam data_transaksi key penerima bukan bertipe string ATAU datanya dict maka konversi ke string
    if type(data_transaksi['penerima']) != type('str'):
        # Pengubahan data dict menjadi string
        data_transaksi['penerima'] = data_transaksi['penerima']['usernama']
    
    
    # Jalankan fungsi tambah_transaksi dengan argumen data_transaksi
    # Tambah_transaksi akan mengembalikan nilai boolean, tampung nilai kembali tersebut kedalam variable transaksi
    transaksi = tambah_transaksi(data_transaksi)
    
    # Jika transaksi nya True atau berhasil
    if transaksi == True:   
        
        ## Update saldo penerima
        if type(data['penerima']) != type('str'):
            
            ## Maka Update saldo pengirim
            penerima = data['penerima']
            saldo_penerima = int(penerima['saldo']) + int(data['jumlah'])
            
            # Maka update data usernama pengirim
            update_user(usernama=penerima['usernama'], kolom='saldo', nilai_baru=saldo_penerima)
        
        return True
        
    else:
        # JIka tidak kembalikan nilai false
        return False
            
    