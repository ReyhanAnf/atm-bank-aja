import time, hashlib

import customtkinter as ctk

from ..pendataan.user import cek_user_kartu
from .proses import generate_kode, kartu_atm

def kembali_ke_home(app, frame):
    from ..awal.main import home
    home(app, frame)


def handle_daftar(app, frame, inputs):
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
    
    user = cek_user_kartu(data['usernama'])
    
      
    if type(user) == type(False):
        if data['pin'] != inputs['kpin'].get():
            gagal = ctk.CTkLabel(frame['body'], text="MASUKAN PIN DENGAN BENAR", fg_color="orange")
            gagal.pack(side='top', fill='x', expand=True)
        else:
            
            # HASHING PIN
            h = hashlib.new('sha256')
            h.update(bytes(data['pin'], encoding='utf-8'))
            data['pin'] = h.hexdigest()
            
            try:
                saldo = int(data['saldo'])
                
                # KETERANGAN SUKSES
                sukses1 = ctk.CTkLabel(frame['body'], text="SALDO BERHASIL DITAMBAHKAN", fg_color='green') # Label Inputan
                sukses1.pack(side='top', fill='x', expand=True)
                
                # KETERANGAN SUKSES
                sukses2 = ctk.CTkLabel(frame['body'], text="DATA VALID", fg_color="green")
                sukses2.pack(side='top', fill='x', expand=True)
                
                
                data['nomor_kartu'] = generate_kode(8)
                data['kode_seri'] = generate_kode(5)
                data['saldo'] = saldo
                
                
                kartu_atm(app, frame, data)
                
            except Exception:
                print("Bukan number")
                
    
    else:
        gagal = ctk.CTkLabel(frame['body'], text="USER TELAH TERDAFTAR", fg_color="yellow", text_color='black')
        gagal.pack(side='top', fill='x', expand=True)
        
    
    banyak_komponen = len(frame['body'].winfo_children())
    if banyak_komponen > 9:
        child = frame['body'].winfo_children()[banyak_komponen - 2]
        child.destroy()
        
