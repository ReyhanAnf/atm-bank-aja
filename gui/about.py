from tkinter import Canvas, PhotoImage, Button

from .setelan import akses_aset_media

LOC = 'about'

def about(app):
    app.geometry("687x549")

    canvas = Canvas(
        app,
        bg = "#EBF3FF",
        height = 549,
        width = 687,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=akses_aset_media("image_1.png", LOC))
    image_1 = canvas.create_image(
        343.0,
        42.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=akses_aset_media("image_2.png", LOC))
    image_2 = canvas.create_image(
        88.0,
        47.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=akses_aset_media("image_3.png", LOC))
    image_3 = canvas.create_image(
        344.0,
        137.0,
        image=image_image_3
    )

    canvas.create_text(
        181.0,
        125.0,
        anchor="nw",
        text="Selamat Datang Di Bank Bangun Mimpi",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    canvas.create_text(
        578.0,
        11.0,
        anchor="nw",
        text="About",
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )

    canvas.create_text(
        304.0,
        180.0,
        anchor="nw",
        text="About",
        fill="#000000",
        font=("Poppins SemiBold", 28 * -1)
    )

    canvas.create_text(
        52.0,
        222.0,
        anchor="nw",
        text="Developer",
        fill="#000000",
        font=("Poppins SemiBold", 20 * -1)
    )

    canvas.create_text(
        52.0,
        263.0,
        anchor="nw",
        text="Reyhan Andrea Firdaus",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    canvas.create_text(
        595.0,
        262.0,
        anchor="nw",
        text="19240133",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    canvas.create_text(
        51.0,
        299.0,
        anchor="nw",
        text="Dina Khoerunnisa",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    canvas.create_text(
        595.0,
        334.0,
        anchor="nw",
        text="19240133",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    canvas.create_text(
        52.0,
        334.0,
        anchor="nw",
        text="Gina",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    canvas.create_text(
        595.0,
        370.0,
        anchor="nw",
        text="19240133",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    canvas.create_text(
        52.0,
        370.0,
        anchor="nw",
        text="Ineu",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    canvas.create_text(
        594.0,
        406.0,
        anchor="nw",
        text="19240133",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    canvas.create_text(
        53.0,
        406.0,
        anchor="nw",
        text="Nazwa",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    canvas.create_text(
        596.0,
        299.0,
        anchor="nw",
        text="19240133",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    from .awal.main import home
    keluar_img = PhotoImage(
        file=akses_aset_media("button_1.png", LOC))
    keluar_btn = Button(
        image=keluar_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: home(app),
        relief="flat"
    )
    keluar_btn.place(
        x=36.0,
        y=442.0,
        width=281.0,
        height=90.0
    )
    app.resizable(False, False)
    app.mainloop()