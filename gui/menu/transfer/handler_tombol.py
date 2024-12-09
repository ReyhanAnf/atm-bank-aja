
from ...pendataan.transaksi import konfirmasi_transaksi
from .proses import mutasi


component = ['canvas']

def transfer_handle(app,canvas, sesi, inputs):
    canvas.delete(component[0])
    # Argumen sesi membawa nilai bertipe dict yang berisi key 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    
    app.geometry("687x549")
    app.configure(bg = "#EBF3FF")
    
    
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    if auth == True:
        
        # Masukan semua data dalam inputs kedalam variabel tersendiri
        # Masing^ data dalam inputs mengandung nilai dummy object yang harus di ambil melalui method .get()
        penerima_input = inputs['penerima'].get()
        nominal_input = inputs['nominal'].get()

        # Konversi nominal input menjadi integer (untuk menghindari pengisian nominal dengan karakter)
        # Simpan kedalam variabel nominal
        nominal = int(nominal_input)
        
        # JIka nominal lebih dari  Rp 10.000 (Minimal pembayaran adalah 10000) dan merupakan kelipatan 50.000
        if nominal >= 10000 and penerima_input != '':
            # Maka lanjutkan ke proses mutasi
            
            # TAMPILAN KETERANGAN SUKSES DAN SIAP MENGIRIM
            
            # TAMPILAN PRORES MENGIRIM DAN MULAI PROSES
            
            # Deklarasi variabel metode, admin dan total
            metode = 'transfer'
            admin = 2500
            total = nominal + admin
            
            # Tampung semua inputan dan variabel tambahan kedalam variabel data dengan key yang sesuai dengan kolom pada database
            data = {
                'pengirim': user,
                'penerima': penerima_input,
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
            
            konfirmasi_transaksi(app, sesi, data, mutasi)
            
            
        else:
            ## Kurang dari Rp 10.000 dan bukan kelipatan 50.000
            # KETERANGAN GAGAL
            status = canvas.create_text(
                186.0,
                380.0,
                anchor="nw",
                text="MINIMAL TRANSFER RP 10.000 DAN KELIPATAN RP 50.000",
                fill="red",
                font=("Poppins Medium", 16 * -1)
            )
            component.insert(0,status)

    else:
        status = canvas.create_text(
            186.0,
            380.0,
            anchor="nw",
            text="ANDA AKAN SEGERA KE MENU AWAL",
            fill="red",
            font=("Poppins Medium", 16 * -1)
        )
        component.insert(0,status)
        
        from ...awal.main import home
        import time
        time.sleep(2)
        home(app)