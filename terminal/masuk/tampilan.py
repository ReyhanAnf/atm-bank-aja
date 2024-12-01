
import os, time

from ..pendataan.user import cek_user_kartu
from .proses import cek_pin

def formulir_masuk():
    sukses = False
    
    while not sukses:
        os.system('cls')
        print("\n")
        print("="*10, " BANK AJA - Masuk", "="*10)
        print("\n")
        
        usernama_kartu = input("Masukan Usernama atau Kartu : ")
        
        if usernama_kartu.lower() == 'keluar':
            sukses = False
            return {
                'auth' : False,
                'data' : None
            }
            
        ## CEK APAKAH USER ADA
        user = cek_user_kartu(usernama_kartu)
        
        if type(user) != type(False):
            for i in range(3):
                pin = input("Masukan PIN : ")
                
                #CEK PIN
                sesi = cek_pin(pin, user)
                
                if not sesi['auth']:
                    print(f"GAGAL MASUK! ULANGI {i}/3")
                    time.sleep(1)
                    continue
                else:
                    print(f"BERHASIL MASUK")
                    time.sleep(1)
                    sukses = True
                    return sesi
                
            print("ANDA TELAH MENCOBA 3 KALI, ANDA AKAN KELUAR!")
            time.sleep(1)
            return {
                'auth' : False,
                'data' : None
            }
        
        else:
            print("GAGAL MASUK! ULANGI")
            time.sleep(1)