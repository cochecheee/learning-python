from tkinter import *
import pandas
import random

# ------------------------------------------ CONSTANTS
BACKGROUND_COLOUR = "#B1DDC6"

#  ------------------------------------------ READ CSV FILE
french_csv = pandas.read_csv("data/french_words.csv")
# ‘records’ : list like [{column -> value}, … , {column -> value}]
french_dict = french_csv.to_dict(orient="records")
current_card = {}

#  ------------------------------------------ MAIN FUNCTIONS
def next_card():
    # choose 1 word and show it on front_card
    global current_card
    global flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(french_dict)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer = window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back)

def is_known():
    french_dict.remove(current_card)
    next_card()

# ------------------------------------------ SET UP UI
window = Tk()
window.title("Flash card")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOUR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
card_front = PhotoImage(file="./image/card_front.png")
card_back = PhotoImage(file="./image/card_back.png")
card_background = canvas.create_image(400,263,image=card_front)
card_title = canvas.create_text(400,150,text="Title",font=("Arial",30,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Arial",50,"bold"))

canvas.config(bg=BACKGROUND_COLOUR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=3)

# # create 2 button 
right_click = PhotoImage(file="./image/right.png")
right_btn = Button(image=right_click,command=is_known)
right_btn.grid(row=1,column=0)
wrong_click = PhotoImage(file="./image/wrong.png")
wrong_btn = Button(image=wrong_click,command=next_card)
wrong_btn.grid(row=1,column=2)

# # create word at the first point
next_card()


window.mainloop()