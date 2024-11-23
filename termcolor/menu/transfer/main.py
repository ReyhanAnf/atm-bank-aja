from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.layout import Layout

import os
from ..tampilan import header, belum_login, pilihan_kembali_ke_menu
from ...pendataan.transaksi import cek_penerima, generate_kode


def formulir_transfer(sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    data = sesi['data']
    
    # ketika user telah login makan jalankan program ini
    if auth == True:
        # bersihkan terminal
        os.system('cls')
        
        # menampilan header sebagai penanda ini di program bank aja dan menunjukan berada di menu apa
        header("Transfer", data['nama'])
        
        # ISI
        kode = generate_kode('transfer', 10)
        pengirim = data['nama']
        
        isian = True
        penerima = {}
        nominal = 0
        while isian:
            penerima = Prompt.ask("Usernama atau Nomor Kartu Penerima")
            penerima = cek_penerima(penerima)
            if penerima == None:
                continue
            
            nominal = int(Prompt.ask("Usernama"))
            if nominal < 10000:
                continue
            
            isian = False
            
        
        metode = 'transfer'
        admin = 2500
        total = nominal + admin
        
        
        print(kode, pengirim, penerima, nominal, metode, admin, total)
        #
        
        # PILIHAN KEMBALI KE MENU
        remenu = pilihan_kembali_ke_menu()
        return remenu
    else:
        return belum_login()
        
    
    
