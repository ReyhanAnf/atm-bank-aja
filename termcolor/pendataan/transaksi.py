import pandas as pd
import numpy as np

from .user import data_user

pd.set_option('display.max_columns', None)


def data_transaksi():
    df = pd.read_csv('./data/transaksi.csv')
    return df


def tambah_transaksi(data):
    df = data_transaksi()
    df.loc[len(df)] = data

    df.to_csv('./data/user.csv', index=False)


def update_transaksi(kode, kolom, nilai_baru):
    df = data_transaksi()
    df_tujuan = df[df['kode'] == kode]
    
    if not df_tujuan.empty:
        df.loc[df['kode'] == kode, kolom] = nilai_baru
        
        df.to_csv('./data/transaksi.csv', index=False)
        print('transaksi berhasil')
        
    else:
        print(f'Data dengan kode: {kode}, Tidak ditemukan')
        

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