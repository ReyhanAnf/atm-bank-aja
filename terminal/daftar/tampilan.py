
import os, hashlib, time

def formulir_daftar():
    valid = False
    
    while valid != True:
        os.system('cls')
        print("\n")
        print("="*10, " BANK AJA - Daftar", "="*10)
        print("\n")
        
        nama = input("Nama : ")
        usernama = input("Usernama : ")
        email = input("Email : ")
        keanggotaan = input("Keangotaan [Silver/Gold/Platinum] : ")
        no_hp = input("Nomor HP : ")
        tanggal_lahir = input("Tanggal Lahir [31/12/2000] : ")
        alamat = input("Alamat : ")
        
        pin = input("PIN : ")
        h = hashlib.new('sha256')
        h.update(bytes(pin, encoding='utf-8'))
        pin = h.hexdigest()
        
        kpin = input("Konfirmasi PIN : ")
        h = hashlib.new('sha256')
        h.update(bytes(kpin, encoding='utf-8'))
        kpin = h.hexdigest()
        
        if pin == kpin:
            data = {
                'nama': nama,
                'usernama': usernama,
                'email' : email,
                'keanggotaan': keanggotaan,
                'no_hp' : no_hp,
                'kelahiran' : tanggal_lahir,
                'alamat' : alamat,
                'pin' : pin
            }
            valid = True
            return data
        else:
            time.sleep(1)
            valid = False
        
        
        
        
def kartu_atm(data):
    data_keys = data.keys()
    
    table = ""
    for key in data_keys:
        text = f"{key:<20} | {data[key]:>20} \n"
        table += text
    return table