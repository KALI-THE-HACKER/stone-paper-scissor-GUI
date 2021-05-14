"""
Stone-Paper-Scissor Game [GUI, Python3]

This is a stone-paper-scissors game supplied with graphical user interface. The script is written in Python3 programming language, and tkinter library is also used in this project in order to supply proper GUI widgets. The game uses the same old school rules of the Stone-Paper-Scissors game (Rock-Paper-Scissors game).
Dependencies :
1. tkinter - An external python3 library for supplying proper GUI widgets. This module is present in windows by default, and for the linux operating systems, we need to install it externally.

Author : Lucky Verma (https://github.com/luckyverma-sudo)
Created on : May 13, 2021

1st modified by : Rishav Das (https://github.com/rdofficial)
1st modified on : May 14, 2021

Last modified by : Lucky Verma (Author) (https://github.com/luckyverma-sudo)
Last modified on : May 14, 2021

Changes made in last modification :
1. Changed score pattern.
2. Changed pop-up window message containing game results, choices and score of the game.
3. Solved some bugs in score showing variables.

Authors contributed to this script (Add your name below if you have contributed) :
1. Lucky Verma (github:https://github.com/luckyverma-sudo/, email:luckyv0545746@gmail.com)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
from tkinter import font


try:
    from tkinter import *
    from tkinter import messagebox as mb
    from random import randint
except Exception as e:
    # If there are any errors encountered during the importing of modules, then we display the error message on the console screen

    input(f'\n[ Error : {e} ]\nPress enter key to continue...')
    exit()

# Declaring the variable to store the score of the current game
score = 0


def checkResults(userEnteredChoice):
    """ The function which calculates the score of the game, using the user entered option and the computer generated random choice. Then sums up the actual score and displays the score on the messagebox. The function uses some conventions which are mentioned below :
