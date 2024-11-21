from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

import os


def menu_awal():
    os.system('cls')
    
    judul = Text.assemble("BANK", (" AJA", "cyan"), justify='center')
    deskripsi = Text.assemble("Halo, senang berjumpa dengan Anda! Silahkan", (" Masuk atau Daftar", "orange"), justify='center')
    
    print(Panel(judul))
    print(Panel(deskripsi))
    # print("\t\t Halo, senang berjumpa dengan [bold magenta]Anda[/bold magenta]! Silahkan [bold cyan]Masuk atau Daftar[/bold cyan]")
    
    
    print("""\n 
          [bold green underline]1.Masukan Kartu [/bold green underline] \n 
          [bold yellow underline]2.Buat Akun     [/bold yellow underline] \n
          [bold red underline]3. Keluar       [/bold red underline] \n
          """)
    

    pilihan = int(Prompt.ask("Pilih"))
    
    return pilihan