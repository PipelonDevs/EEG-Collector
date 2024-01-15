from tkinter import ttk
import tkinter as tk

from program_state import program_state
from views.GameView import GameView

class MenuView(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.user_id = tk.StringVar()
        self.user_id_label = ttk.Label(self, text="User ID: ")
        self.user_id_entry = ttk.Entry(self, width=30, textvariable=self.user_id)

        self.options_label = ttk.Label(self, text="\nOptions: ")

        self.game_name = tk.StringVar()
        self.game_entry = ttk.Entry(self, width=30, textvariable=self.game_name)
        self.game_button = ttk.Button(self, text="Game", command=self.start_game)


        self.arrange()


    def arrange(self):
        self.user_id_label.grid(row=0, column=0, sticky=tk.W)
        self.user_id_entry.grid(row=0, column=2, sticky=tk.W)

        self.options_label.grid(row=3, column=0, sticky=tk.W, ipady=10)

        self.game_entry.grid(row=4, column=0, sticky=tk.W)
        self.game_button.grid(row=4, column=1, sticky=tk.W)        


        self.pack(anchor=tk.CENTER)

    def start_game(self):
        program_state.user_id = self.user_id.get()
        program_state.played_game = self.game_name.get()
        self.destroy()
        program_state.current_view = GameView(self.master)

    def start_tetris_experiment(self):
        program_state.user_id = self.user_id.get()
        self.destroy()
        program_state.current_view = next(program_state.phases_iterator)()

