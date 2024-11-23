import random, time
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich import print

def pilihan_menu(menu):
    text = "\n "
        
    for i in range(len(menu)):
        formatext = f"bold underline color({random.randint(1, 50)})"
        tag_open = f"\t\t [{formatext}]"
        tag_close = f"[/{formatext}] \n"
        
        if menu[i].lower() == 'keluar' :
            # Jika menunya 'keluar', maka jadikan keluar sebagai angka 0
            isi = tag_open + f"{0}. " + menu[i] + tag_close
            text += isi
        else:
            isi = tag_open + f"{i+1}. " + menu[i] + tag_close
            text += isi
        
    return text



def header(judul, nama):
    #Buat tampilan header untuk menandakan ini berada di menu yang mana
    
    # Dengan parameter judul dan nama user yang sudah diverifikasi masuk
    judul = Text.assemble("BANK", (" AJA", "cyan"), f" - {judul.upper()}", justify='center')
    deskripsi = Text.assemble("HALO ", (f"{nama.upper()}", "cyan bold"),  justify='center')
    
    print(Panel(judul))
    print(Panel(deskripsi))
    
    
def pilihan_kembali_ke_menu():
    menu = ['Kembali Ke Menu','Keluar']
    tampil_menu = pilihan_menu(menu)
    print(tampil_menu)
    
    pilihan = int(Prompt.ask("Pilih"))
    
    if pilihan == 1:
        remenu = True
        return remenu
    
    
    elif pilihan == 0:
        remenu = False
        return remenu
    
    
    else:
        print(Panel(Text("INPUT SALAH! ANDA AKAN KEMBALI KE MENU!", style="bold white on orange", justify='center')))
        time.sleep(1)
        remenu = True
        return remenu


def belum_login():
    print(Panel(Text("ANDA BELUM LOGIN, ANDA AKAN SEGERA KELUAR!", style="bold white on red", justify='center')))
    time.sleep(1)
    remenu = False
    return remenu