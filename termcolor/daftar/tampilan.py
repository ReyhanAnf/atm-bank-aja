from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.layout import Layout


import os
import hashlib
import time


def formulir():
    valid = False
    
    while valid != True:
        os.system('cls')
        
        judul = Text.assemble("BANK", (" AJA", "cyan"), (" - REGISTRASI", "bold"), justify='center')
        deskripsi = Text.assemble("Isi Data dengan sesuai dan cek kembali!", justify='center')
        
        print(Panel(judul))
        print(Panel(deskripsi))
        
        
        nama = Prompt.ask("Nama")
        usernama = Prompt.ask("Usernama")
        email = Prompt.ask("Email")
        keanggotaan = Prompt.ask("Keanggotaan", choices=["Gold", "Platinum", "Diamond"], default="Gold")
        no_hp = Prompt.ask("No.Hp")
        tanggal_lahir = Prompt.ask("Tanggal Lahir cth:[31/01/2000]")
        alamat = Prompt.ask("Alamat")
        
        pin = Prompt.ask("PIN")
        h = hashlib.new('sha256')
        h.update(bytes(pin, encoding='utf-8'))
        pin = h.hexdigest()
        
        kpin = Prompt.ask("Konfirmasi PIN")
        h = hashlib.new('sha256')
        h.update(bytes(kpin, encoding='utf-8'))
        kpin = h.hexdigest()

        

        if pin == kpin:
            data = {
                'nama': nama,
                'usernama': usernama,
                'pin': pin,
                'email': email,
                'keanggotaan': keanggotaan,
                'no_hp': no_hp,
                'kelahiran': tanggal_lahir,
                'alamat': alamat,
                'dibuat': time.time()
            }
            
            return data
        else:
            print(Panel(Text("PIN TIDAK SESUAI!", style="bold white on red", justify='center')))
            time.sleep(3)
            valid = False
            
            
            

            
    
def kartu_atm(data):
    content = f" Nama: {data['nama']} \n\n Username: {data['usernama']} \n\n Email: {data['email']} \n\n No. Handphone: {data['no_hp']} \n\n Tanggal Lahir: {data['kelahiran']} \n\n Alamat: {data['alamat']}"
    content2 = f"=============== \n = {data['nomor_kartu']} = \n =============== \n\n Member: {data['keanggotaan']} \n\n Saldo: {data['saldo']}"
    
    lay = Layout()
    lay.split_row(
        Layout(Panel(Text(content))),
        Layout(Panel(Text(content2, style="bold")))
    )
    
    print("\n\n")
    
    judul = Panel(renderable=lay, title="DEBIT BANK AJA", height=17, padding=1, highlight=True)
    print(judul)
    
    print(Panel(Text("SCREENSHOT KARTU INI!! SIMPAN DAN INGAT!", style="black on yellow", justify='center')))
    

   
        
        
    
    
    
        
    
     
    
    