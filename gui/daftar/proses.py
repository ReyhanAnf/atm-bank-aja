import numpy as np

import customtkinter as ctk

from ..pendataan.user import tambah_user
from ..setelan import reset_frame


def generate_kode(len):
    kode = ''
    
    
    random = np.random.randint(0,9, size=len)
    for i in random:
        kode += str(i)
    
    return kode

    
def daftar_user(app, frame, data):
    progressbar = ctk.CTkProgressBar(frame['body'], orientation="horizontal", mode='indeterminate', determinate_speed=5, indeterminate_speed=1)
    progressbar.start()
    
    progressbar.pack(pady=20)
    
    
    try:
        tambah_user(data)
    
        sukses_wrap = ctk.CTkFrame(frame['body'], width=700)
        sukses_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
        
        sukses = ctk.CTkLabel(sukses_wrap, text="Anda Sudah Terdaftar!", text_color='white', fg_color='green', font=('Arial', 22))
        sukses.pack(side='top', padx=5, pady=5, fill='x', expand=True)
        
        ###################################################### FOOTER
        ######################################################
        reset_frame(frame['footer'])
        
        from .handler_tombol import kembali_ke_home
        batalBtn = ctk.CTkButton(frame['footer'], height=50,text="Selesai", command=lambda : kembali_ke_home(app, frame))
        batalBtn.pack(side="left", fill='x', expand=True, padx=10)
        ###################################################### 
        ###################################################### FOOTER
            
    except Exception:
        gagal_wrap = ctk.CTkFrame(frame['body'], width=700)
        gagal_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
        
        gagal = ctk.CTkLabel(gagal_wrap, text="Gagal Terdaftar!", text_color='black', fg_color='red', font=('Arial', 22))
        gagal.pack(side='top', padx=5, pady=5, fill='x', expand=True)
        
    


     
            
def kartu_atm(app, frame, data):
    reset_frame(frame['body'])
    reset_frame(frame['footer'])
    
    kartu_wrap = ctk.CTkFrame(frame['body'], width=700, height=350, fg_color='white')
    kartu_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
    
    judul = ctk.CTkButton(kartu_wrap, text="ATM BANK AJA", fg_color='white', text_color='green', font=('Arial', 22))
    judul.pack(side='top', padx=5, pady=5, fill='x', expand=True)
    
    nomor_kartu = ctk.CTkButton(kartu_wrap, text=data['nomor_kartu'], fg_color='black', text_color='white', font=('Arial', 26))
    nomor_kartu.pack(side='top', padx=5, pady=5, fill='x', expand=True)
    
    data_kartu_wrap = ctk.CTkFrame(kartu_wrap, width=700, height=350, fg_color='white')
    data_kartu_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
    
    nama = ctk.CTkLabel(data_kartu_wrap, text=data['nama'], text_color='black', font=('Arial', 16))
    nama.grid(row=0, column=1, padx=15, pady=5, columnspan=4, sticky='ew')
    
    usernama = ctk.CTkLabel(data_kartu_wrap, text=data['usernama'], text_color='black', font=('Arial', 16))
    usernama.grid(row=1, column=1, padx=15, pady=5, columnspan=4, sticky='ew')
    
    email = ctk.CTkLabel(data_kartu_wrap, text=data['email'], text_color='black', font=('Arial', 20))
    email.grid(row=2, column=1, padx=15, pady=5, columnspan=4, sticky='ew')
    
    no_hp = ctk.CTkLabel(data_kartu_wrap, text=data['no_hp'], text_color='black', font=('Arial', 20))
    no_hp.grid(row=2, column=1, padx=15, pady=5, columnspan=4, sticky='ew')
    
    anggota = ctk.CTkLabel(data_kartu_wrap, text=data['keanggotaan'], text_color='black', font=('Arial', 20))
    anggota.grid(row=3, column=1, padx=15, pady=5, columnspan=4, sticky='ew')
    
    lahir = ctk.CTkLabel(data_kartu_wrap, text=data['kelahiran'], text_color='black', font=('Arial', 20))
    lahir.grid(row=4, column=1, padx=15, pady=5, columnspan=4, sticky='ew')
    
    alamat = ctk.CTkLabel(data_kartu_wrap, text=data['alamat'], text_color='black', font=('Arial', 20))
    alamat.grid(row=5, column=1, padx=15, pady=5, columnspan=4, sticky='ew')
    
    saldo = ctk.CTkButton(kartu_wrap, text=f"Rp. {data['saldo']:,.2f}", text_color='black', font=('Arial', 20))
    saldo.pack(side='left', padx=10, pady=10)
    
    kode_seri = ctk.CTkButton(kartu_wrap, text=data['kode_seri'], text_color='black', font=('Arial', 20))
    kode_seri.pack(side='right', padx=10, pady=10)
    
    
    
    dialog_wrap = ctk.CTkFrame(frame['body'], width=700)
    dialog_wrap.pack(side='top', padx=10, pady=10, fill='x', expand=True)
    
    dialog = ctk.CTkLabel(dialog_wrap, text="Apakah anda sudah yakin data sudah benar? ", text_color='white', font=('Arial', 22))
    dialog.pack(side='top', padx=5, pady=5, fill='x', expand=True)
    
    
    ###################################################### FOOTER
    ######################################################
    from .handler_tombol import kembali_ke_home
    batalBtn = ctk.CTkButton(frame['footer'], height=50,text="Batal", command=lambda : kembali_ke_home(app, frame))
    batalBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    
    daftarBtn = ctk.CTkButton(frame['footer'], height=50,text="Ya & Daftar", command=lambda : daftar_user(app, frame, data))
    daftarBtn.pack(side="left", fill='x', expand=True, padx=10)
    ###################################################### 
    ###################################################### FOOTER