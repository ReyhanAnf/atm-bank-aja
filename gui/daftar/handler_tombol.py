# Import library eksternal yaitu library TKinter atau CustomTKinter , time dan hashlib  
import time, hashlib
import customtkinter as ctk

# Import module internal
from ..pendataan.user import cek_user_kartu
from .proses import generate_kode, kartu_atm

# Fungsi untuk kembali ke home
def kembali_ke_home(app, frame):
    from ..awal.main import home
    home(app, frame)

# Fungsi untuk menghandel tombol daftar dan melanjutkan proses daftar
def handle_daftar(app, frame, inputs):
    # Konversi data dalam inputs kedalam variabel data dengan mengambil data dalam inputan dengan method get
    # Karena inputan masih merupakan data dummy
    data = {
        'nama': inputs['nama'].get(),
        'usernama': inputs['usernama'].get(),
        'email' : inputs['email'].get(),
        'no_hp' : inputs['no_hp'].get(),
        'keanggotaan': inputs['anggota'].get(),
        'kelahiran': inputs['lahir'].get(),
        'alamat': inputs['alamat'].get('0.0', 'end'),
        'pin': inputs['pin'].get(),
        'saldo': inputs['saldo'].get(),
        'dibuat': time.time()
    }
    
    # mengecek apakah usernama yang diinputkan sudah terdaftar atau belu,m
    user = cek_user_kartu(data['usernama'])
    
    # Jika False atau belum terdaftar maka lanjutkan pendaftaran
    if type(user) == type(False):
        # Jika pin yang dimasukan tidak sama dengan konfirmasi pin
        if data['pin'] != inputs['kpin'].get():
            # Maka tampilkan gagal masuk
            gagal = ctk.CTkLabel(frame['body'], text="MASUKAN PIN DENGAN BENAR", fg_color="orange")
            gagal.pack(side='top', fill='x', expand=True)
        else:
            # Jika pin sama dengan konfirmasi pin
            # HASHING PIN
            h = hashlib.new('sha256')
            h.update(bytes(data['pin'], encoding='utf-8'))
            data['pin'] = h.hexdigest()
            
            # Coba apakah program akan sukses atau error
            try:
                # konversi saldo kedalam integer, jika ada yang menginput karakter maka akan terdeteksi error
                saldo = int(data['saldo'])
                
                # KETERANGAN SUKSES
                sukses1 = ctk.CTkLabel(frame['body'], text="SALDO BERHASIL DITAMBAHKAN", fg_color='green') # Label Inputan
                sukses1.pack(side='top', fill='x', expand=True)
                
                # KETERANGAN SUKSES
                sukses2 = ctk.CTkLabel(frame['body'], text="DATA VALID", fg_color="green")
                sukses2.pack(side='top', fill='x', expand=True)
                
                # Generate nomor kartu, kode seri dan tambahkan saldo kedalam data dengan memanggil fungsi terkait
                data['nomor_kartu'] = generate_kode(8)
                data['kode_seri'] = generate_kode(5)
                data['saldo'] = saldo
                
                # Tampilkan kartu atm untuk melihat preview data yang diinputkan
                kartu_atm(app, frame, data)
                
            except Exception:
                # Jika terdeteksi error maka akan tampilkan peringatan bukan angka
                gagal = ctk.CTkLabel(frame['body'], text="Saldo Bukan Angka", fg_color="green")
                gagal.pack(side='top', fill='x', expand=True)
                
    
    else:
        # Jika ternyata user sudah terdaftar maka tampilkan peringatan
        gagal = ctk.CTkLabel(frame['body'], text="USER TELAH TERDAFTAR", fg_color="yellow", text_color='black')
        gagal.pack(side='top', fill='x', expand=True)
    
    
    # Hapus pesan peringatan atau sukses sebelumnya ketika pesan baru dimunculkan.
    # Sehingga akan tampil 1 peringatan ketika 1 aksi 
    banyak_komponen = len(frame['body'].winfo_children())
    if banyak_komponen > 9:
        child = frame['body'].winfo_children()[banyak_komponen - 2]
        child.destroy()
        
