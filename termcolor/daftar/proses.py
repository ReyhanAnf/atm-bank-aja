import numpy as np
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

from ..pendataan.user import tambah_user

import time

def generate_kode(len):
    kode = ''
    
    
    random = np.random.randint(0,9, size=len)
    for i in random:
        kode += str(i)
    
    return kode

    
def daftar_user(data):
    print(Text(".....Mengupload..", justify='center'))
    
    time.sleep(.7)
    
    tambah_user(data)
    print(Panel(Text("SELAMAT ANDA SUDAH TERDAFTAR!", style="white on green", justify='center')))


def isi_saldo_awal(data):
    data = data
    data['saldo'] = 0
    valid = False
    
    while valid != True:
        saldo = int(Prompt.ask("Saldo Awal"))
        if saldo >= 50000:
            data['saldo'] += saldo
            valid = True
        else:
            valid = False