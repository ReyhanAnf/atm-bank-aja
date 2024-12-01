# Import library eksternal yaitu library TKinter atau CustomTKinter
import customtkinter as ctk

# Import module internal
from ..setelan import reset_frame
from .handler_tombol import kembali_ke_home, handle_daftar

# Fungsi untuk mengimput data dalam pendaftaran user
def formulir_daftar(app, frame):
    # Buat judul aplikasi
    app.title("BANK AJA - GUI")
    
    # Reset semua frame utama agar bersih dari widget lain
    reset_frame(frame['header'])
    reset_frame(frame['body'])
    reset_frame(frame['footer'])
    
    
    
    ###################################################### HEADER
    ###################################################### 
    
    # Buat tampilan judul untuk navigasi
    title = ctk.CTkButton(frame['header'], text="BANK AJA - DAFTAR", font=('Arial', 28, 'bold'))
    # Tampilkan tampilan judul untuk navigasi
    title.pack(side="top")
    
    ###################################################### 
    ###################################################### HEADER
    
    
    
    ###################################################### BODY
    ######################################################
    
    ########### INPUT USER
    # Buat pembungkus untuk untuk inputan nama
    nama_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    # Tampilkan pembungkus untuk untuk inputan nama
    nama_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    nama_Label = ctk.CTkLabel(nama_wrap, text="Nama Lengkap") # Label Inputan
    # Tampilkan keterangan tentang input
    nama_Label.pack(side='left', padx=10, pady=5
                    )
    # buat inputan
    nama_input = ctk.CTkEntry(nama_wrap, corner_radius=10, placeholder_text="Nama Lengkap", width=300, height=40) # Inputan
    # Tampilkan inputan
    nama_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT USERNAMA
    # Buat pembungkus untuk inputan usernama
    usernama_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    # Tampilkan pembungkus untuk inputan usernama
    usernama_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    usernamaLabel = ctk.CTkLabel(usernama_wrap, text="Usernama") # Label
    # Tampilkan keterangan tentang input
    usernamaLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    usernama_input = ctk.CTkEntry(usernama_wrap, corner_radius=10, placeholder_text="usernama", width=300, height=40) # Inputan
    # Tampilkan inputan
    usernama_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT EMAIL
    # Buat pembungkus untuk inputan email
    email_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    # Tampilkan pembungkus untuk inputan email
    email_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    emailLabel = ctk.CTkLabel(email_wrap, text="Email") # Label
    # Tampilkan keterangan tentang input
    emailLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    email_input = ctk.CTkEntry(email_wrap, corner_radius=10, placeholder_text="email", width=300, height=40) # Inputan
    # Tampilkan inputan
    email_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT No HP
    # Buat pembungkus untuk inputan nomor hp
    noHp_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    # Tampilkan pembungkus untuk inputan nomor hp
    noHp_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    noHpLabel = ctk.CTkLabel(noHp_wrap, text="Nomor HP") # Label
    # Tampilkan keterangan tentang input
    noHpLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    noHp_input = ctk.CTkEntry(noHp_wrap, corner_radius=10, placeholder_text="noHp", width=300, height=40) # Inputan
    # Tampilkan inputan
    noHp_input.pack(side='right', padx=10, pady=5)
    
    
    ############# INPUT ANGGOTA
    # Buat pembungkus untuk inoutan anggota
    anggota_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    # Tampilkan pembungkus untuk inoutan anggota
    anggota_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input atau Label
    anggotaLabel = ctk.CTkLabel(anggota_wrap, text="Anggota") # Label
    # Tampilkan keterangan tentang input atau Label
    anggotaLabel.pack(side='left', padx=10, pady=5)
    
    # Buat dan tampilkan Pilihan
    anggota_var = ctk.StringVar(value='gold') # Variabel penampung
    # Pilihan 1
    a_silver = ctk.CTkRadioButton(anggota_wrap, text="Silver", value='silver', variable=anggota_var) # Inputan
    a_silver.pack(side='right', padx=10, pady=5)
    # Pilihan 2
    a_gold = ctk.CTkRadioButton(anggota_wrap, text="Gold", value='gold', variable=anggota_var) # Inputan
    a_gold.pack(side='right', padx=10, pady=5)
    # Pilihan 3
    a_platinum = ctk.CTkRadioButton(anggota_wrap, text="Platinum", value='platinum', variable=anggota_var) # Inputan
    a_platinum.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT TANGGAL LAHIR
    # Buat pembungkus untuk inputan tanggal lahir
    lahir_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    # Buat pembungkus untuk inputan tanggal lahir
    lahir_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    lahirLabel = ctk.CTkLabel(lahir_wrap, text="Tanggal Lahir") # Label
    # Tampilkan keterangan tentang input
    lahirLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    lahir_input = ctk.CTkEntry(lahir_wrap, corner_radius=10, placeholder_text="01/01/2000", width=300, height=40) # Inputan
    # Tampilkan inputan
    lahir_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT ALAMAT
    # Buat pembungkus untuk inputan alamat
    alamat_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    # Tampilkan pembungkus untuk inputan alamat
    alamat_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    alamatLabel = ctk.CTkLabel(alamat_wrap, text="Alamat") # Label
    # Tampilkan keterangan tentang input
    alamatLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    alamat_input = ctk.CTkTextbox(alamat_wrap, corner_radius=10, width=300, height=40) # Inputan
    # Tampilkan inputan
    alamat_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT PIN
    # Buat pembungkus untuk inputan pin
    pin_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    # Tampilkan pembungkus untuk inputan pin
    pin_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    pinLabel = ctk.CTkLabel(pin_wrap, text="PIN") # Label
    # Tampilkan keterangan tentang input
    pinLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    pin_input = ctk.CTkEntry(pin_wrap, corner_radius=10, placeholder_text="***", width=300, height=40) # Inputan
    # Tampilkan inputan
    pin_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT KONFIRMASI PIN
    # Buat pembungkus untuk inputan pin
    kpin_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    # Tampilkan pembungkus untuk inputan pin
    kpin_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    kpinLabel = ctk.CTkLabel(kpin_wrap, text="KONFIRMASI PIN") # Label
    # Tampilkan keterangan tentang input
    kpinLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    kpin_input = ctk.CTkEntry(kpin_wrap, corner_radius=10, placeholder_text="***", width=300, height=40) # Inputan
    # Tampilkan inputan
    kpin_input.pack(side='right', padx=10, pady=5)
    
    
    ########### INPUT SALDO
    # Buat pembungkus untuk untuk inputan saldo
    saldo_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    # Tampilkan pembungkus untuk untuk inputan saldo
    saldo_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    saldo_Label = ctk.CTkLabel(saldo_wrap, text="Saldo Awal Rp.") # Label Inputan
    # Tampilkan keterangan tentang input
    saldo_Label.pack(side='left', padx=10, pady=5)
    
    # buat inputan
    saldo_input = ctk.CTkEntry(saldo_wrap, corner_radius=10, placeholder_text="50000", width=300, height=40) # Inputan
    # Tampilkan inputan
    saldo_input.pack(side='right', padx=10, pady=5)
    
    # Bungkus semua inputan kedalam 1 variabel penampung bertipe dict
    inputs = {
        'nama': nama_input,
        'usernama': usernama_input,
        'email' : email_input,
        'no_hp': noHp_input,
        'anggota': anggota_var,
        'lahir': lahir_input,
        'alamat': alamat_input,
        'pin': pin_input,
        'kpin': kpin_input,
        'saldo' : saldo_input
    }
    
    ######################################################
    ###################################################### BODY
    
    

    ###################################################### FOOTER
    ###################################################### 
    
    # Buat tombol batal
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol batal di klik maka akan batal ke fungsi lambda yang mengeksekusi fungsi kembali ke home
    batalBtn = ctk.CTkButton(frame['footer'], height=50,text="Batal", fg_color='orange', command=lambda : kembali_ke_home(app, frame))
    # Tampilkan tombol
    batalBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    # Buat tombol daftar
    # parameter command adalah untuk menjalankan perintah ketika di klik
    # lambda merupakan fungsi sederhana untuk keperluan sekali saja
    # ketika tombol daftar di klik maka akan daftar ke fungsi lambda yang mengeksekusi fungsi handle daftar
    daftarBtn = ctk.CTkButton(frame['footer'], height=50,text="Lanjut Daftar", fg_color='blue', command=lambda : handle_daftar(app, frame, inputs))
    # Tampilkan tombol
    daftarBtn.pack(side="left", fill='x', expand=True, padx=10)
    ###################################################### 
    ###################################################### FOOTER
    
    
       


    