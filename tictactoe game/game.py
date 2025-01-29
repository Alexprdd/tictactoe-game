import tkinter as tk
from tkinter import messagebox
import random 

#variables for list
buttons=[[None for i in range(3)]for i in range(3)]
mode="Singleplayer"
currentplayer="X"
score={
    "X":0,
    "O":0
}
def checkwinner():
    for row in range(3):
        if buttons[row][0]["text"]==buttons[row][1]["text"]==buttons[row][2]["text"]:
            return True
    for column in range(3):
        if buttons[0][column]["text"]==buttons[1][column]["text"]==buttons[2][column]["text"]:
            return True
def reset_game():
def update_Score(currentplayer):
def isboardfull():

def on_button_clicked(row,column):
    global currentplayer
    currentplayer="X"
    if buttons[row][column]["text"]=="" and not checkwinner():
        buttons[row][column]["text"]=currentplayer
        if checkwinner():
            update_Score(currentplayer)
            messagebox.showinfo("WINNER=...",f"Player {currentplayer}")
            reset_game() 
        elif isboardfull():
            messagebox.showinfo("Game Over","TIE!")
        else:
            if mode=="Singleplayer" and currentplayer=="X":
                currentplayer="O"
                ai_move()
            else:
                currentplayer="O" if currentplayer=="X" else "X"

def singleplayer_gamemode():
    global mode
    mode="Singleplayer"
    startgame()
def multiplayer_gamemode():
    global mode
    mode="Multiplayer"
    startgame()
#window
window=tk.Tk()
window.title("TicTacToe Game")
window.geometry("500x500")
window.configure(bg="lightgrey")

score_label=tk.Label(window, text=f"Score: X={score["X"]}  O={score["O"]}", font=("Arial",12))
score_label.pack()

#frames
buttonsframe=tk.Frame(window, bd=2)
buttonsframe.pack(pady=10)

modeframe=tk.Frame(window, bd=2)
modeframe.pack(pady=10)
modeframe.configure(bg="lightgrey")

#buttons for modes
singleplayer_button=tk.Button(modeframe, text="Singleplayer", font=("Arial",12),bd=2, width=10, command=singleplayer_gamemode)
singleplayer_button.grid(row=3, column=0, padx=10)

multiplayer_button=tk.Button(modeframe, text="Multiplayer", font=("Arial",12),bd=2, width=10, command=multiplayer_gamemode)
multiplayer_button.grid(row=3, column=2, padx=10)

for row in range(3):
    for column in range(3):
        button=tk.Button(buttonsframe, text="", width=10, height=5, command=lambda r=row, c=column:on_button_clicked(r,c))
        button.grid(row=row,column=column)
        buttons[row][column]=button



window.mainloop()
