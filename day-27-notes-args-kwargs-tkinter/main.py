# Tkinter, *args, **kwargs, and Creating GUI Programs
# Packer documentation https://docs.python.org/3/library/tkinter.html#the-packer

from tkinter import *


def button_clicked():
    user_input = input_field.get()
    my_label.config(text=user_input)


# Window
window = Tk()
window.title("Baby's First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # pads entire window, can use for individual items

# Label
my_label = Label(text="I am a Label lalalala!", font=("Calibri", 24, "normal"))
# my_label["text"] = "New Text" # OR below
my_label.config(text="New Text", padx=50, pady=50)
my_label.grid(column=0, row=0)  # screen placement geometry system


# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# Entry
input_field = Entry(width=10)
input_field.grid(column=3, row=2)


# Keep window open until program's done
window.mainloop() # keeps window on screen, listens for input. must be at the end of script

# # ------------------

# # Pack, Place, Grid
# pack starts at the top and places everything below by default
# pack alternatively places things from 'side' keyword value
# easy but difficult for precision

# place puts an item directly at a coordinate (x=, y=)
# place can be difficult with many items

# grid creates a grid of rows and columns
# cannot use grid and pack together



