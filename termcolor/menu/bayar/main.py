from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

import os
from ..tampilan import header, belum_login, pilihan_kembali_ke_menu, pilihan_menu
from ...pendataan.transaksi import cek_penerima, konfirmasi_transaksi

from .proses import mutasi

def bayar(sesi):
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
        header("Pembayaran", user['nama'])
        
        
        ######## MENU
        menu = ['PLN Paska', 'PLN Token', 'PDAM',  'Virtual Account', 'Pulsa', 'BPJS', 'TopUp Gopay', 'TopUp Shopeepay', 'TopUp Ovo', 'Keluar']
        teks_menu = pilihan_menu(menu)
        print(teks_menu)
        
        pilih_menu = int(Prompt.ask('Pilih'))
        
        
        ######## ISI
        if pilih_menu != 0:
            menu_dipilih = menu[pilih_menu-1]
        
            isian = True
            nominal = 0
            while isian:
                # print(Panel(Text("SETOR HARUS MENGGUNAKAN KELIPATAN RP. 50.000 ATAU RP. 100.000", style="bold white on navy_blue", justify='center')))
                tujuan = Prompt.ask(f"Nomor Tujuan {menu_dipilih}")
                nominal = int(Prompt.ask("Nominal Setor"))
                
                isian = False
                
            
            metode = 'bayar'
            admin = 2500
            total = nominal + admin
            
            formulir = {
                'pengirim': user,
                'penerima': f'{menu_dipilih} - {tujuan}',
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
                remenu = bayar(sesi)
                return remenu
                
            else:
                print("Kembali")
                remenu = True
                return remenu
            
            # PILIHAN KEMBALI KE MENU
            remenu = pilihan_kembali_ke_menu()
            return remenu
        else:
            return False
        #############
        
        
    else:
        return belum_login()
        
    
    
