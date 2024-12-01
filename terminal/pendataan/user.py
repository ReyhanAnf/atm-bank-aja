import pandas as pd
pd.set_option('display.max_columns', None)


def data_user():
    df = pd.read_csv('./data/user.csv')
    return df


def tambah_user(data):
    df = data_user()
    
    df.loc[len(df)] = data
    df.to_csv('./data/user.csv', index=False)


def cek_user_kartu(inputer):
    df = data_user()
    
    if not df.loc[df['usernama'] == inputer].empty:
        index = df.loc[df['usernama'] == inputer].index[0]
        return df.iloc[index]
    elif not df.loc[df['nomor_kartu'] == inputer].empty:
        index = df.loc[df['nomor_kartu'] == inputer].index[0]
        return df.iloc[index]
    else:
        return False