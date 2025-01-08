import tkinter as tk
from tkinter import messagebox
import random 

#variables for list
buttons=[[None for i in range(3)]for i in range(3)]
mode="single"
currentplayer="X"
score={
    "X":0,
    "O":0
}
#window
window=tk.Tk()
window.title("TicTacToe Game")
window.geometry("500x500")
window.configure(bg="lightgrey")

score_label=tk.Label(window, text=f("score: X={score["X"]}  O={score["O"]}"))
score_label.pack()
#frames
buttonsframe=tk.Frame(window, bd=2)
buttonsframe.pack(pady=10)

modeframe=tk.Frame(window, bd=2)
modeframe.pack(pady=10)
modeframe.configure(bg="lightgrey")

#buttons for modes
singleplayer_button=tk.Button(modeframe, text="Singleplayer", font=("Arial",12),bd=2, width=10)
singleplayer_button.grid(row=3, column=0, padx=10)

multiplayer_button=tk.Button(modeframe, text="Multiplayer", font=("Arial",12),bd=2, width=10)
multiplayer_button.grid(row=3, column=2, padx=10)

for row in range(3):
    for column in range(3):
        button=tk.Button(buttonsframe, text="", width=10, height=5)
        button.grid(row=row,column=column)
        buttons[row][column]=button




window.mainloop()