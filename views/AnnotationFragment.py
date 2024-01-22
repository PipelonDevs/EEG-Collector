import json
import time
from tkinter import ttk, messagebox, font
import tkinter as tk
from program_state import program_state
from RangeSlider.RangeSlider import RangeSliderH

from utils.dict_types import Annotations 



class AnnotationFragment(tk.Frame):
    def __init__(self, master, recording_path):
        super().__init__(master)
        self.recording_path = recording_path

        self.annotations = Annotations(**program_state.saving_strategy.pull(url=recording_path))

        self.new_annotation_button = ttk.Button(self, text="New annotation", command=self.new_annotation)

        # self.arrange()
        
    def arrange(self):

        self.new_annotation_button.grid(row=6, column=0, sticky=tk.W, pady=(30, 10))

        self.pack(anchor=tk.CENTER)

    def new_annotation(self):
        ...

        