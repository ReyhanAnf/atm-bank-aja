# Import library eksternal yaitu library TKinter atau CustomTKinter , time dan hashlib  
import time, hashlib

# Import module internal
from ..pendataan.user import cek_user_kartu, tambah_user
from .proses import generate_kode

component = ['canvas']

# Fungsi untuk menghandel tombol daftar dan melanjutkan proses daftar
def handle_daftar(canvas, inputs):
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
            status = canvas.create_text(
                261.0,
                650.0,
                anchor="nw",
                text="GAGAL DAFTAR",
                fill="red",
                font=("Poppins Medium", 16 * -1)
            )
            component.insert(0, status)
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
                status = canvas.create_text(
                    261.0,
                    650.0,
                    anchor="nw",
                    text="DATA VALID - PROSES MENDAFTAR....",
                    fill="green",
                    font=("Poppins Medium", 16 * -1)
                )
                component.insert(0, status)
                
                # Generate nomor kartu, kode seri dan tambahkan saldo kedalam data dengan memanggil fungsi terkait
                data['nomor_kartu'] = generate_kode(8)
                data['kode_seri'] = generate_kode(5)
                data['saldo'] = saldo
                
                # Tampilkan kartu atm untuk melihat preview data yang diinputkan
                
                try:
                    canvas.delete(component[0])
                    
                    # Tambahkan data user baru ke database
                    tambah_user(data)
                    status = canvas.create_text(
                        261.0,
                        650.0,
                        anchor="nw",
                        text="SUKSES MENDAFTAR",
                        fill="green",
                        font=("Poppins Medium", 16 * -1)
                    )
                    component.insert(0, status)
                        
                except Exception:
                    canvas.delete(component[0])
                    # Jika error dengan berbagai kondisi
                    # Tampilkan pesan gagal
                    status = canvas.create_text(
                        261.0,
                        650.0,
                        anchor="nw",
                        text="GAGAL MENDAFTAR",
                        fill="red",
                        font=("Poppins Medium", 16 * -1)
                    )
                    component.insert(0, status)
                
            except Exception:
                canvas.delete(component[0])
                # Jika terdeteksi error maka akan tampilkan peringatan bukan angka
                status = canvas.create_text(
                    261.0,
                    650.0,
                    anchor="nw",
                    text="GAGAL DAFTAR",
                    fill="red",
                    font=("Poppins Medium", 16 * -1)
                )
                component.insert(0, status)
                                
    
    else:
        # Jika ternyata user sudah terdaftar maka tampilkan peringatan
        canvas.delete(component[0])
        status = canvas.create_text(
            261.0,
            650.0,
            anchor="nw",
            text="GAGAL! USER TELAH TERDAFTAR",
            fill="red",
            font=("Poppins Medium", 16 * -1)
        )
        component.insert(0, status)
        
