import time

import customtkinter as ctk

from ..pendataan.user import cek_user_kartu, cek_pin
from ..menu.main import dashboard

def kembali_ke_home(app, frame):
    from ..awal.main import home
    home(app, frame)


def handle_masuk(app, frame, inputs):
    user_input = inputs['usernama'].get()
    pin_input = inputs['pin'].get()
    
    user = cek_user_kartu(user_input)
    
      
    if type(user) != type(False):
        sesi = cek_pin(pin_input, user)
        
        if not sesi['auth']:
            gagal = ctk.CTkLabel(frame['body'], text="GAGAL", fg_color="orange")
            gagal.pack(side='top', fill='x', expand=True)
        else:
            sukses = ctk.CTkLabel(frame['body'], text="BERHASIL", fg_color="green")
            sukses.pack(side='top', fill='x', expand=True)
            
            time.sleep(1)
            
            dashboard(app, frame, sesi)
    
    else:
        gagal = ctk.CTkLabel(frame['body'], text="USER ATAU NOMOR KARTU TIDAK DITEMUKAN", fg_color="yellow", text_color='black')
        gagal.pack(side='top', fill='x', expand=True)
        
    
    banyak_komponen = len(frame['body'].winfo_children())
    if banyak_komponen > 3:
        child = frame['body'].winfo_children()[banyak_komponen - 2]
        child.destroy()