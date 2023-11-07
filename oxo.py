from tkinter import Tk, PhotoImage, Button

def configure_window():
    window.title("O X O")
    window.geometry("300x300")

def create_buttons():
#    global squares
#    for square in squares:
       square = Button(window, image =available)
       square.place(x=0,y=0)
       square.config(width = 100, height = 100)

window = Tk()
configure_window()
available = PhotoImage(file = "myButton.png")
ButtonP1 = PhotoImage(file = "myButtonP1.png")
ButtonP2 = PhotoImage(file = "myButtonP2.png")
winner = PhotoImage(file = "winner.png")
squares = [None for i in range(9)]
create_buttons()

window.mainloop()