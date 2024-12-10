# Import library eksternal yaitu library TKinter atau CustomTKinter dan numpy
import customtkinter as ctk
import numpy as np

# Import module internal
from ..pendataan.user import tambah_user
from ..setelan import reset_frame


# Fungsi untuk generate kode id kartu
# memiliki parameter  len -> int untuk seberapa panjang karakter kode yang diinginkan
def generate_kode(len):
    # buat variabel kode dengan string kosong untuk menampug nomor acak
    kode = ''
    
    # Buat len(misal 8) list angka random menggunakan modul numpy dengan range angka random dari 0 sampai 9
    random = np.random.randint(0,9, size=len)
    # Setiap nilai dari random akan di petakan kedalam variabel i
    for i in random:
        # variabel kode di tambah dengan angka acak yang telah diubah menjadi str
        kode += str(i)
    
    # kembalikan str kode
    return kode

