from tkinter import Tk, PhotoImage, Button, messagebox

def configure_window():
    window.title("O X O")
    window.geometry("300x300")

def square_taken():
    messagebox.showerror(title = "Already selected", message="This square has already been selected, you cannot pick it.")

def check_win():
    global moves
    won_game = False
    global player
    if(player ==1): #You only have to check if the player that just went won, which this does
        playerCheck =2
    else:
        playerCheck = 1
    if moves[0][0] == playerCheck and moves[1][1] == playerCheck and moves[2][2] == playerCheck: #Could have a for loop, but it's just longer
        return True
    if moves[0][2] == playerCheck and moves[1][1] == playerCheck and moves[2][0] == playerCheck:
        return True
    for i in range(3): # checking all the rows
        for j in range(3):
            if moves[i][j] != playerCheck:
                won_game = False
                break
            else:
                won_game = True
        if won_game == True:
            return True
    for i in range(3): # checking all the columns
        for j in range(3):
            if moves[j][i] != playerCheck:
                won_game = False
                break
            else:
                won_game = True
        if won_game == True:
            return True
    return won_game # This should always return false if it reaches here
    

def update_move(buttonNum, player):
    global moves
    moves[buttonNum%3][int(buttonNum/3)] = player
    if check_win() == True:
        print("won")
        win = Button(window, image= winner)
        win.pack(expand=True)
        window.after(5000, game_loop)

def handle_button_click(button_number):
    global player
    if(player == 1):
        icon = ButtonP1
        player =2
    else:
        icon = ButtonP2
        player =1 
    squares[button_number].config(image =icon, command = lambda:square_taken())
    update_move(button_number, player)

def create_buttons():
   for i in range(len(squares)):
       squares[i] = Button(window, image =available, command=lambda n=i:handle_button_click(n))
       squares[i].place(x=100 * (i%3),y=100 * int(i/3))
       squares[i].config(width = 100, height = 100)

def game_loop():
    win = None
    create_buttons()
    player =1

    moves = [[0] * 3] * 3

window = Tk()
configure_window()
available = PhotoImage(file = "myButton.png")
ButtonP1 = PhotoImage(file = "myButtonP1.png")
ButtonP2 = PhotoImage(file = "myButtonP2.png")
winner = PhotoImage(file = "winner.png")
squares = [None for i in range(9)]
player =1
moves = [[0] * 3] * 3
win = None
game_loop()


window.mainloop()