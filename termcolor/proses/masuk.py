import hashlib
from ..model.user import get_user

def cek_user_kartu(inputer):
    df = get_user()
    
    if not df.loc[df['usernama'] == inputer].empty:
        index = df.loc[df['usernama'] == inputer].index[0]
        return df.iloc[index]
    elif not df.loc[df['nomor_kartu'] == inputer].empty:
        index = df.loc[df['nomor_kartu'] == inputer].index[0]
        return df.iloc[index]
    else:
        return False
    
def cek_pin(pin_input, user):
    pin_user = user['pin']
    
    h = hashlib.new('sha256')
    h.update(bytes(pin_input, encoding='utf-8'))
    pin_input = h.hexdigest()
    
    if pin_input == pin_user:
        return [True, user]
    else:
        return [False, None]
    