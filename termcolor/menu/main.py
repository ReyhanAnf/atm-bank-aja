from rich import print
from rich.prompt import Prompt

import os

from .tampilan import pilihan_menu,header
from .info_rekening.main import info_rekening
from .cek_saldo.main import cek_saldo
from .transfer.main import formulir_transfer


def menu_utama(sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    data = sesi['data']
    
    # bersihkan terminal
    os.system('cls')
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    while auth:
        # menampilan header sebagai penanda ini di program bank aja dan menunjukan berada di menu apa
        header(judul="Menu", nama=data['nama'])
        
        # List menu pada fitur menu
        menu = ["Informasi Rekening", "Cek Saldo", "Histori Transaksi", "Transfer", 'Setor', "Tarik", "Transfer", "Bayar", "Keluar"]
        # List menu akan di konversi menjadi text yang bisa langsung di print menggunakan perulangan di fungsi 'pilihan_menu'
        text = pilihan_menu(menu)
        
        # menampilkan list menu sesuai variabel menu
        print(text)
        
        # menampung pilihan user untuk menentukan menu dan masuk ke langkah selanjutnya sesuai pilihan menu yang dipilih
        pilihan = int(Prompt.ask("Pilih"))
        
        # jika pilihan nya adalah 1 atau yang lainnya, maka jalankan program sesuai urutan data pada variabel menu
        if pilihan == 1:
            # jalankan program INFORMASI REKENING
            # info_rekening akan menampilkan informasi rekening dan mengembalikan nilai BOOLEAN yang mana akan menentukan apakah akan kembali ke menu utama atau keluar
            # Jika remenu = True maka akan kembali ke menu utama
            # Jika remenu = False maka akan keluar
            remenu = info_rekening(sesi)
            return remenu
        
        elif pilihan == 2:
            # jalankan program CEK SALDO
            # cek_saldo akan menampilkan informasi saldo dan mengembalikan nilai BOOLEAN yang mana akan menentukan apakah akan kembali ke menu utama atau keluar
            # Jika remenu = True maka akan kembali ke menu utama
            # Jika remenu = False maka akan keluar
            remenu = cek_saldo(sesi)
            return remenu
        elif pilihan == 4:
            # jalankan program CEK SALDO
            # cek_saldo akan menampilkan informasi saldo dan mengembalikan nilai BOOLEAN yang mana akan menentukan apakah akan kembali ke menu utama atau keluar
            # Jika remenu = True maka akan kembali ke menu utama
            # Jika remenu = False maka akan keluar
            remenu = formulir_transfer(sesi)
            return remenu
            
            
        elif pilihan == 0:
            return False
        
        
        else:
            break
    