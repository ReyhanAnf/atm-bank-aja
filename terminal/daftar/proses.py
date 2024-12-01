import numpy as np

def generate_kode(len):
    kode = ''
    
    random = np.random.randint(0,9, size=len)
    for r in random:
        kode += str(r)
    
    return kode

def isi_saldo_awal(data):
    data = data
    data['saldo'] = 0
    
    valid = False
    while valid != True:
        saldo = int(input('Saldo Awal : '))
        
        if saldo < 50000:
            print("Minimal Saldo Awal adalah Rp 50.000")
            continue
        else:
            data['saldo'] += saldo
            valid = True