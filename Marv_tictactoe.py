import tkinter #tk-interface (graphical user inerface library)

def set_tile(row, column):
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
        #already taken spot
        return

    board[row][column]["text"] = curr_player #mark the board
    if curr_player == playerO: #switch player
        curr_player = playerX
    else:
        curr_player = playerO
    
    label["text"] = curr_player+"'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # Rows
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] != "":
            winner = board[row][0]["text"]
            label.config(text=f"{winner} is the winner! yay", fg=color_yellow)
            for col in range(3):
                board[row][col].config(fg=color_yellow, bg=color_light_gray)
            game_over = True
            return

    # Columns
    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != "":
            winner = board[0][col]["text"]
            label.config(text=f"{winner} is the winner! yay", fg=color_yellow)
            for r in range(3):
                board[r][col].config(fg=color_yellow, bg=color_light_gray)
            game_over = True
            return
        
 # Main diagonal (top-left to bottom-right)
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] 
        and board[0][0]["text"] != ""):
        winner = board[0][0]["text"]
        label.config(text=f"{winner} is the winner! yay", fg=color_yellow)
        for i in range(3):
            board[i][i].config(fg=color_yellow, bg=color_light_gray)
        game_over = True
        return

# Anti-diagonal (top-right to bottom-left)
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] 
        and board[0][2]["text"] != ""):
        winner = board[0][2]["text"]
        label.config(text=f"{winner} is the winner! yay", fg=color_yellow)
        for i in range(3):
            board[i][2-i].config(fg=color_yellow, bg=color_light_gray)
        game_over = True
        return

#check for draw
    if turns == 9:
        label.config(text=" TIE! Dummy", fg=color_yellow)
        game_over = True
        return

def new_game():
    global curr_player, turns, game_over
    curr_player = playerX
    turns = 0
    game_over = False
    label.config(text=curr_player+ "s' turn", fg="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", bg=color_gray,fg= color_blue)

#game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0
game_over = False

#window setup
window = tkinter.Tk() #create the game window
window.title("Tic tac toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("consolas",20), background=color_gray,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, pady=10, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("consolas", 50, "bold"),
                                            background=color_gray, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column, padx=5, pady=5)

button = tkinter.Button(frame, text="NEW GAME", font=("consolas", 20), bg=color_gray,
                         fg="white", command = new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")
                        

frame.pack(padx=10, pady=10)


#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(X)+(Y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()

