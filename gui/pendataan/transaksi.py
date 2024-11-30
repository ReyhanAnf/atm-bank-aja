import pandas as pd
import numpy as np
import datetime

import customtkinter as ctk
from ..setelan import reset_frame

# from ..menu.tampilan import pilihan_menu
from .user import data_user

pd.set_option('display.max_columns', None)


def data_transaksi():
    df = pd.read_csv('./data/transaksi.csv')
    return df


def tambah_transaksi(data):
    data['status'] = 'sukses'
    data['waktu'] = datetime.datetime.now()
    
    df = data_transaksi()
    df.loc[len(df)] = data
    

    df.to_csv('./data/transaksi.csv', index=False)
    return True


def update_transaksi(kode, kolom, nilai_baru):
    df = data_transaksi()
    df_tujuan = df[df['kode'] == kode]
    
    if not df_tujuan.empty:
        df.loc[df['kode'] == kode, kolom] = nilai_baru
        
        df.to_csv('./data/transaksi.csv', index=False)
        print('transaksi berhasil')
        return True
        
    else:
        print(f'Data dengan kode: {kode}, Tidak ditemukan')
        return False
        

def cek_penerima(identity):
    df = data_user()
    
    if not df.loc[df['usernama'] == identity].empty:
        index = df.loc[df['usernama'] == identity].index[0]
        return df.iloc[index]
    elif not df.loc[df['nomor_kartu'] == identity].empty:
        index = df.loc[df['nomor_kartu'] == identity].index[0]
        return df.iloc[index]
    else:
        return f"{identity} - None"



def generate_kode(metode, len):
    kode = ''
    
    if metode.lower() == 'transfer':
        kode += 'TRF-'
    elif metode.lower() == 'setor':
        kode += 'STR-'
    elif metode.lower() == 'tarik':
        kode += 'TRK-'
    else:
        kode += 'A-'
    
    random = np.random.randint(0,9, size=len)
    for i in random:
        kode += str(i)
    
    return kode



def konfirmasi_transaksi(app, frame, sesi, data, mutasi):
    reset_frame(frame['body'])
    reset_frame(frame['footer'])
    
    kode = generate_kode(data['metode'], 10)
    data['kode'] = kode
    
    
    if type(data['penerima']) == type('str'):
        penerima = data['penerima']
        data['penerima'] = cek_penerima(data['penerima'])
    else:
        penerima = data['penerima']
        penerima = f"{penerima['nama']} - {penerima['nomor_kartu']}"
    
    
    
    content = {
        'Nama_Pengirim' : f"{data['pengirim']['nama']} - {data['pengirim']['nomor_kartu']}",
        'Nama_Penerima' : penerima,
        'Metode': data['metode'],
        'Jumlah' : f"Rp {data['jumlah']:,}",
        'Admin' : f"Rp {data['admin']:,}",
        'Total' : f"Rp {data['total']:,}",
    }

    if data['metode'] != 'transfer':
        del content['Nama_Pengirim']
        del content['Nama_Penerima']
        nama = {'Nama': f"{data['pengirim']['nama']} - {data['pengirim']['nomor_kartu']}"}
        content = {**nama, **content}
    
      
    kcontent = content.keys()
    
    for key in kcontent:
        ########### INPUT USER
        # Buat pembungkus untuk untuk inputan nama
        wrap = ctk.CTkFrame(frame['body'], fg_color='transparent') # Pembungkus
        wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
        
        # Buat keterangan tentang input
        text_key = " ".join(key.split("_"))
        label = ctk.CTkLabel(wrap, text=text_key, text_color='white') # Label Inputan
        label.pack(side='left', padx=10, pady=5)
        
        # buat inputan
        isian = ctk.CTkLabel(wrap, corner_radius=10, text=content[key], width=300, text_color='white') # Inputan
        isian.pack(side='right', padx=10, pady=5)
    
    ################################################## FOOTER
    ######################################### 
    
    def transaksi_handle():
        status = mutasi(data)
        if status == True:
            sukses = ctk.CTkLabel(frame['body'], text=f"{data['metode'].upper()} BERHASIL", fg_color="green")
            sukses.pack(side='top', fill='x', expand=True)
            
            from ..menu.main import dashboard
            reset_frame(frame['footer'])
            selesaiBtn = ctk.CTkButton(frame['footer'], height=50,text="Selesai", command=lambda : dashboard(app, frame, sesi))
            selesaiBtn.pack(side="left", fill='x', expand=True, padx=10)
        else:
            gagal = ctk.CTkLabel(frame['body'], text=f"{data['metode'].upper()} GAGAL", fg_color="red")
            gagal.pack(side='top', fill='x', expand=True)
            
            from ..menu.transfer.main import transfer
            reset_frame(frame['footer'])
            ulangBtn = ctk.CTkButton(frame['footer'], height=50,text="Ulangi", command=lambda : transfer(app, frame, sesi))
            ulangBtn.pack(side="left", fill='x', expand=True, padx=10)
            
    
    mutasiBtn = ctk.CTkButton(frame['footer'], height=50,text="Konfirmasi", command=transaksi_handle)
    mutasiBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    ######################################### 
    ################################################## FOOTER
    
    