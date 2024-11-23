
import os

from .awal.tampilan import menu_awal

def main():
    program = True
    while program:
        os.system('cls')
        
        # Menu Awal
        menu_awal()
        program = False