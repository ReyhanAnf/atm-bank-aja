import numpy as np

def generate_kode(len):
    kode = ''
    
    
    random = np.random.randint(0,9, size=len)
    for i in random:
        kode += str(i)
    
    return kode

