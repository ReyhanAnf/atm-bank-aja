
import os, time

from .awal.tampilan import menu_awal
from .masuk.tampilan import formulir_masuk
from .daftar.tampilan import formulir_daftar, kartu_atm
from .daftar.proses import isi_saldo_awal, generate_kode

from .pendataan.user import tambah_user

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
            program_daftar = True
            
            while program_daftar:
                data = formulir_daftar()
                if data != None:
                    # Isi saldo
                    isi_saldo_awal(data)
                    # Bikin kode kartu atm
                    data['nomor_kartu'] = generate_kode(8)
                    # Bikin serial kode
                    data['kode_seri'] = generate_kode(4)
                    
                    print(kartu_atm(data))
                    
                    yakin = input("\t Apakah kamu sudah yakin? [y/t] ")
                    if yakin.lower() == 'y' or yakin == '':
                        # upload atau tambah user
                        tambah_user(data)
                        time.sleep(1)
                        program_daftar = False
                        
                    else:
                        continue
                    
            
        elif pilihan == 0:
            print("keluar")
        else:
            print("Pilihan tidak valid")
        