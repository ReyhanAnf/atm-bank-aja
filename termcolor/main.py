import os, time

from .awal.tampilan import menu_awal

from .daftar.proses import generate_kode, isi_saldo_awal, tambah_user
from .daftar.tampilan import formulir, kartu_atm

from .masuk.tampilan import formulir_masuk

from .menu.main import menu_utama


def main():
    program = True

    while program:
        os.system('cls')
        pilihan = menu_awal()
        
        
        if pilihan == 1:
            # LOGIN
            sesi = formulir_masuk()
            
            remenu = True
            while remenu:
                if sesi['auth'] == True:
                    #DASHBOARD
                    remenu = menu_utama(sesi)
                    if remenu == True:
                        continue
                    else:
                        break
                else:
                    break
            continue
                        
            
            
        elif pilihan == 2:
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
                        tambah_user(data)
                        time.sleep(1)
                        program_register = False
                    else:
                        continue
                else:
                    continue
                    
            
        elif pilihan == 0:
            exit()
            
            
        else:
            print("INPUT SALAH!")
        
        
        
        
        