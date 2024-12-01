# import module sendiri dari folder dalam project
import termcolor
import terminal
import gui

# Buat pilihan tampilan aplikasi
menu = """
    =========== \n
    1. Tampilan Biasa \n
    2. Tampilan Berwarna \n
    3. GUI \n
    =========== \n
"""

#Tampilkan pilihan tampilan aplikasi
print(menu)

# Inputan pilihan tampilan
mode = int(input('Pilih : '))

# Jika yang dipilih 1 maka jalankan tampilan terminal
# Jika yang dipilih 2 maka jalankan tampilan terminal berwarna
# Jika yang dipilih 3 maka jalankan tampilan GUI
# Jika inputan tidak sesuai maka keluarkan pesan "pilihan salah"
if mode == 1:
    terminal.main()
elif mode == 2:
    termcolor.main()
elif mode == 3:
    gui.main()
else:
    print("Pilihan Salah")
    
    
