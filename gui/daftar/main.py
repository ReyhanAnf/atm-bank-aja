import customtkinter as ctk

from ..setelan import reset_frame
from .handler_tombol import kembali_ke_home, handle_daftar

def formulir_daftar(app, frame):
    app.title("BANK AJA - GUI")
    
    reset_frame(frame['header'])
    reset_frame(frame['body'])
    reset_frame(frame['footer'])
    ###################################################### HEADER
    
    
    title = ctk.CTkButton(frame['header'], text="BANK AJA - DAFTAR", font=('Arial', 28, 'bold'))
    title.pack(side="top")
    ###################################################### HEADER
    
    
    
    ###################################################### BODY
    ######################################################
    
    ########### INPUT USER
    # Buat pembungkus untuk untuk inputan nama
    nama_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    nama_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    nama_Label = ctk.CTkLabel(nama_wrap, text="Nama Lengkap") # Label Inputan
    nama_Label.pack(side='left', padx=10, pady=5)
    
    # buat inputan
    nama_input = ctk.CTkEntry(nama_wrap, corner_radius=10, placeholder_text="Nama Lengkap", width=300, height=40) # Inputan
    nama_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT USERNAMA
    # Buat pembungkus untuk inputan usernama
    usernama_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    usernama_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    usernamaLabel = ctk.CTkLabel(usernama_wrap, text="Usernama") # Label
    usernamaLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    usernama_input = ctk.CTkEntry(usernama_wrap, corner_radius=10, placeholder_text="usernama", width=300, height=40) # Inputan
    usernama_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT EMAIL
    # Buat pembungkus untuk inputan email
    email_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    email_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    emailLabel = ctk.CTkLabel(email_wrap, text="Email") # Label
    emailLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    email_input = ctk.CTkEntry(email_wrap, corner_radius=10, placeholder_text="email", width=300, height=40) # Inputan
    email_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT No HP
    # Buat pembungkus untuk inputan nomor hp
    noHp_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    noHp_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    noHpLabel = ctk.CTkLabel(noHp_wrap, text="Nomor HP") # Label
    noHpLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    noHp_input = ctk.CTkEntry(noHp_wrap, corner_radius=10, placeholder_text="noHp", width=300, height=40) # Inputan
    noHp_input.pack(side='right', padx=10, pady=5)
    
    
    ############# INPUT ANGGOTA
    # Buat pembungkus untuk inoutan anggota
    anggota_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    anggota_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input atau Label
    anggotaLabel = ctk.CTkLabel(anggota_wrap, text="Anggota") # Label
    anggotaLabel.pack(side='left', padx=10, pady=5)
    
    # Buat Inputan
    anggota_var = ctk.StringVar(value='gold') # Variabel penampung
    a_silver = ctk.CTkRadioButton(anggota_wrap, text="Silver", value='silver', variable=anggota_var) # Inputan
    a_silver.pack(side='right', padx=10, pady=5)
    a_gold = ctk.CTkRadioButton(anggota_wrap, text="Gold", value='gold', variable=anggota_var) # Inputan
    a_gold.pack(side='right', padx=10, pady=5)
    a_platinum = ctk.CTkRadioButton(anggota_wrap, text="Platinum", value='platinum', variable=anggota_var) # Inputan
    a_platinum.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT TANGGAL LAHIR
    # Buat pembungkus untuk inputan tanggal lahir
    lahir_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    lahir_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    lahirLabel = ctk.CTkLabel(lahir_wrap, text="Tanggal Lahir") # Label
    lahirLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    lahir_input = ctk.CTkEntry(lahir_wrap, corner_radius=10, placeholder_text="01/01/2000", width=300, height=40) # Inputan
    lahir_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT ALAMAT
    # Buat pembungkus untuk inputan alamat
    alamat_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    alamat_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    alamatLabel = ctk.CTkLabel(alamat_wrap, text="Alamat") # Label
    alamatLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    alamat_input = ctk.CTkTextbox(alamat_wrap, corner_radius=10, width=300, height=40) # Inputan
    alamat_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT PIN
    # Buat pembungkus untuk inputan pin
    pin_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    pin_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    pinLabel = ctk.CTkLabel(pin_wrap, text="PIN") # Label
    pinLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    pin_input = ctk.CTkEntry(pin_wrap, corner_radius=10, placeholder_text="***", width=300, height=40) # Inputan
    pin_input.pack(side='right', padx=10, pady=5)
    
    
    ######## #INPUT KONFIRMASI PIN
    # Buat pembungkus untuk inputan pin
    kpin_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    kpin_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    kpinLabel = ctk.CTkLabel(kpin_wrap, text="KONFIRMASI PIN") # Label
    kpinLabel.pack(side='left', padx=10, pady=5)
    
    # Buat inputan
    kpin_input = ctk.CTkEntry(kpin_wrap, corner_radius=10, placeholder_text="***", width=300, height=40) # Inputan
    kpin_input.pack(side='right', padx=10, pady=5)
    
    
    ########### INPUT SALDO
    # Buat pembungkus untuk untuk inputan saldo
    saldo_wrap = ctk.CTkFrame(frame['body']) # Pembungkus
    saldo_wrap.pack(side='top', padx=10, pady=5, fill='x', expand=True)
    
    # Buat keterangan tentang input
    saldo_Label = ctk.CTkLabel(saldo_wrap, text="Saldo Awal Rp.") # Label Inputan
    saldo_Label.pack(side='left', padx=10, pady=5)
    
    # buat inputan
    saldo_input = ctk.CTkEntry(saldo_wrap, corner_radius=10, placeholder_text="50000", width=300, height=40) # Inputan
    saldo_input.pack(side='right', padx=10, pady=5)
    
    
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
    batalBtn = ctk.CTkButton(frame['footer'], height=50,text="Batal", fg_color='orange', command=lambda : kembali_ke_home(app, frame))
    batalBtn.pack(side="left", fill='x', expand=True, padx=10)
    
    
    daftarBtn = ctk.CTkButton(frame['footer'], height=50,text="Lanjut Daftar", fg_color='blue', command=lambda : handle_daftar(app, frame, inputs))
    daftarBtn.pack(side="left", fill='x', expand=True, padx=10)
    ###################################################### 
    ###################################################### FOOTER
    
    
       


    