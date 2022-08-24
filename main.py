import tkinter as tk
from tkinter import messagebox
from config import *
from word_bank import *
from card import *

timer = None
word_text = None
language_text = None
word_bank = WordBank()
card = Card()


def clear_text():
    card_canvas.create_image(400, 263, image=card_front_img)
    language_canvas.configure(background="white", highlightthickness=0)
    language_canvas.itemconfig(language_text, text="")
    word_canvas.configure(background="white", highlightthickness=0)
    word_canvas.itemconfig(word_text, text="")



def right_button_clicked():
    word_bank.word_learned(card.spanish_word)
    window.after_cancel(timer)
    clear_text()
    card.get_next_pair()
    show_next_pair()
    update_progress()


def wrong_button_clicked():
    window.after_cancel(timer)
    clear_text()
    card.get_next_pair()
    show_next_pair()
    update_progress()



def destroy_welcome():
    welcome_canvas.destroy()
    start_canvas.destroy()
    start_button.destroy()
    protect_canvas_lower.destroy()
    protect_canvas_upper.destroy()
    update_progress()
    card.get_next_pair()
    show_next_pair()


def show_next_pair():
    clear_text()
    card_canvas.create_image(400, 263, image=card_front_img)
    language_canvas.configure(background="white", highlightthickness=0)
    global language_text
    language_text = language_canvas.create_text(350, 30, text="Spanish:", fill=BACK_OF_CARD_COLOR, font=("Helvetica", 24, "italic"))
    word_canvas.configure(background="white", highlightthickness=0)
    global word_text
    word_text = word_canvas.create_text(350, 30, text=card.spanish_word, fill="black", font=("Helvetica", 40, "bold"), anchor="n")
    global timer
    timer = window.after(SLEEP_TIME * 1000, flip_card)



def flip_card():
    card_canvas.create_image(400, 263, image=card_back_img)
    global language_text
    language_canvas.configure(background=BACK_OF_CARD_COLOR, highlightthickness=0)
    language_canvas.itemconfig(language_text, text="English:", fill="white")
    global word_text
    word_canvas.configure(background=BACK_OF_CARD_COLOR, highlightthickness=0)
    word_canvas.itemconfig(word_text, text=card.english_word)


def show_description_popup():
    messagebox.showinfo(title="Description", message=DESCRIPTION_TEXT)


def update_progress():
    """Reads from 'words_learned.json' and 'words_database.json' files.
    Displays number of words learned vs number of words in database."""
    word_bank.get_progress()
    progress_label.config(text="Learned: {} / {}".format(word_bank.words_learned_count, word_bank.words_to_learn_count))


def show_reset_progress_popup():
    yes = messagebox.askyesno(title="Warning", message="Are you sure you want to reset your progress?")
    if yes:
        reset_progress()


def reset_progress():
    word_bank.reset_progress()
    update_progress()
    window.after_cancel(timer)
    clear_text()
    card.get_next_pair()
    show_next_pair()
    update_progress()


window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
right_btn_img = tk.PhotoImage(file="images/right.png")
wrong_btn_img = tk.PhotoImage(file="images/wrong.png")

description_button = tk.Button(text="Description", highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=show_description_popup)
description_button.grid(row=0, column=0, sticky="w", padx=50)

progress_label = tk.Label(text="Lorem Ipsum", font=("Helvetica", 14, "normal"), fg="black", bg=BACKGROUND_COLOR)
progress_label.grid(row=0, column=1)

reset_button = tk.Button(text="Reset", highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=show_reset_progress_popup)
reset_button.grid(row=0, column=2, sticky="e", padx=60, pady=10)

card_canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_canvas.create_image(400, 263, image=card_back_img)
card_canvas.grid(row=1, column=0, columnspan=3)

wrong_button = tk.Button(image=wrong_btn_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=wrong_button_clicked)
wrong_button.grid(row=2, column=0)

right_button = tk.Button(image=right_btn_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=right_button_clicked)
right_button.grid(row=2, column=2)

language_canvas = tk.Canvas(width=700, height=60)
language_canvas.configure(background=BACK_OF_CARD_COLOR, highlightthickness=0)
language_canvas.place(x=38, y=170)

word_canvas = tk.Canvas(width=700, height=100)
word_canvas.configure(background=BACK_OF_CARD_COLOR, highlightthickness=0)
word_canvas.place(x=38, y=300)

protect_canvas_upper = tk.Canvas(width=700, height=30)
protect_canvas_upper.configure(background=BACKGROUND_COLOR, highlightthickness=0)
protect_canvas_upper.place(x=38, y=13)

welcome_canvas = tk.Canvas(width=700, height=60)
welcome_canvas.configure(background=BACK_OF_CARD_COLOR, highlightthickness=0)
welcome_canvas.create_text(350, 30, text="Welcome to Flashy!", font=("helvetica", 40, "bold"), anchor="center", fill="black")
welcome_canvas.place(x=38, y=200)

start_canvas = tk.Canvas(width=700, height=60)
start_canvas.configure(background=BACK_OF_CARD_COLOR, highlightthickness=0)
start_canvas.create_text(350, 30, text="Click the button to start learning some Spanish!", font=("helvetica", 20, "normal"), anchor="center")
start_canvas.place(x=38, y=260)

start_button = tk.Button(text="Start", command=destroy_welcome, highlightthickness=0, highlightbackground=BACK_OF_CARD_COLOR)
start_button.place(x=350, y=400)

protect_canvas_lower = tk.Canvas(width=700, height=105)
protect_canvas_lower.configure(background=BACKGROUND_COLOR, highlightthickness=0)
protect_canvas_lower.place(x=38, y=574)

window.mainloop()
