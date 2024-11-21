import os, time

from .tampilan.awal import menu_awal
from .tampilan.daftar import formulir, isi_saldo_awal, kartu_atm, simpan_user
from .tampilan.masuk import formulir_masuk
from .tampilan.menu import menu_utama

from .proses.daftar import generate_kode

def main():
    program = True
    
    while program:
        os.system('cls')
        pilihan = menu_awal()
        
        
        if(pilihan == 1):
            # LOGIN
            session = formulir_masuk()
            if session[0]:
                menu_utama(session)
            
            
        elif(pilihan == 2):
            # REGISTER
            program_register = True
            while program_register:
                data = formulir()
                if data != None:
                    isi_saldo_awal(data)
                    data['nomor_kartu'] = generate_kode(8)
                    data['kode_seri'] = generate_kode(4)
                    
                    kartu_atm(data)
                    
                    yakin = input("Yakin data sudah benar? [y/t]")
                    if yakin.lower() == 'y':
                        simpan_user(data)
                        time.sleep(10)
                        program_register = False
                    else:
                        continue
                else:
                    continue
                    
            
        elif(pilihan == 3):
            exit()
            
            
        else:
            print("INPUT SALAH!")
    
    
    
    
    