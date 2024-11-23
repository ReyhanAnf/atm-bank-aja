import termcolor
import terminal

menu = """
    =========== \n
    1. Tampilan Biasa \n
    2. Tampilan Berwarna \n
    3. GUI \n
    =========== \n
"""
print(menu)

mode = int(input('Pilih : '))

if mode == 1:
    terminal.main()
elif mode == 2:
    termcolor.main()
else:
    print("Pilihan Salah")
    
    
