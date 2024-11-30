import hashlib
import pandas as pd

pd.set_option('display.max_columns', None)


def data_user():
    df = pd.read_csv('./data/user.csv')
    return df
 


def update_user(usernama, kolom, nilai_baru):
    df = data_user()
    df_tujuan = df[df['usernama'] == usernama]
    
    if not df_tujuan.empty:
        df.loc[df['usernama'] == usernama, kolom] = nilai_baru
        
        df.to_csv('./data/user.csv', index=False)
        return True
        
    else:
        print(f'Data dengan usernama: {usernama}, Tidak ditemukan')
        return False


def tambah_user(data):
    df = data_user()
    df.loc[len(df)] = data

    df.to_csv('./data/user.csv', index=False)


def cek_user_kartu(inputer):
    df = data_user()
    
    if not df.loc[df['usernama'] == inputer].empty:
        index = df.loc[df['usernama'] == inputer].index[0]
        return df.iloc[index]
    elif not df.loc[df['nomor_kartu'] == int(inputer)].empty:
        index = df.loc[df['nomor_kartu'] == int(inputer)].index[0]
        return df.iloc[index]
    else:
        return False



    
def cek_pin(pin_input, user):
    pin_user = user['pin']
    
    h = hashlib.new('sha256')
    h.update(bytes(pin_input, encoding='utf-8'))
    pin_input = h.hexdigest()
    
    
    if pin_input == pin_user:
        return {'auth': True, 'data': user}
    else:
        return {'auth': False, 'data': None}