from pathlib import Path
## Fungsi ini berfungsi untuk mereset frame


def reset_frame(frame):
    for child in frame.winfo_children():
        child.destroy()
        
 
        
def relative_to_assets(path: str, loc) -> Path:
    PATH = Path(__file__).parent
    ASSETS_PATH = PATH / Path(PATH.joinpath(r"assets").joinpath(loc))
    return ASSETS_PATH / Path(path)