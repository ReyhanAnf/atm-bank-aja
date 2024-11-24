from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

import os
from ..tampilan import header, belum_login, pilihan_kembali_ke_menu
from ...pendataan.transaksi import cek_penerima, konfirmasi_transaksi

from .proses import mutasi

def formulir_tarik(sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] bertipe dict
    auth = sesi['auth']
    user = sesi['data']
    
    # ketika user telah login makan jalankan program ini
    if auth == True:
        # bersihkan terminal
        os.system('cls')
        
        # menampilan header sebagai penanda ini di program bank aja dan menunjukan berada di menu apa
        header("Tarik", user['nama'])
        
        ######## ISI
        
        isian = True
        nominal = 0
        while isian:
            print(Panel(Text("PENARIKAN HARUS MENGGUNAKAN KELIPATAN RP. 50.000 ATAU RP. 100.000 \n DAN MAKSIMAL PENARIKAN ADALAH RP. 2.500.000", style="bold white on navy_blue", justify='center')))
            nominal = int(Prompt.ask("Nominal Penarikan"))
            
            if nominal % 50000 != 0 or nominal < 50000:
                print(Panel(Text("PENARIKAN HARUS MENGGUNAKAN KELIPATAN RP. 50.000 ATAU RP. 100.000", style="bold black on orange3", justify='center')))
                print(Panel(Text("MINIMAL PENARIKAN RP. 10.000", style="bold white on orange3", justify='center')))
                continue
            
            isian = False
            
        
        metode = 'tarik'
        admin = 0
        total = nominal + admin
        
        formulir = {
            'pengirim': user,
            'penerima': user,
            'metode': metode,
            'admin' : admin,
            'status' : 'menunggu',
            'jumlah': nominal,
            'total' : total
        }
        
        konfirmasi = konfirmasi_transaksi(formulir)
        lanjut = konfirmasi[0]
        data = konfirmasi[1]
        
        
        if lanjut == True and 'kode' in data:
            mutasi(data)
            
        elif lanjut == False and data != None:
            remenu = formulir_tarik(sesi)
            return remenu
            
        else:
            print("Kembali")
            remenu = True
            return remenu
        
        #############
        
        # PILIHAN KEMBALI KE MENU
        remenu = pilihan_kembali_ke_menu()
        return remenu
    else:
        return belum_login()
        
    
    