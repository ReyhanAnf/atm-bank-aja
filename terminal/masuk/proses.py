import hashlib

def cek_pin(pin_input, user):
    pin_user = user['pin']
    
    h = hashlib.new('sha256')
    h.update(bytes(pin_input, 'utf-8'))
    pin_input = h.hexdigest()
    
    if pin_user == pin_input:
        return {
            'auth' : True,
            'data' : user
        }
    else:
        return {
            'auth' : False,
            'data' : None
        }