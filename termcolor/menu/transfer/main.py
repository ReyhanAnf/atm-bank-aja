from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

import os
from ..tampilan import header, belum_login, pilihan_kembali_ke_menu
from ...pendataan.transaksi import cek_penerima, konfirmasi_transaksi

from .proses import mutasi

def formulir_transfer(sesi):
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
        header("Transfer", user['nama'])
        
        ######## ISI
        
        isian = True
        penerima = {}
        nominal = 0
        while isian:
            penerima = Prompt.ask("Usernama atau Nomor Kartu Penerima")
            penerima = cek_penerima(penerima)
            nominal = int(Prompt.ask("Jumlah Transfer"))
            
            if type(penerima) == type(False):
                print(Panel(Text("PENERIMA TIDAK DITEMUKAN!", style="bold white on yellow", justify='center')))
                continue
            
            if nominal < 10000:
                print(Panel(Text("MINIMAL TRANSFER RP. 10.000", style="bold white on yellow", justify='center')))
                continue
            
            isian = False
            
        
        metode = 'transfer'
        admin = 2500
        total = nominal + admin
        
        formulir = {
            'pengirim': user,
            'penerima': penerima,
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
            remenu = formulir_transfer(sesi)
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
        
    
    
