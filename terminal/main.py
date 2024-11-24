
import os

from .awal.tampilan import menu_awal

def main():
    program = True
    while program:
        os.system('cls')
        
        # Menu Awal
        pilihan = menu_awal()
        if pilihan == 1:
            print("masuk")
        elif pilihan == 2:
            print("daftar")
        elif pilihan == 0:
            print("keluar")
        else:
            print("Pilihan tidak valid")
        