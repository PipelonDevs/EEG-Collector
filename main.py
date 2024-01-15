import tkinter as tk


from tkinter import messagebox as mBox
from views.MenuVew import MenuView
from views.tetris_experiment.experiment_settings import phases_iterator
from program_state import program_state

root = tk.Tk()
root.title("Data gatherring")
root.geometry("500x500")
canvas = tk.Canvas(root, height=500, width=500)

# main_frame = tk.Frame(root)
# main_frame.pack(fill=tk.BOTH, expand=True)
program_state.phases_iterator = phases_iterator
program_state.master = root
program_state.current_view = MenuView(root)

root.mainloop()