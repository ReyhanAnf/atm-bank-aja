import termcolor

mode = int(input('Masukan Jenis Keluaran /n [1. Berwarna]: '))

if mode == 1:
    termcolor.main()
else:
    print("Pilihan Salah")