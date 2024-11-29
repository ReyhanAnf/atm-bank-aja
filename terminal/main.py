
import os

from .awal.tampilan import menu_awal
from .masuk.tampilan import formulir_masuk

def main():
    program = True
    while program:
        os.system('cls')
        
        # Menu Awal
        pilihan = menu_awal()
        
        if pilihan == 1:
            sesi = formulir_masuk()
            
            remenu = True
            while remenu:
                if sesi['auth'] == True:
                    ## DASHBOARD
                    remenu = 'menu utama'
                    if remenu == True:
                        continue
                    else:
                        break
                else:
                    break
            
        elif pilihan == 2:
            print("daftar")
        elif pilihan == 0:
            print("keluar")
        else:
            print("Pilihan tidak valid")
        