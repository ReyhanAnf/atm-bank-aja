from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich import print

import time, os

from ...daftar.tampilan import kartu_atm
from ..tampilan import pilihan_kembali_ke_menu, header

def info_rekening(sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth'] #True or False
    data = sesi['data']
    
    # ketika user telah login makan jalankan program ini
    if auth:
        # bersihkan terminal
        os.system('cls')
        
        # menampilan header sebagai penanda ini di program bank aja dan menunjukan berada di menu apa
        header(judul="Info Rekening", nama=data['nama'])
        
        ## ISI
        kartu_atm(data)
        ##
        
        ## PILIHAN KEMBALI KE MENU
        remenu = pilihan_kembali_ke_menu()
        return remenu
        
    else:
        print(Panel(Text("ANDA BELUM LOGIN, ANDA AKAN SEGERA KELUAR!", style="bold white on red", justify='center')))
        time.sleep(1)
        remenu = False
        return remenu