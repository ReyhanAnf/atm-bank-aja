import customtkinter as ctk
from ...pendataan.transaksi import data_transaksi

from ...setelan import reset_frame
from ...daftar.proses import kartu_atm
from ...pendataan.user import cek_user_kartu

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
        
        title = ctk.CTkButton(frame['header'], text="BANK AJA - RIWAYAT TRANSAKSI", font=('Arial', 28, 'bold'))
        title.pack(side="top")
        
        halo = ctk.CTkLabel(frame['header'], text=f"Hai, {user['nama']}!", fg_color="white", text_color='black')
        halo.pack(side='top', fill='x', expand=True, ipadx=10, ipady=10, pady=10)
        
        ######################################### 
        ################################################## HEADER
        
        
        
        ################################################## BODY
        #########################################
        df = data_transaksi()
        df = df[(df['pengirim'] == user['usernama']) | (df['penerima'] == user['usernama'])].reset_index(drop=True)
    
        n_rows = df.shape[0] 
        n_cols = df.shape[1] 
        
        # Extracting columns from the data and 
        # creating text widget with some 
        # background color 
        column_names = df.columns

        
        scrollable_frame = ctk.CTkScrollableFrame(frame['body'], width=700, height=500, corner_radius=20, label_anchor='center')
        scrollable_frame.pack(side='top', fill='both', expand=True, ipadx=5, ipady=5)
        
        
        for j in range(n_cols):
            kol = ctk.CTkLabel(scrollable_frame, text=column_names[j], width=80, text_color='green')
            kol.grid(row=0, column=j, ipadx=5, ipady=2)

        for i in range(n_rows):
            for j in range(n_cols):
                row = ctk.CTkLabel(scrollable_frame, text=df[column_names[j]][i], width=80, anchor='e')
                row.grid(row=i+1, column=j, ipadx=10, ipady=5, sticky='ew')
        ######################################### 
        ################################################## BODY
        
        
        
        ################################################## FOOTER
        ######################################### 
        
        reset_frame(frame['footer'])
        from ..proses import kembali_ke_menu
        kembaliBtn = ctk.CTkButton(frame['footer'], height=50, text="Kembali", fg_color='orange', text_color='black', command=lambda : kembali_ke_menu(app, frame, sesi))
        kembaliBtn.pack(side="left", fill='x', expand=True, padx=10)
        
        ######################################### 
        ################################################## FOOTER
    else:
        pass

