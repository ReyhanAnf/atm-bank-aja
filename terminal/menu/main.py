import os

from .info_rekening.main import info_rekening

def dashboard(sesi):
    auth = sesi['auth']
    user = sesi['data']
    
    os.system('cls')
    print("\n")
    print("="*10, " BANK AJA - Dashboard", "="*10)
    print("\n")
    
    while auth:
        menu = ['Informasi Rekening', 'Cek Saldo', 'Histori Transaksi', 'Transfer', 'Tarik', 'Setor', 'Bayar', 'Keluar']
        
        menu_print = "\n ====================================== \n"
        for i in range(len(menu)):
            text = f"{i}. {menu[i]} \n"
            menu_print += text
        menu_print += "\n ======================================= \n"
        
        pilihan = int(input("Pilih : "))
        
        if pilihan == 1:
            remenu = info_rekening(sesi)
            if remenu:
                continue
            else:
                break
        elif pilihan == 2:
            pass
        elif pilihan == 3:
            pass
        elif pilihan == 4:
            pass
        elif pilihan == 5:
            pass
        elif pilihan == 6:
            pass
        elif pilihan == 7:
            pass
        elif pilihan == 8:
            pass
        else:
            pass
        