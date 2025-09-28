from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

word_dict = {}


def new_word_wrong():
    global flip
    window.after_cancel(flip)
    try:
        display_word = random.choice(Vocab_dict)
    except NameError:
        canvas.create_text(380, 150, text="You've learnt all the words!", font=("Arial", 40, "italic"))
    else:
        word_dict.update(display_word)
        new_display = display_word["German"]
        canvas.itemconfig(word_text, text=f"{new_display}", fill="black")
        canvas.itemconfig(title_text, text="German", fill="black")
        canvas.itemconfig(card_display, image=card_front)
        flip = window.after(3000, english_card)


def new_word_right():
    global flip
    window.after_cancel(flip)
    try:
        display_word = random.choice(Vocab_dict)
        word_dict.update(display_word)
        new_display = display_word["German"]
        canvas.itemconfig(word_text, text=f"{new_display}", fill="black")
        canvas.itemconfig(title_text, text="German", fill="black")
        canvas.itemconfig(card_display, image=card_front)
        flip = window.after(3000, english_card)

        Vocab_dict.remove(display_word)
        vocab_df = pd.DataFrame(Vocab_dict)
        csv_file = vocab_df.to_csv("words_to_learn.csv", index=False)
    except IndexError:
        print("You've learnt all the words!")
        window.quit()


def english_card():
    english_display = word_dict["English"]
    canvas.itemconfig(card_display, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{english_display}", fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, width=900, height=626)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_display = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(380, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(380, 276, text="", font=("Arial", 60, "bold"))

cross = PhotoImage(file="images/wrong.png")
tick = PhotoImage(file="images/right.png")

card_back = PhotoImage(file="images/card_back.png")

flip = window.after(3000, english_card)

try:
    data = pd.read_csv("words_to_learn.csv")
    Vocab_list = pd.DataFrame(data)
except FileNotFoundError:
    data = pd.read_csv("data/german_words.csv")
    Vocab_list = pd.DataFrame(data)
except pd.errors.EmptyDataError:
    print("You've learnt all the words!")
else:
    Vocab_dict = Vocab_list.to_dict(orient="records")

wrong_button = Button(image=cross, highlightthickness=0, command=new_word_wrong)
right_button = Button(image=tick, highlightthickness=0, command=new_word_right)

canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

new_word_wrong()

window.mainloop()