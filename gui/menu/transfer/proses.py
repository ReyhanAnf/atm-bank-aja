
from ...pendataan.user import update_user
from ...pendataan.transaksi import tambah_transaksi



import time

def mutasi(data):
    ##
    data_transaksi = data.copy()
    
    data_transaksi['pengirim'] = data_transaksi['pengirim']['usernama']
    if type(data_transaksi['penerima']) != type('str'):
        data_transaksi['penerima'] = data_transaksi['penerima']['usernama']
    
    transaksi = tambah_transaksi(data_transaksi)
    
    
    if transaksi == True:
        
        ## Update saldo pengirim
        pengirim = data['pengirim']
        saldo_pengirim = int(pengirim['saldo']) - int(data['total'])
        update_user(usernama=pengirim['usernama'], kolom='saldo', nilai_baru=saldo_pengirim)
        
        
        ## Update saldo penerima
        if type(data['penerima']) != type('str'):
            penerima = data['penerima']
            saldo_penerima = int(penerima['saldo']) + int(data['jumlah'])
            update_user(usernama=penerima['usernama'], kolom='saldo', nilai_baru=saldo_penerima)
        
        return True
        
    else:
        return False
            
    