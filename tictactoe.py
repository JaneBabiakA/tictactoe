import tkinter as tk
from functools import partial

score = {"x": 0, "o": 0}

def startGame(): #reset all necessary stats
    player = "x"
    clicks = 0
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
    xScore["text"] = "x: " + str(score["x"])
    oScore["text"] = "o: " + str(score["o"])
    return None

def squareClick(i, j):
    global player
    global clicks
    if buttons[i][j]["text"] == "":
        clicks+= 1
        buttons[i][j]["text"] = player
        if player == "x":
            player = "o"
        else:
            player = "x"
        if clicks >= 5: #check for a win
            for i in range(3):
                if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
                    score[buttons[i][0]["text"]] += 1
                    alert["text"] = "Player " + buttons[i][0]["text"] + " wins the game!"
                    break
                elif buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
                    score[buttons[0][i]["text"]] += 1
                    alert["text"] = "Player " + buttons[0][i]["text"] + " wins the game!"
                    break
            if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
                score[buttons[0][0]["text"]] += 1
                alert["text"] = "Player " + buttons[0][0]["text"] + " wins the game!"
            elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
                score[buttons[0][2]["text"]] += 1
                alert["text"] = "Player " + buttons[0][2]["text"] + " wins the game!"
    return None

#configure main window
window = tk.Tk()
window.title("TicTacToe")
window.geometry("460x505")
window.maxsize(460, 505)
window.grid_columnconfigure(0, weight=1)

#header
header = tk.Frame(window, width="495", height="50")
header.grid(row=0, sticky="nsew")
header.grid_columnconfigure(0, weight=1)
newGame = tk.Button(header, text="New Game", command=startGame)
newGame.grid(row=0, column=0, sticky="w")
title = tk.Label(header, text="TicTacToe")
title.grid(row=1, column=0)
container = tk.Frame(header)
container.grid(row=0, column=1, sticky="e")
oScore = tk.Label(container)
xScore = tk.Label(container)
oScore.grid(row=0, column=0)
xScore.grid(row=0, column=1)
alert = tk.Label(header, text="")
alert.grid(row=2)


#playing grid
gameGrid = tk.Frame(window, width="495", height="495")
gameGrid.grid(row=1, padx=(5, 5), pady=(5, 5), sticky="nsew")
gameGrid.grid_columnconfigure(0, weight=1)
buttons = [[tk.Button(gameGrid, width="20", height="9", command=partial(squareClick, i, j)) for j in range(3)] for i in range(3)]
for k in range(3):
    for l in range(3):
        print(buttons[k][l])
        buttons[k][l].grid(row=k, column=l)
clicks = 0
player = "x"
startGame()
window.mainloop()