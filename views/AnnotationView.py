import time
from tkinter import font, ttk, messagebox
import tkinter as tk
from tkinter.filedialog import askopenfilename

from program_state import program_state
from .AnnotationFragment import AnnotationFragment


def get_metadata_from_path(path):
    """
    The metadata components are assumed to be in the following order: 
    user_id, game_name, date, time.

    Example:
    path = "user001_Tetris_2021-05-10/user001_Tetris_2021-05-10_11-30.csv"
    user_id, game_name, date, time = get_metadata_from_path(path)

    Parameters:
    path (str): The file path from which to extract metadata.

    Returns:
    tuple: A tuple containing the user_id, game_name, date, and time extracted from the file path.
    """
    # 1. Get the filename from the path
    # 2. Remove the extension from the filename
    # 3. Split the filename by the underscore character
    user_id, game_name, date, time = path \
        .split("/")[-1].split("\\")[-1] \
        .split(".")[0] \
        .split("_")
    return user_id, game_name, date, time


class AnnotationView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        master.withdraw() # we don't want a full GUI, so keep the root window from appearing
        full_path = askopenfilename(initialdir="Datasets/GameDatasets", title="Select dataset to annotate", filetypes=(("json files", "*.json"), ("all files", "*.*"))) 
        master.deiconify() # make the root window appear again
        
        user_id, game_name, date, time = get_metadata_from_path(full_path)

        self.view_name_label = ttk.Label(self, text="Annotate Data", font=("Helvetica", 24))

        self.user_id_label = ttk.Label(self, text=f"User ID")
        self.game_name_label = ttk.Label(self, text=f"Game")
        self.datetime_label = ttk.Label(self, text=f"Date")
        # self.device_name_label = ttk.Label(self, text=f"Device")

        self.user_id_value_label = ttk.Label(self, font=font.Font(weight="bold"), text=f"{user_id}")
        self.game_name_value_label = ttk.Label(self, font=font.Font(weight="bold"), text=f"{game_name}")
        self.date_value_label = ttk.Label(self, font=font.Font(weight="bold"), text=f"{date} {time}")
        # self.device_name_value_label = ttk.Label(self, font=font.Font(weight="bold"), text=f"{self.annotations_fragment.meta.device.device_name}")

        self.annotations_fragment = AnnotationFragment(master, full_path)
        # hLeft = tk.DoubleVar(value = 0.2)  #left handle variable initialised to value 0.2
        # hRight = tk.DoubleVar(value = 0.85)  #right handle variable initialised to value 0.85
        # self.hSlider = RangeSliderH(master, [hLeft, hRight] , padX=10, Height=50, font_size=10, bgColor='#f0f0f0')

        self.arrange()

    def arrange(self):
        self.view_name_label.grid(row=0, column=0, sticky=tk.N, pady=(10, 30), columnspan=3)

        self.user_id_label.grid(row=2, column=0)
        self.game_name_label.grid(row=2, column=2)
        self.datetime_label.grid(row=2, column=4)
        # self.device_name_label.grid(row=2, column=6)

        self.user_id_value_label.grid(row=4, column=0, padx=10)
        self.game_name_value_label.grid(row=4, column=2, padx=10)
        self.date_value_label.grid(row=4, column=4, padx=10)
        # self.device_name_value_label.grid(row=4, column=6, padx=10)

        self.pack(anchor=tk.CENTER)

        self.annotations_fragment.arrange()


    def destroy(self) -> None:
        try:
            self.annotations_fragment.destroy()
        except:
            print("Annotations not created")
        super().destroy()