from tkinter import Tk, PhotoImage, Button

def configure_window():
    window.title("O X O")
    window.geometry("300x300")

def handle_button_click(button_number):
    print(button_number)

def create_buttons():
   for i in range(len(squares)):
       squares[i] = Button(window, image =available, command=lambda n=i:handle_button_click(n))
       squares[i].place(x=100 * (i%3),y=100 * int(i/3))
       squares[i].config(width = 100, height = 100)

window = Tk()
configure_window()
available = PhotoImage(file = "myButton.png")
ButtonP1 = PhotoImage(file = "myButtonP1.png")
ButtonP2 = PhotoImage(file = "myButtonP2.png")
winner = PhotoImage(file = "winner.png")
squares = [None for i in range(9)]
create_buttons()
print(squares)
window.mainloop()