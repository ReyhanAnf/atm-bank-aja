# Import library eksternal yaitu library TKinter atau CustomTKinter
import customtkinter as ctk

# Import module internal untuk menu
from ...pendataan.transaksi import data_transaksi
from ...setelan import reset_frame
from ..proses import kembali_ke_home

# Buat fungsi Riwayat Transaksi untuk menampilkan transaksi dalam bentuk tabel
def riwayat_transaksi(app, frame, sesi):
    # Argumen sesi membawa nilai bertipe dict yang berisi 'auth' sebagai penanda bahwa user telah melakukan login 
    # dan 'data' membawa informasi data user yang telah login
    # sesi['auth'] bertipe boolean
    # sesi['data'] beripe dict
    auth = sesi['auth']
    user = sesi['data']
    
    # bersihkan frame
    reset_frame(frame['header'])
    reset_frame(frame['body'])
    
    # ketika user telah login makan jalankan program ini terus sebelum user memilih pilihan keluar
    if auth == True:
        ################################################## HEADER
        #########################################
        
        # Buat Judul dengan Navigasi nya dan tampilkan di paling atas
        title = ctk.CTkButton(frame['header'], text="BANK AJA - RIWAYAT TRANSAKSI", font=('Arial', 28, 'bold'))
        title.pack(side="top")
        
        # Buat sapaan kepada user sesuai nama user yang telah melakukan autentikasi
        halo = ctk.CTkLabel(frame['header'], text=f"Hai, {user['nama']}!", fg_color="white", text_color='black')
        halo.pack(side='top', fill='x', expand=True, ipadx=10, ipady=10, pady=10)
        
        ######################################### 
        ################################################## HEADER
        
        
        
        ################################################## BODY
        #########################################
        
        # Ambil data transaksi dari module pendataan
        df = data_transaksi()
        
        # Sorting data
        # Ambil data ketika data tersebut mengandung user ini (user yang telah login)
        # Baik itu sebagai penerima atau pengirim dalam transaksi
        # Jadi data akan menampilkan data yang pengirim atau penerimanya user ini saja
        df = df[(df['pengirim'] == user['usernama']) | (df['penerima'] == user['usernama'])].reset_index(drop=True)

        # Ambil jumlah baris dan kolom
        n_rows = df.shape[0] 
        n_cols = df.shape[1] 
        
        # Ambil data list dari kolom yang ada pada database atau data
        column_names = df.columns

        # Buat tampilan Frame yang bisa di scroll untuk diisi oleh tabel data
        scrollable_frame = ctk.CTkScrollableFrame(frame['body'], width=700, height=500, corner_radius=20, label_anchor='center')
        scrollable_frame.pack(side='top', fill='both', expand=True, ipadx=5, ipady=5)
        
        # Setiap kolom dicetak didalam satu baris yang sama
        for j in range(n_cols):
            kol = ctk.CTkLabel(scrollable_frame, text=column_names[j], width=80, text_color='green')
            kol.grid(row=0, column=j, ipadx=5, ipady=2)

        # Buat perulangan sesuai jumlah baris untuk menampilkan isi data
        for i in range(n_rows):
            # Setiap nilai dalam satu kolom akan dicetak pada baris ke-i sampai i sama dengan jumlah baris
            # Setiap kolom dicetak dalam satu baris yang sama
            for j in range(n_cols):
                # Tampilkan baris dimulai dari baris ke 1 (bukan ke 0, karena ke 0 adalah untuk kolom header)
                row = ctk.CTkLabel(scrollable_frame, text=df[column_names[j]][i], width=80, anchor='e')
                row.grid(row=i+1, column=j, ipadx=10, ipady=5, sticky='ew')
                
        ######################################### 
        ################################################## BODY
        
        
        
        ################################################## FOOTER
        ######################################### 
        
        # Buat tombol kembali dan tampilkan
        # Akan menjalankan fungsi kembali_ke_menu
        reset_frame(frame['footer'])
        from ..proses import kembali_ke_menu
        kembaliBtn = ctk.CTkButton(frame['footer'], height=50, text="Kembali", fg_color='orange', text_color='black', command=lambda : kembali_ke_menu(app, frame, sesi))
        kembaliBtn.pack(side="left", fill='x', expand=True, padx=10)
        
        ######################################### 
        ################################################## FOOTER
    else:
        # Jika user belum atau tidak pernah autentikasi maka kembalikan ke home
        kembali_ke_home(app, frame)

