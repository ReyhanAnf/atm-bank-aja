

def kembali_ke_menu(app, frame, sesi):
    from .main import dashboard
    dashboard(app, frame, sesi)
    
    
def kembali_ke_home(app, frame):
    from ..awal.main import home
    home(app, frame)