from tkinter import Tk, PhotoImage, Button, messagebox

def configure_window():
    window.title("O X O")
    window.geometry("300x300")

def square_taken():
    messagebox.showerror(title = "Already selected", message="This square has already been selected, you cannot pick it.")

def check_win():
    global moves
    won_game = False
    global counter
    player = counter%2
    if moves[0][0] == player and moves[1][1] == player and moves[2][2] == player: #Could have a for loop, but it's just longer
        return True
    if moves[0][2] == player and moves[1][1] == player and moves[2][0] == player:
        return True
    for i in range(3): # checking all the rows
        for j in range(3):
            if moves[i][j] != player:
                won_game = False
                break
            else:
                won_game = True
        if won_game == True:
            return True
    for i in range(3): # checking all the columns
        for j in range(3):
            if moves[j][i] != player:
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
        global win
        win.pack(fill="both", expand=True)
        window.after(5000, game_loop)

def handle_button_click(button_number):
    global counter
    
    player = counter%2
    if(player==0):
        icon = ButtonP1
    else:
        icon = ButtonP2 
    squares[button_number].config(image =icon, command = lambda:square_taken())
    update_move(button_number, player)
    counter+=1

def create_buttons():
   for i in range(len(squares)):
       squares[i] = Button(window, image =available, command=lambda n=i:handle_button_click(n))
       squares[i].place(x=100 * (i%3),y=100 * int(i/3))
       squares[i].config(width = 100, height = 100)

def reset_buttons():
    win.pack_forget()
    for i in range(len(squares)):
        squares[i].config(image=available, command=lambda n=i:handle_button_click(n))
    
def game_loop():
    global win, counter, moves
    reset_buttons()
    create_buttons()
    counter=0
    moves = [[-1 for i in range(3)] for j in range(3)] 

window = Tk()
configure_window()
available = PhotoImage(file = "myButton.png")
ButtonP1 = PhotoImage(file = "myButtonP1.png")
ButtonP2 = PhotoImage(file = "myButtonP2.png")
winner = PhotoImage(file = "winner.png")
squares = [None for i in range(9)]
win = Button(window, image= winner)
create_buttons()
counter=0
moves = [[-1 for i in range(3)] for j in range(3)]


game_loop()
window.mainloop()