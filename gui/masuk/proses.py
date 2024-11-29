import hashlib

    
def cek_pin(pin_input, user):
    pin_user = user['pin']
    
    h = hashlib.new('sha256')
    h.update(bytes(pin_input, encoding='utf-8'))
    pin_input = h.hexdigest()
    
    
    if pin_input == pin_user:
        return {'auth': True, 'data': user}
    else:
        return {'auth': False, 'data': None}
    