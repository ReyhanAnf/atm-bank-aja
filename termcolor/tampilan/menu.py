from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

from .daftar import kartu_atm
import os, random

def menu_utama(session):
    auth = session[0]
    data = session[1]
    
    os.system('cls')
    
    judul = Text.assemble("BANK", (" AJA", "cyan"), " - MENU", justify='center')
    deskripsi = Text.assemble("HALO ", (f"{data['nama'].upper()}", "cyan bold"), ", SILAHKAN PILIH", (" MENU!", "orange"), justify='center')
    
    print(Panel(judul))
    print(Panel(deskripsi))
    
    
    menu = ["Informasi Rekening", "Cek Saldo", "Histori Transaksi", "Transfer", 'Setor', "Tarik", "Transfer", "Bayar"]
    text = "\n "
    
    for i in range(len(menu)):
        formatext = f"bold underline color({random.randint(1, 50)})"
        tag_open = f"\t\t [{formatext}]"
        tag_close = f"[/{formatext}] \n"
        
        isi = tag_open + f"{i+1}. " + menu[i] + tag_close
        text += isi
        
    print(text)
    
    
    pilihan = Prompt.ask("Pilih")