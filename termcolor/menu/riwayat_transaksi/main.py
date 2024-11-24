from rich.panel import Panel
from rich.text import Text
from rich import print
from rich.console import Console
from rich.table import Table

import os

from ..tampilan import header, pilihan_kembali_ke_menu, belum_login
from ...pendataan.transaksi import data_transaksi

def tabel(dataset, judul):
    table = Table(title=judul)

    for col in dataset.columns:
        table.add_column(col, justify="right", style="cyan", no_wrap=True)

    for i in range(len(dataset)):
        row = []
        for val in dataset.iloc[i]:
            if type(val) != type('str'):
                row.append(f'Rp {val:,.2f}')
            else:
                row.append(str(val))
            
        table.add_row(*row)
        
    
    console = Console()
    console.print(table)

def riwayat_transaksi(sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    # ketika user telah login makan jalankan program ini
    if auth == True:
        # bersihkan terminal
        os.system('cls')
        
        # menampilan header sebagai penanda ini di program bank aja dan menunjukan berada di menu apa
        header("Riwayat Transaksi", user['nama'])
        
        # ISI
        data = data_transaksi()
        data = data[(data['pengirim'] == user['usernama']) | (data['penerima'] == user['usernama'])]
        tabel(data, judul='Riwayat Transaksi')
        #
        
        # PILIHAN KEMBALI KE MENU
        remenu = pilihan_kembali_ke_menu()
        return remenu
    else:
        return belum_login()
        