Stone --> 1
Paper --> 2
Scissors --> 3
These conventions are to be used during the calculation of the result of each rounds of the game, even the user enters the input through the radiobuttons, and these 1,2,3 are the values that are recieved.
The calculations of the result also uses some conventions for the score increment and decrement, which are listed below :
1. Win --> +5 score
2. Draw --> +0 score
3. Loss --> -5 score
And, the win, loss, and draw are generated using the rules of the old school game of stone-paper-scissors. """

    # Accessing the global variable 'score' and also giving it global scope inside this function too
    global score

    # Getting the computer choice
    computerChoice = randint(1, 3)

    # Calculating the result as per user entered choice
    if userEnteredChoice == 1:
        # If the user choosed stone

        userEnteredChoice_var = "Stone"
        if computerChoice == 1:
            # If the computer also choosed stone, then its a draw

            computerChoice_var = "Stone"
            score += 0
            mb.showinfo(
                'Draw', f"    Game Draw!\n\nYour's Choice : {userEnteredChoice_var.upper()}\nBot's Choice : {computerChoice_var.upper()}\n\n Current score : {score}.")
        elif computerChoice == 2:
            # If the computer choosed paper, then its a loss

            computerChoice_var = "Paper"
            score -= 5
            mb.showinfo(
                'Lose', f"    You Lose!\n\nYour's Choice : {userEnteredChoice_var.upper()}\nBot's Choice : {computerChoice_var.upper()}\n\n Current score : {score}.")
        elif computerChoice == 3:
            # If the computer choosed scissors, then its a win

            computerChoice_var = "Scissor"
            score += 5
            mb.showinfo(
                'Win', f"    You Win!\n\nYour's Choice : {userEnteredChoice_var.upper()}\nBot's Choice : {computerChoice_var.upper()}\n\n Current score : {score}.")
        else:
            # If the computer choosen option is not recognized

            mb.showerror(
                'Failure', f'The computer entered choice is not recognized. Current score : {score}.')
    elif userEnteredChoice == 2:
        # If the user choosed paper

        userEnteredChoice_var = "Paper"
        if computerChoice == 1:
            # If the computer choosed stone, then its a win

            computerChoice_var = "Stone"
            score += 5
            mb.showinfo(
                'Win', f"    You win!\n\nYour's Choice : {userEnteredChoice_var.upper()}\nBot's Choice : {computerChoice_var.upper()}\n\n Current score : {score}.")
        elif computerChoice == 2:
            # If the computer also choosed paper, then its a draw

            computerChoice_var = "Paper"
            score += 0
            mb.showinfo(
                'Draw', f"    Game Draw!\n\nYour's Choice : {userEnteredChoice_var.upper()}\nBot's Choice : {computerChoice_var.upper()}\n\n Current score : {score}.")
        elif computerChoice == 3:
            # If the computer choosed scissors, then its a loss

            computerChoice_var = "Scissor"
            score -= 5
            mb.showinfo(
                'Lose', f"    you Lose!\n\nYour's Choice : {userEnteredChoice_var.upper()}\nBot's Choice : {computerChoice_var.upper()}\n\n Current score : {score}.")
        else:
            # If the computer choosen option is not recognized

            mb.showerror(
                'Failure', f'The computer entered choice is not recognized. Current score : {score}.')
    elif userEnteredChoice == 3:
        # If the user choosed scissors

        userEnteredChoice_var = "Scissor"
        if computerChoice == 1:
            # If the computer choosed stone, then its a loss

            computerChoice_var = "Stone"
            score -= 5
            mb.showinfo(
                'Lose', f"    You Lose!\n\nYour's Choice : {userEnteredChoice_var.upper()}\nBot's Choice : {computerChoice_var.upper()}\n\n Current score : {score}.")
        elif computerChoice == 2:
            # If the computer choosed paper, then its a win

            computerChoice_var = "Paper"
            score += 5
            mb.showinfo(
                'Win', f"    You Win!\n\nYour's Choice : {userEnteredChoice_var.upper()}\nBot's Choice : {computerChoice_var.upper()}\n\n Current score : {score}.")
        elif computerChoice == 3:
            # If the computer also choosed scissors, then its a draw

            computerChoice_var = "Scissor"
            score += 0
            mb.showinfo(
                'Draw', f"    Game Draw!\n\nYour's Choice : {userEnteredChoice_var.upper()}\nBot's Choice : {computerChoice_var.upper()}\n\n Current score : {score}.")
        else:
            # If the computer choosen option is not recognized

            mb.showerror(
                'Failure', f'The computer entered choice is not recognized. Current score : {score}.')
    else:
        # If the user entered choice is not recognized

        mb.showerror('Invalid input',
                     'The option you entered is not recognized')

    scoreLabelVariable.set(f'Current score : {score}')
    root.update_idletasks()


def main():
    # Making some of the variables declared in this function, to be globally accessed
    global root, scoreLabelVariable

    # Declaring the main tkinter window and configuring it
    root = Tk()
    root.config(background='black')
    root.title('Stone-Paper-Scissor Game by Lucky Verma')
    root.geometry('450x350')
    root.minsize(450, 350)
    root.maxsize(450, 600)

    # Displaying the main heading label for the game
    Label(root, text='STONE-PAPER-SCISSOR', background='black', foreground='cyan',
          font=('consolas', 18, 'bold', 'italic', 'underline')).pack(padx=5, pady=10)

    # Setting the widgets for user input (Labels, radiobuttons, etc)
    # ----
    # Note :
    # 1. All the widgets in the tkinter window except the heading label, are included under this tkinter frame declared as 'frame1'.
    # 2. There are 3 radiobuttons declared in this frame1, and they indicate the options : stone, paper, scissors.
    # ----
    frame1 = Frame(root, background='black', relief=GROOVE)
    frame1.pack(padx=5, pady=5)
    Label(
        frame1,
        text='Select your choice : ',
        foreground='cyan',
        background='black',
        font=('monospace', 15)).pack(padx=5, pady=5)
    # Declaring the integer type variable for the the radiobutton inputs
    choice = IntVar(root)

    # The radiobuttons for displaying the options on the tkinter window
    Radiobutton(
        frame1,
        text='Stone',
        foreground='cyan',
        background='black',
        value=1,
        variable=choice,
        selectcolor='black',
        font=('monospace', 12),
        padx=5,
        pady=5,
        command=lambda: checkResults(choice.get())
    ).pack(padx=5, pady=7.5)
    Radiobutton(
        frame1,
        text='Paper',
        foreground='cyan',
        background='black',
        value=2,
        variable=choice,
        selectcolor='black',
        font=('monospace', 12),
        padx=5,
        pady=5,
        command=lambda: checkResults(choice.get())
    ).pack(padx=5, pady=7.5)
    Radiobutton(
        frame1,
        text='Scissors',
        foreground='cyan',
        background='black',
        value=3,
        variable=choice,
        selectcolor='black',
        font=('monospace', 12),
        padx=5,
        pady=5,
        command=lambda: checkResults(choice.get())
    ).pack(padx=5, pady=7.5)

    # The label which contains the score details
    # The string variable to store the text to be displayed on the current score label
    scoreLabelVariable = StringVar(root)
    scoreLabelVariable.set(f'Current score : {score}')
    Label(
        frame1,
        textvariable=scoreLabelVariable,
        foreground='white',
        background='black',
        font=('monospace', 11, 'bold', 'italic'),
    ).pack(padx=5, pady=5)

    mainloop()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses CTRL+C key combo, then we exit the script

        exit()
    except Exception as e:
        # If there are any errors encountered during the process, then we display the error message on the console screen

        input(f'\n[ Error : {e} ]\nPress enter key to continue...')
        exit()
