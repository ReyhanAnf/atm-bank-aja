# Import library eksternal yaitu library TKinter atau CustomTKinter , time dan hashlib  
import time, hashlib
import customtkinter as ctk

# Import module internal
from ..pendataan.user import cek_user_kartu
from .proses import generate_kode, kartu_atm

component = ['canvas']

# Fungsi untuk menghandel tombol daftar dan melanjutkan proses daftar
def handle_daftar(inputs, canvas):
    canvas.delete(component[0])
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
                    text="DATA VALID",
                    fill="green",
                    font=("Poppins Medium", 16 * -1)
                )
                component.insert(0, status)
                
                # Generate nomor kartu, kode seri dan tambahkan saldo kedalam data dengan memanggil fungsi terkait
                data['nomor_kartu'] = generate_kode(8)
                data['kode_seri'] = generate_kode(5)
                data['saldo'] = saldo
                
                # Tampilkan kartu atm untuk melihat preview data yang diinputkan
                # kartu_atm(app, frame, data)
                
            except Exception:
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
        status = canvas.create_text(
            261.0,
            650.0,
            anchor="nw",
            text="GAGAL! USER TELAH TERDAFTAR",
            fill="red",
            font=("Poppins Medium", 16 * -1)
        )
        component.insert(0, status)
        
