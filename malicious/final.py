from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Desktop Assistant")
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth()/2 - 982/2)
positionDown = int(window.winfo_screenheight()/2 - 710/2)
window.geometry(f"982x629+{positionRight}+{positionDown}")
window.iconbitmap('images/favicon.ico')
# window.wm_attributes('-alpha', 0.7)
window.configure(bg="#fff")
canvas = Canvas(window, bg="#fff", height=629, width=982,
                bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)


'''Final Page'''
img = ImageTk.PhotoImage(file="images/logo1.png")
canvas.create_image(50, 40, image=img)

wizard = ImageTk.PhotoImage(file="images/wizard.png")
canvas.create_image(500, 220, image=wizard, tag='wizard')

Rectangle_box = ImageTk.PhotoImage(file="images/Rectangle 9.png")
canvas.create_image(500, 490, image=Rectangle_box, tag='Rectangle_box')


ball_1 = ImageTk.PhotoImage(file="images/ball 1.png")
canvas.create_image(720, 200, image=ball_1, tag='ball_1')

ball_2 = ImageTk.PhotoImage(file="images/ball 2.png")
canvas.create_image(60, 350, image=ball_2, tag='ball_2')

ball_3 = ImageTk.PhotoImage(file="images/ball 3.png")
canvas.create_image(260, 170, image=ball_3, tag='ball_3')

ball_4 = ImageTk.PhotoImage(file="images/ball 4.png")
canvas.create_image(790, 330, image=ball_4, tag='ball_4')

ball_5 = ImageTk.PhotoImage(file="images/ball 5.png")
canvas.create_image(950, 150, image=ball_5, tag='ball_5')

ball_6 = ImageTk.PhotoImage(file="images/ball 6.png")
canvas.create_image(200, 350, image=ball_6, tag='ball_6')

window.mainloop()
