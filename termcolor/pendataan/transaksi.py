import pandas as pd
import numpy as np
import datetime

from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

from ..menu.tampilan import pilihan_menu
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
        return False



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



def konfirmasi_transaksi(data):
    if type(data['penerima']) == type('str'):
        penerima = data['penerima']
    else:
        penerima = f"{data['penerima']['nama']} - {data['penerima']['nomor_kartu']}"
        
    content = f""" 
                    Nama Pengirim: {data['pengirim']['nama']} - {data['pengirim']['nomor_kartu']}\n
                    Nama Penerima: {penerima} \n
                    Metode: {data['metode']} \n
                    Admin: Rp {data['admin']:,.2f} \n
                    Jumlah: Rp {data['jumlah']:,.2f} \n
                    Total: Rp {data['total']:,.2f}
                    """.upper()
                    
    
    lay = Layout(Text(content))
    
    print("\n\n")
    
    judul = Panel(renderable=lay, title=f"KONFIRMASI TRANSAKSI - {data['metode'].upper()}", height=17, padding=1, highlight=True)
    print(judul)
    
    print(Panel(Text("PERIKSA KEMBALI DATA!!", style="black on yellow", justify='center')))
    
    menu = ["Konfirmasi dan Lanjut", "Koreksi Data", "Keluar"]
    text = pilihan_menu(menu)
    print(text)
    
    pilihan = int(Prompt.ask("Pilih"))
    if pilihan == 1:
        data['kode'] = generate_kode(data['metode'], 10)
        return [True, data]
    elif pilihan == 2:
        return [False, data]
    else:
        return [False, None]
    
    