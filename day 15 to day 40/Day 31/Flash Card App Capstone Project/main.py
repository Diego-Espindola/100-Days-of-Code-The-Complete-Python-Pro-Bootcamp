from tkinter import *
import pandas as pd
import random as r
from pathlib import Path
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
RANDOM_WORD = {}
DELAY_FUNCTION = None

# Reading the csv file
if Path("./data/words_to_learn.csv").exists():
    df_words = pd.read_csv('./data/words_to_learn.csv')
    if df_words.empty:
        messagebox.showinfo("End", "There is no more data in the words to learn.\nCongratulations!!!"
                                   "\nIf you want to repeat it, please remove the words_to_learn.csv file")
        exit()
else:
    df_words = pd.read_csv('./data/french_words.csv')
WORDS = df_words.to_dict(orient="records")
COLUMNS = df_words.columns.tolist()


def next_card():
    global RANDOM_WORD, DELAY_FUNCTION
    RANDOM_WORD = r.choice(WORDS)
    canvas.itemconfig(image_card, image=img_front)
    canvas.itemconfig(language, text=COLUMNS[0], fill="black")
    canvas.itemconfig(word_label, text=RANDOM_WORD[COLUMNS[0]], fill="black")
    DELAY_FUNCTION = window.after(3000, back_card)


def back_card():
    canvas.itemconfig(image_card, image=img_back)
    canvas.itemconfig(language, text=COLUMNS[1], fill="white")
    canvas.itemconfig(word_label, text=RANDOM_WORD[COLUMNS[1]], fill="white")


def known_word():
    window.after_cancel(DELAY_FUNCTION)
    if len(WORDS) == 0:
        messagebox.showinfo("End", "There is no more data in the words to learn"
                                   "\nCongratulations!!!")
    else:
        WORDS.remove(RANDOM_WORD)
        df = pd.DataFrame(WORDS)
        df.to_csv("./data/words_to_learn.csv", index=False)
        next_card()


def unknown_word():
    window.after_cancel(DELAY_FUNCTION)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
img_front = PhotoImage(file="./images/card_front.png")
img_back = PhotoImage(file="./images/card_back.png")
image_card = canvas.create_image(400, 263, image=img_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
next_card()

wrong_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=unknown_word)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
know_button = Button(image=right_image, highlightthickness=0, command=known_word)
know_button.grid(column=1, row=1)

window.mainloop()
