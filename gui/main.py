# Python program to create a basic GUI 
# application using the customtkinter module

import customtkinter as ctk
import tkinter as tk

from .awal import main as awal

# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("System") 

# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green") 

appWidth, appHeight = 700, 600

def main():
    app = ctk.CTk()
    app.resizable(width=True, height=True)
    app.geometry(f"{appWidth}x{appHeight}")
    
    frame_header = ctk.CTkFrame(app, corner_radius=10, fg_color="transparent")
    frame_header.pack(side="top", fill="x", expand=True)
    
    frame_body = ctk.CTkFrame(app, corner_radius=10, fg_color="transparent")
    frame_body.pack(side="top", fill="both", expand=True)
    
    frame_footer = ctk.CTkFrame(app, corner_radius=10, fg_color="transparent")
    frame_footer.pack(side="bottom", fill="x", expand=True)
    
    frame = {
        'header': frame_header,
        'body': frame_body,
        'footer': frame_footer
    }
    
    awal.home(app, frame)
    app.mainloop()
        
