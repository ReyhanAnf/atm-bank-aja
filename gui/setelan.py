

def reset_frame(frame):
    for child in frame.winfo_children():
        child.destroy()
        
