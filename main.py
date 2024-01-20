import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

from tkinter import messagebox as mBox
from views.MenuView import MenuView
from program_state import program_state
import os
from consts import BASE_DATASET_PATH, DEVICES_PATH, GAME_DATASET_PATH


root = ThemedTk(theme='ubuntu')
root.title("Data collector")
root.geometry("900x500")

def go_to_menu():
    program_state.current_view.destroy()
    program_state.current_view = MenuView(root)


def create_folders():
    os.makedirs(BASE_DATASET_PATH, exist_ok=True)
    os.makedirs(os.path.join(BASE_DATASET_PATH, GAME_DATASET_PATH), exist_ok=True)
    os.makedirs(DEVICES_PATH, exist_ok=True)

create_folders()

menubar = tk.Menu(root)
root.config(menu=menubar)

menubar.add_command(label="Home", command=go_to_menu)
canvas = tk.Canvas(root, height=500, width=500)

program_state.master = root
program_state.current_view = MenuView(root)

root.mainloop()