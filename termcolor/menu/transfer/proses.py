
from ...pendataan.user import update_user
from ...pendataan.transaksi import tambah_transaksi

from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.progress import track


import time

def mutasi(data):
    ##
    data_transaksi = data.copy()
    data_transaksi['pengirim'] = data_transaksi['pengirim']['usernama']
    data_transaksi['penerima'] = data_transaksi['penerima']['usernama']
    transaksi = tambah_transaksi(data_transaksi)
    
    for step in track(range(50), description='Memprosess..', refresh_per_second=50):
            time.sleep(.01)
    
    if transaksi == True:
        
        ## Update saldo pengirim
        pengirim = data['pengirim']
        saldo_pengirim = int(pengirim['saldo']) - int(data['total'])
        update_user(usernama=pengirim['usernama'], kolom='saldo', nilai_baru=saldo_pengirim)
        
        
        ## Update saldo penerima
        penerima = data['penerima']
        saldo_penerima = int(penerima['saldo']) + int(data['jumlah'])
        update_user(usernama=penerima['usernama'], kolom='saldo', nilai_baru=saldo_penerima)
        
        print(Panel(Text("TRANSAKSI BERHASIL!", style="bold white on green", justify='center')))
        return True
        
    else:
        print(Panel(Text("TRANSAKSI GAGAL!", style="bold white on green", justify='center')))
        return False
            
    