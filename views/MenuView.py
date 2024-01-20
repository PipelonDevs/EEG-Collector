from tkinter import messagebox, ttk
import tkinter as tk
from RangeSlider.RangeSlider import RangeSliderH 

from program_state import program_state
from views.AnnotationFragment import AnnotationFragment
from views.AnnotationView import AnnotationView
from views.GameView import GameView
from views.ManageDevicesView import ManageDevicesView

class MenuView(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        # self.user_id = tk.StringVar()
        # self.user_id_entry = ttk.Entry(self, width=20, textvariable=self.user_id)
        # self.user_id_button = ttk.Button(self, text="Validate", command=self.validate_user_id)

        self.project_name_label = ttk.Label(self, text="EEG Collector", font=("Helvetica", 24))
        self.description_label = ttk.Label(self, text="The goal is to create a simple tool that will greatly simplify the collection, visualization and annotation of data.", font=("Helvetica", 12))
        self.options_label = ttk.Label(self, text="Options: ", font=("Helvetica", 16))

        # self.game_name = tk.StringVar()
        # self.game_entry = ttk.Entry(self, width=20, textvariable=self.game_name)
        self.device_button = ttk.Button(self, text="Manage devices", command=self.manage_devices)
        self.game_button = ttk.Button(self, text="Play Game", command=self.start_game)
        self.annotate_button = ttk.Button(self, text="Annotate", command=self.annotate)

        
        self.arrange()


    def arrange(self):
        self.project_name_label.grid(row=0, column=0, sticky=tk.N, pady=10)
        self.description_label.grid(row=1, column=0, sticky=tk.N, pady=10)

        self.options_label.grid(row=2, column=0, sticky=tk.N, pady=(30, 10))

        self.device_button.grid(row=3, column=0, sticky=tk.N, pady=10)
        self.game_button.grid(row=4, column=0, sticky=tk.N, pady=10)
        self.annotate_button.grid(row=5, column=0, sticky=tk.N, pady=10)

        self.pack(anchor=tk.CENTER)

    def on_destroy(self):
        self.destroy()

    def start_game(self):
        self.on_destroy()
        program_state.current_view = GameView(self.master)

    def manage_devices(self):
        self.on_destroy()
        program_state.current_view = ManageDevicesView(self.master)

    def annotate(self):
        self.on_destroy()
        program_state.current_view = AnnotationView(self.master)