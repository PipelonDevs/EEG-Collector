import tkinter as tk


from tkinter import messagebox as mBox
from views.MenuVew import MenuView
from program_state import program_state

root = tk.Tk()
root.title("Data collector")
root.geometry("500x500")
canvas = tk.Canvas(root, height=500, width=500)

program_state.master = root
program_state.current_view = MenuView(root)

root.mainloop()