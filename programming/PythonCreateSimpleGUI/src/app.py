import os
from math import *
import tkinter as tk
from PIL import Image, ImageTk


# defining functions
# ------------------------------------------------------------------------
# IMPORTANT event have to initialized with None in order
# to be compatible with both <Return> and button execution, respectively.
def compute(event=None):
    userIn = entry.get()
    if len(userIn) > 0:
        res.configure(text="{}".format(str(eval(userIn))))


# set parameter and path to logo
# ------------------------------------------------------------------------
# define window size
H, W = 480, 480
# define background color
colBG = "#FFFFFF"
# define title as app description
strTitle = (
    "This app interprets mathematical expressions \n"
    + "(using Package math) and calculates \n"
    + "the numerical result."
)

# little hack/trick to change dir
pathDirImg = os.getcwd().replace("src", "img")
pathImg = os.path.join(pathDirImg, "logoBS.png")

# load logo image
logo = Image.open(pathImg)
logo = logo.resize((100, 100))


# create GUI app
# ------------------------------------------------------------------------
# define window
objWin = tk.Tk()
objWin.geometry("{}x{}+{}+{}".format(W, H, 0, 0))

# define frame layout and including BG
objFrame = tk.Frame(
    objWin,
    width=W,
    height=H,
    bg=colBG,
)
objFrame.grid(columnspan=3, rowspan=6, row=0)

# set logo
logo = ImageTk.PhotoImage(logo)
lblLogo = tk.Label(image=logo, borderwidth=0)
lblLogo.grid(column=1, row=0)

# define and place description
lblDesc = tk.Label(
    objWin,
    text=strTitle,
    font=("Ubuntu", 12),
    justify="center",
    bg=colBG,
)
lblDesc.grid(column=0, row=1, columnspan=3)

# define and place label for input
lblInput = tk.Label(
    objWin,
    text="Enter Your Expression: ",
    bg=colBG,
    fg="#3071db",
)
lblInput.grid(column=0, row=2, columnspan=3)

# define and place input field
entry = tk.Entry(objWin, width=48)
entry.bind("<Return>", compute)
entry.grid(column=0, row=3, columnspan=3)

# define and place result field
res = tk.Label(objWin, bg=colBG)
res.grid(column=0, row=4, columnspan=3)

# define and place execution button
btmE = tk.Button(objWin, text="Eval", command=compute)
btmE.grid(column=0, row=5)

# define and place quit button
btmQ = tk.Button(objWin, text="Quit", command=objWin.destroy)
btmQ.grid(column=2, row=5)

# run main loop
objWin.mainloop()
