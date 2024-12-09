# Import library eksternal yaitu library TKinter atau CustomTKinter , time dan hashlib 
 
import time

# Import module internal
from ..pendataan.user import cek_user_kartu, cek_pin

    
component = ['canvas']

# Fungsi untuk menghandel tombol masuk dan melanjutkan proses masuk
def handle_masuk(app, canvas, inputs):
    canvas.delete(component[0])
    # Tampung inputan kedalam variabel tersendiri
    user_input = inputs['usernama'].get()
    pin_input = inputs['pin'].get()
    
    # cek apakah user telah terdafatr
    user = cek_user_kartu(user_input)
    
    # Jika user tidak kosong dalam kata lain telah terdaftar
    if type(user) != type(False):
        # maka cek pin user tesebut apakah sama denga pin yang ada di data
        sesi = cek_pin(pin_input, user)
        # Jika benar maka sesi akan mengembalika nilai true
        
        if not sesi['auth']:
            # Jika sesi auth nya tidak berhasil maka akan menampilkan pesan gagal masuk
            # gagal = ctk.CTkLabel(frame['body'], text="GAGAL MASUK", fg_color="orange")
            # gagal.pack(side='top', fill='x', expand=True)
            status = canvas.create_text(
                301.0,
                480.0,
                anchor="nw",
                text="GAGAL MASUK",
                fill="red",
                font=("Poppins Medium", 16 * -1)
            )
            component.insert(0,status)
        else:
            # Jika sesi auth nya berhasil maka akan menampilkan pesan berhasil
            # sukses = ctk.CTkLabel(frame['body'], text="BERHASIL MASUk", fg_color="green")
            # sukses.pack(side='top', fill='x', expand=True)
            status = canvas.create_text(
                301.0,
                480.0,
                anchor="nw",
                text="SUKSES MASUK",
                fill="green",
                font=("Poppins Medium", 16 * -1)
            )
            component.insert(0,status)
            # Jeda program selama 1 detik
            time.sleep(1)
            # Lanjutkan ke dashboard
            from ..menu.main import dashboard
            dashboard(app, sesi)
    
    else:

        status = canvas.create_text(
            301.0,
            480.0,
            anchor="nw",
            text="GAGAL MASUK",
            fill="red",
            font=("Poppins Medium", 16 * -1)
        )
        component.insert(0,status)
        # Jika user tidak ada makan akan menampilkan pesan tidak ditemukan
        # gagal = ctk.CTkLabel(frame['body'], text="USER ATAU NOMOR KARTU TIDAK DITEMUKAN", fg_color="yellow", text_color='black')
        # gagal.pack(side='top', fill='x', expand=True)
        
    # Hapus pesan peringatan atau sukses sebelumnya ketika pesan baru dimunculkan.
    # Sehingga akan tampil 1 peringatan ketika 1 aksi 
    # banyak_komponen = len(frame['body'].winfo_children())
    # if banyak_komponen > 3:
    #     child = frame['body'].winfo_children()[banyak_komponen - 2]
    #     child.destroy()