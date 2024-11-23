from rich.text import Text
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print

from .proses import cek_pin
from ..pendataan.user import cek_user_kartu

import os, time

def formulir_masuk():
    sukses = False
    
    while not sukses:
        os.system('cls')
        judul = Text.assemble("BANK", (" AJA", "cyan"), (" - MASUK", "bold"), justify='center')
        deskripsi = Text.assemble("MASUKAN NOMOR KARTU!", justify='center')
        
        print(Panel(judul))
        print(Panel(deskripsi))
        
        usernama_kartu = Prompt.ask("Usernama atau Kartu")
        user = cek_user_kartu(usernama_kartu)
        
        if type(user) != type(False):
            for i in range(3):
                pin = Prompt.ask("PIN")
                sesi = cek_pin(pin, user)
                
                if not sesi['auth']:
                    print(Panel(Text(f"GAGAL MASUK! ULANGI {i+1}/3", style="bold white on orange3", justify='center')))
                    time.sleep(1)
                    continue
                else:
                    print(Panel(Text("BERHASIL MASUK!", style="bold white on green", justify='center')))
                    time.sleep(2)
                    sukses = True
                    return sesi
                
            print(Panel(Text("TELAH MENCOBA SEBANYAK 3 KALI - ANDA AKAN KELUAR!!", style="bold white on red", justify='center')))
            time.sleep(2)
            break
            
        else:
            print(Panel(Text("GAGAL MASUK! ULANGI", style="bold white on red", justify='center')))
            time.sleep(2)
            
                
            
            
            