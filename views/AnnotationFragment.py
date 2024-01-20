import json
import time
from tkinter import ttk, messagebox
import tkinter as tk
from program_state import program_state
from RangeSlider.RangeSlider import RangeSliderH

from utils.Annotations import Annotations 



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
        .split("/")[-1] \
        .split(".")[0] \
        .split("_")
    return user_id, game_name, date, time


class AnnotationFragment(tk.Frame):
    def __init__(self, master, recording_path):
        super().__init__(master)
        self.recording_path = recording_path

        self.annotations = Annotations(recording_path)
        user_id, game_name, date, time = get_metadata_from_path(recording_path)

        self.user_id_label = ttk.Label(self, text=f"User ID: {user_id}")
        self.game_label = ttk.Label(self, text=f"Game: {game_name}")
        self.date_label = ttk.Label(self, text=f"Date: {date}")
        self.time_label = ttk.Label(self, text=f"Time: {time}")

        self.device_label = ttk.Label(self, text=f"Device: {self.annotations.meta.device}: {self.annotations.meta.unit_name}")
        self.new_annotation_button = ttk.Button(self, text="New annotation", command=self.new_annotation)

        self.arrange()
        
    def arrange(self):
        self.user_id_label.pack(anchor=tk.W)
        self.game_label.pack(anchor=tk.W)
        self.date_label.pack(anchor=tk.W)
        self.time_label.pack(anchor=tk.W)
        self.device_label.pack(anchor=tk.W)
        self.new_annotation_button.pack(anchor=tk.W)

        self.pack(anchor=tk.CENTER)

    def new_annotation(self):
        ...

        