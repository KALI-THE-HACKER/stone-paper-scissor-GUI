from tkinter import *
from tkinter import messagebox as mb
import random
import time


def show():
    root.geometry("450x600")
    root.minsize(450, 600)
    root.maxsize(450, 600)
    u_choice = var.get()
    int_choice = str(u_choice)

    if (int_choice == "1"):
        choice = "stone"

    elif (int_choice == "2"):
        choice = "paper"

    elif (int_choice == "3"):
        choice = "scissor"

    else:
        mb.showerror('error', "Please select any choice!")
        return 0

    blank_label = Label(root, text="", background=bg).grid(row=13, column=0)
    blank_label = Label(root, text="", background=bg).grid(row=14, column=0)

    yours_choice = Label(
        first_frame, text="Your's Choice     :", background=bg, foreground=fg, font=(17)).grid(row=15, column=0)
    yours_choice_ = Label(
        first_frame, text=f"{choice.upper()}", background=bg, foreground=fg, font=(17)).grid(row=15, column=1)

    blank_label = Label(root, text="", background=bg).grid(row=16, column=0)

    # starting of main algorithm of this game i.e. working of bot
    options = ("stone", "paper", "scissor")
    bot_choice = random.choice(options)

    bots_choice = Label(first_frame, text="Bot's Choice      :",
                        background=bg, foreground=fg, font=(17)).grid(row=17, column=0)
    bots_choice_ = Label(first_frame, text=f"{bot_choice.upper()}",
                         background=bg, foreground=fg, font=(17)).grid(row=17, column=1)

    if (choice == "stone"):
        if (bot_choice == "stone"):
            win_lose = "Game Tie!"

        elif (bot_choice == "paper"):
            win_lose = "You Lose!"

        elif (bot_choice == "scissor"):
            win_lose = "You Win!"

    elif (choice == "paper"):
        if (bot_choice == "paper"):
            win_lose = "Game Tie!"

        elif (bot_choice == "scissor"):
            win_lose = "You Lose!"

        elif (bot_choice == "stone"):
            win_lose = "You Win!"

    elif (choice == "scissor"):
        if (bot_choice == "scissor"):
            win_lose = "Game Tie!"

        elif (bot_choice == "stone"):
            win_lose = "You Lose!"

        elif (bot_choice == "paper"):
            win_lose = "You Win!"

        else :
            mb.showerror('error', "[ Error ]")


    wi_lo = Label(first_frame, text=win_lose, background=bg,
                  foreground=fg, font=("Consolas 20 bold")).place(x=160, y=440)

    play_again_btn = Button(first_frame, text="PLAY AGAIN", font=(
        14), background=bg, foreground=fg, command = playagain).place(x = 60, y = 530)

    exit_btn = Button(first_frame, text="EXIT GAME", font=(
        14), background=bg, foreground=fg, command = exitgame).place(x = 265, y = 530)

def playagain():
    pass

    


def exitgame():
    mb.showwarning("Terminating", 'Click OK to Terminate...')
    exit()


root = Tk()
root.config(background="black")
root.title("Stone - Paper - Scissor game by lucky verma")

bg = "black"
fg = "cyan"


root.geometry("450x350")
root.minsize(450, 350)
root.maxsize(450, 600)
root.config(background="black")

blank_label = Label(root, text="", background=bg).grid(row=0, column=0)
blank_label = Label(root, text="", background=bg).grid(row=1, column=0)
main_label = Label(root, text="|| STONE - PAPER - SCISSOR ||", background=bg,
                   foreground=fg, font=("Consolas 16 italic underline")).place(x=30, y=10)


blank_label = Label(root, text="", background=bg).grid(row=2, column=0)
blank_label = Label(root, text="", background=bg).grid(row=3, column=0)


first_frame = Frame(root, background=bg, relief=GROOVE).grid(row=4, column=0)

l1 = Label(first_frame, text="Select your choice :", background=bg,
           foreground=fg, font=(17)).grid(row=4, column=0)

var = IntVar()

rbtn = Radiobutton(first_frame, text="    STONE     ", background=bg, value=1, variable=var,
                   foreground=fg, selectcolor="black", font=(16)).grid(row=5, column=1)

rbtn = Radiobutton(first_frame, text="    PAPER      ", background=bg, value=2, variable=var,
                   foreground=fg, selectcolor="black", font=(16)).grid(row=6, column=1)

rbtn = Radiobutton(first_frame, text="    SCISSOR  ", background=bg, value=3, variable=var,
                   foreground=fg, selectcolor="black", font=(16)).grid(row=7, column=1)

blank_label = Label(root, text="", background=bg).grid(row=8, column=0)
blank_label = Label(root, text="", background=bg).grid(row=9, column=0)
blank_label = Label(root, text="", background=bg).grid(row=10, column=0)
# blank_label = Label(root, text="", background=bg).grid(row=11, column=0)

show_btn = Button(first_frame, text="Show!", background=bg,
                  foreground=fg, font=(17), command=show).grid(row=12, column=1)


root.mainloop()
