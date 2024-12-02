import customtkinter as ctk

from ...pendataan.transaksi import konfirmasi_transaksi
from .proses import mutasi

def setor_handler(app, frame, inputs, sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi Q'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    if auth == True:
        # Masukan semua data dalam inputs kedalam variabel tersendiri
        # Masing^ data dalam inputs mengandung nilai dummy object yang harus di ambil melalui method .get()
        nominal_input = inputs['nominal'].get()

        # Konversi nominal input menjadi integer (untuk menghindari pengisian nominal dengan karakter)
        # Simpan kedalam variabel nominal
        nominal = int(nominal_input)
        
        # JIka nominal lebih dari  Rp 10.000 (Minimal pembayaran adalah 10000) dan merupakan kelipatan 50.000
        if nominal > 10000 and nominal % 50000 == 0:
            # Maka lanjutkan ke proses mutasi
            
            # TAMPILAN KETERANGAN SUKSES DAN SIAP MENGIRIM
            sukses = ctk.CTkLabel(frame['body'], text="PROSES...", fg_color='green') # Label Inputan
            sukses.pack(side='top', fill='x', expand=True)
            
            # TAMPILAN PRORES MENGIRIM DAN MULAI PROSES
            progressbar = ctk.CTkProgressBar(frame['body'], orientation="horizontal", mode='indeterminate', determinate_speed=5, indeterminate_speed=1)
            progressbar.start()
            progressbar.pack(pady=20)
            
            # Deklarasi variabel metode, admin dan total
            metode = 'setor'
            admin = 0
            total = nominal + admin
            
            # Tampung semua inputan dan variabel tambahan kedalam variabel data dengan key yang sesuai dengan kolom pada database
            data = {
                'pengirim': user,
                'penerima': user,
                'metode': metode,
                'admin' : admin,
                'status' : 'menunggu',
                'jumlah': nominal,
                'total' : total
            }
            
            # Jalankan fungsi konfirmasi_transaksi untuk mengkonfirmasi dan melanjutkan mutasi data
            # FUNGSI MUTASI
            # Fungsi mutasi berasal dari masing masing aktivitas menu transaksi. Tiap menu transaksi memiliki mutasi berbeda
            # JIka bayar maka saldo pengirim saja yang dikurangi
            # Jika Setor maka saldo penerima ditambah
            # Jika Transfer maka saldo keduanya ditambah dan dikurang
            konfirmasi_transaksi(app, frame, sesi, data, mutasi)
            
        else:
            ## Kurang dari Rp 10.000 dan bukan kelipatan 50.000
            # KETERANGAN GAGAL
            gagal = ctk.CTkLabel(frame['body'], text="NOMINAL MERUPAKAN KELIPATAN RP 50.000", fg_color='orange') # Label Inputan
            gagal.pack(side='top', fill='x', expand=True)

        # Hapus pesan peringatan atau sukses sebelumnya ketika pesan baru dimunculkan.
        # Sehingga akan tampil 1 peringatan ketika 1 aksi 
        banyak_komponen = len(frame['body'].winfo_children())
        if banyak_komponen > 9:
            child = frame['body'].winfo_children()[banyak_komponen - 2]
            child.destroy()
            
            
                
        ################################################## FOOTER
        ######################################### 
        
        # Buat tombol koreksi dan ketika di klik akan kembali mengisi form
        from .main import setor
        koreksiBtn = ctk.CTkButton(frame['footer'], height=50,text="Koreksi", fg_color='orange', text_color='black', command=lambda : setor(app, frame, sesi))
        koreksiBtn.pack(side="left", fill='x', expand=True, padx=10)
        
        
        ######################################### 
        ################################################## FOOTER