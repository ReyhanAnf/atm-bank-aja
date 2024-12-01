
# Fungsi untuk kembali ke menu
def kembali_ke_menu(app, frame, sesi):
    from .main import dashboard
    dashboard(app, frame, sesi)
    
    
# Fungsi untuk kembali ke home
def kembali_ke_home(app, frame):
    from ..awal.main import home
    home(app, frame)