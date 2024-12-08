import os
from ...daftar.tampilan import kartu_atm

def info_rekening(sesi):
    auth = sesi['auth']
    user = sesi['data']
    
    os.system('cls')
    print("\n")
    print("="*10, " BANK AJA - Info Rekening", "="*10)
    print("\n")
    
    while auth:
        print(kartu_atm(user))
        
        remenu = int(input("Kembali ke menu ? [y/t] "))
        return remenu