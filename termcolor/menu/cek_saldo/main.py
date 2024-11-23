from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich import print

import os

from ..tampilan import header, pilihan_kembali_ke_menu, belum_login

def cek_saldo(sesi):
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
        header("Cek Saldo", data['nama'])
        
        # ISI
        saldo = data['saldo']
        print(Panel(Text(f"SISA SALDO ANDA ADALAH RP. {saldo}", style="bold white on navy")))
        #
        
        # PILIHAN KEMBALI KE MENU
        remenu = pilihan_kembali_ke_menu()
        return remenu
    else:
        return belum_login()
        