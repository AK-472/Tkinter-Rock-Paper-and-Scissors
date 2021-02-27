# These are the modules I will be using
import random
from tkinter import *
root = Tk()
root.title("Rock, Paper, and Scissors")
# These humoungus functions give you every single RPS combination


def rock_button_click():
    blank1 = Label(root, text="                                     ",
                   ).grid(row=1, column=1)
    blank2 = Label(root, text="                                     ",
                   ).grid(row=2, column=1)
    blank3 = Label(root, text="                                     ",
                   ).grid(row=3, column=1)
    blank4 = Label(root, text="                                     ",
                   ).grid(row=2, column=2)
    blank5 = Label(root, text="                                     ",
                   ).grid(row=1, column=2)
    blank6 = Label(root, text="                                     ",
                   ).grid(row=3, column=2)
    rocks = True
    my_choice_1 = Label(root, text="Rock", fg="grey",
                        font=20).grid(row=1, column=1)
    label_1 = Label(root, text="VS", font=20).grid(row=2, column=1)
    chosen = random.randrange(1, 4)
    if chosen == 1:
        computer_counter = Label(
            root, text="Rock", fg="grey", font=20).grid(row=3, column=1)
        if chosen == 1 and rocks:
            result = Label(root, text="Tie", fg="black",
                           font=20).grid(row=2, column=2)
    elif chosen == 2:
        computer_counter = Label(
            root, text="Paper", fg="grey", font=20).grid(row=3, column=1)
        if chosen == 2 and rocks:
            result = Label(root, text="Computer Wins",
                           fg="black", font=20).grid(row=2, column=2)
    elif chosen == 3:
        computer_counter = Label(root, text="Scissor",
                                 fg="grey", font=20).grid(row=3, column=1)
        if chosen == 3 and rocks:
            result = Label(root, text="Player Wins",
                           fg="black", font=20).grid(row=2, column=2)


def paper_button_click():
    blank1 = Label(root, text="                                     ",
                   ).grid(row=1, column=1)
    blank2 = Label(root, text="                                     ",
                   ).grid(row=2, column=1)
    blank3 = Label(root, text="                                     ",
                   ).grid(row=3, column=1)
    blank4 = Label(root, text="                                     ",
                   ).grid(row=2, column=2)
    blank5 = Label(root, text="                                     ",
                   ).grid(row=1, column=2)
    blank6 = Label(root, text="                                     ",
                   ).grid(row=3, column=2)
    papers = True
    my_choice_1 = Label(root, text="Paper", fg="grey",
                        font=20).grid(row=1, column=1)
    label_1 = Label(root, text="VS", font=20).grid(row=2, column=1)
    chosen = random.randrange(1, 4)
    if chosen == 1:
        computer_counter = Label(
            root, text="Rock", fg="grey", font=20).grid(row=3, column=1)
        if chosen == 1 and papers:
            result = Label(root, text="Player Wins",
                           fg="black", font=20).grid(row=2, column=2)
    elif chosen == 2:
        computer_counter = Label(
            root, text="Paper", fg="grey", font=20).grid(row=3, column=1)
        if chosen == 2 and papers:
            result = Label(root, text="Tie", fg="black",
                           font=20).grid(row=2, column=2)
    elif chosen == 3:
        computer_counter = Label(root, text="Scissor",
                                 fg="grey", font=20).grid(row=3, column=1)
        if chosen == 3 and papers:
            result = Label(root, text="Computer Wins",
                           fg="black", font=20).grid(row=2, column=2)


def scissors_button_click():
    blank1 = Label(root, text="                                     ",
                   ).grid(row=1, column=1)
    blank2 = Label(root, text="                                     ",
                   ).grid(row=2, column=1)
    blank3 = Label(root, text="                                     ",
                   ).grid(row=3, column=1)
    blank4 = Label(root, text="                                     ",
                   ).grid(row=2, column=2)
    blank5 = Label(root, text="                                     ",
                   ).grid(row=1, column=2)
    blank6 = Label(root, text="                                     ",
                   ).grid(row=3, column=2)
    scissors = True
    my_choice_1 = Label(root, text="Scissors", fg="grey",
                        font=20).grid(row=1, column=1)
    label_1 = Label(root, text="VS", font=20).grid(row=2, column=1)
    chosen = random.randrange(1, 4)
    if chosen == 1:
        computer_counter = Label(
            root, text="Rock", fg="grey", font=20).grid(row=3, column=1)
        if chosen == 1 and scissors:
            result = Label(root, text="Computer Wins",
                           fg="black", font=20).grid(row=2, column=2)
    elif chosen == 2:
        computer_counter = Label(
            root, text="Paper", fg="grey", font=20).grid(row=3, column=1)
        if chosen == 2 and scissors:
            result = Label(root, text="Player Wins",
                           fg="black", font=20).grid(row=2, column=2)
    elif chosen == 3:
        computer_counter = Label(root, text="Scissor",
                                 fg="grey", font=20).grid(row=3, column=1)
        if chosen == 3 and scissors:
            result = Label(root, text="Tie", fg="black",
                           font=20).grid(row=2, column=2)


# Just some info on the application itself
info = Label(root, text="Rock, Paper, and Scissors",
             font=20).grid(row=0, column=0)
# These are the buttons you can choose from
rock_button = Button(root, text="Rock", fg="red",
                     command=rock_button_click, padx=16, pady=11).grid(row=1, column=0)
paper_button = Button(root, text="Paper", fg="green",
                      command=paper_button_click, padx=16, pady=11).grid(row=2, column=0)
scissors_button = Button(root, text="Scissor", fg="blue",
                         command=scissors_button_click, padx=16, pady=11).grid(row=3, column=0)
root.mainloop()
