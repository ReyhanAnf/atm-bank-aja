import customtkinter as ctk

from ...pendataan.transaksi import konfirmasi_transaksi
from .proses import mutasi

def bayar_handle(app, frame, inputs,sesi):
    
    auth = sesi['auth']
    user = sesi['data']
    
    if auth == True:
        bayar_input = inputs['bayar'].get()
        tujuan_input = inputs['tujuan'].get()
        nominal_input = inputs['nominal'].get()

        
        nominal = int(nominal_input)
        
        if nominal >= 1000:
            # KETERANGAN SUKSES
            sukses = ctk.CTkLabel(frame['body'], text="PROSES MENGIRIM...", fg_color='green') # Label Inputan
            sukses.pack(side='top', fill='x', expand=True)
            
            # KETERANGAN SUKSES
            progressbar = ctk.CTkProgressBar(frame['body'], orientation="horizontal", mode='indeterminate', determinate_speed=5, indeterminate_speed=1)
            progressbar.start()
            
            progressbar.pack(pady=20)
            
            metode = 'bayar'
            admin = 2500
            total = nominal + admin
            
            data = {
                'pengirim': user,
                'penerima': f"{bayar_input} - {tujuan_input}",
                'metode': metode,
                'admin' : admin,
                'status' : 'menunggu',
                'jumlah': nominal,
                'total' : total
            }
            
            konfirmasi_transaksi(app, frame, sesi, data, mutasi)
            
        else:
            ## Kurang dari Rp 10.000
            # KETERANGAN GAGAL
            gagal = ctk.CTkLabel(frame['body'], text="NOMINAL MINIMAL RP 1000", fg_color='orange') # Label Inputan
            gagal.pack(side='top', fill='x', expand=True)

        
        banyak_komponen = len(frame['body'].winfo_children())
        if banyak_komponen > 11:
            child = frame['body'].winfo_children()[banyak_komponen - 2]
            child.destroy()
            
            
                
        ################################################## FOOTER
        ######################################### 
        
        from .main import transfer
        koreksiBtn = ctk.CTkButton(frame['footer'], height=50,text="Koreksi", fg_color='orange', text_color='black', command=lambda : transfer(app, frame, sesi))
        koreksiBtn.pack(side="left", fill='x', expand=True, padx=10)
        
        
        ######################################### 
        ################################################## FOOTER