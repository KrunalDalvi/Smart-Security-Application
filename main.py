import tkinter as tk
import os
import tkinter.font as font
from tkinter import *
from PIL import Image, ImageTk # PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities. 
from motion import noise
from rect_noise import rect_noise
from track_people import track_people
from record import record
from login_page import login_page

class main_page:
    pass

window = tk.Tk()
window.title("God's Eye")
window.geometry("1280x800")

# The PhotoImage class is used to display images in labels, buttons, canvases, and text widgets, which is present in tkinter package.
# This function takes a file path as an argument and returns the image object.
# We can place the geometry manager that allows users to put the widget anywhere on the screen by providing x & y coordinates. 
bg = ImageTk.PhotoImage(file="Images/main_bg.png")
label1 = Label(window, image = bg)
label1.place(x=0,y=0,relwidth=1,relheight=1)

# Wants to close initial window and open new one
def login_redirect():
    window.destroy()   
    root = Tk()
    obj2 = login_page(root)
    root.mainloop()

# ----------------- Image on Button -------------------#
# open() opens and identifies the given image file 
# resize() Returns a resized copy of this image
# Image.ANTIALIAS is a kind of a filter
btn1_image = Image.open('icons/security-camera.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn3_image = Image.open('icons/incognito.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)


# --------------- Button -------------------#    
btn_font = font.Font(size=20)
btn1 = tk.Button(window, text=' Motion Detection ', height=55, width=500, bg='#FECE00', fg='Black', command=noise, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.place(x=750,y=100)

btn2 = tk.Button(window, text='Motion in Specified Area ', height=55, width=500, bg='#FECE00', fg='Black', command=rect_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.place(x=750, y=200)

btn3 = tk.Button(window, text='Track Visitor', height=55, width=500, bg='#FECE00', fg='Black', command=track_people, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.place(x=750, y=300)

btn4 = tk.Button(window, text='Record', height=55, width=500, bg='#FECE00', fg='Black', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.place(x=750, y=400)

btn5 = tk.Button(window, text="Logout", height=55, width=500, bg='#FECE00', fg='Black', command=login_redirect, image=btn5_image, compound='left')
btn5['font'] = btn_font
btn5.place(x=750, y=500)
    
window.mainloop()


