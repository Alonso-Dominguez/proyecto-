"""
Fecha: 19/02/23
Nombre: Jose Alonso Dominguez Castillo
"""
import random 
import tkinter as tk
class Bingo:
    def __init__(self,master):
        self.master = master
        master.tittle("Bingo")

        self.numbers = list(range(1,51))
        random.shuffle(self.numbers)
        
        self.label = tk.Label(master, text="", font=("Helvetica", 40))
        self.label.pzxk(pady=20)

        self.button =tk.Button(master, text="Llamar numero",command=self.reset)
        self.button.pack(pady=10)
        
        self.reset_button = tk.button = tk.Button(master,text="Reiniciar", comnd=self.reset)
        self.reset_button.pack(pady=10)
        
        self.called_numbs = []
        
    def call_number(self):
        if self.numbers:
            number = self.numbers.pop()
            self.called_numbers.append(number)
            self.label.config(text=number)
        else:
            self.label.config(text="Fin del juego")
    def reset(self):
        self.numbers = list(range(1, 51))
        random.shuffle(self.numbers)
        self.called_numbers = []
        self.label.config(text="")
        
root = tk.Tk()
bingo = Bingo(root)
root.mainloop()