
# ---------------------------------IMPORTS------------------------------------ #
from tkinter import *
import pandas as pd
from tkinter import messagebox

# ---------------------------------CONSTANTS---------------------------------- #
BG_COLOR = "#B1DDC6"
WORD_FONT = ('Arial', 60, 'bold')
CONTEXT_FONT = ('Arial', 40, 'italic')
FLIP_WAIT_SEC = 3
timer = None
english_word = None
words_to_learn = pd.DataFrame(columns=['French', 'English'])

# card_back_img = PhotoImage('./images/card_back.png')


# Image to button!
# my_image = PhotoImage(file="path/to/image_file.png")
# button = Button(image=my_image, highlightthickness=0)

# -------------------------------GET WORD------------------------------------- #

try:
    data = pd.read_csv('./data/words_to_learn.csv')
    print(data.head())
except FileNotFoundError:
    data = pd.read_csv('./data/french_words.csv')


def show_new_card():
    global context_text, word_text, timer, words_to_learn, english_word

    if len(data) == 0:
        messagebox.showinfo(title="No more words!", message="There are no more words to learn! Program will now exit.")
        window.destroy()
        return

    random_word = data.sample(n=1)
    english_word = random_word.iloc[0]["English"]
    french_word = random_word.iloc[0]["French"]

    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(context_text, text="French", fill='#000000')
    canvas.itemconfig(word_text, text=french_word, fill='#000000')

    flip_wait_ms = 1000 * FLIP_WAIT_SEC
    timer = window.after(flip_wait_ms, flip_card)


def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(context_text, text="English", fill='#ffffff')
    canvas.itemconfig(word_text, text=english_word, fill='#ffffff')
    window.after_cancel(timer)


def is_known():
    global data, english_word

    data = data[data.English != english_word]
    data.to_csv('./data/words_to_learn.csv', index=False)
    show_new_card()


# -----------------------------------UI--------------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(bg=BG_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
card_img = canvas.create_image(400, 263, image=card_front_img)
context_text = canvas.create_text(400, 150, text='', font=CONTEXT_FONT)
word_text = canvas.create_text(400, 263, text='', font=WORD_FONT, tag='word')
canvas.grid(column=0, row=0, columnspan=2)
show_new_card()

wrong_button_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=show_new_card)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)


window.mainloop()







