import time
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter.filedialog import askopenfilename

from program_state import program_state
from .AnnotationFragment import AnnotationFragment

class AnnotationView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        master.withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename(initialdir="Datasets/GameDatasets", title="Select dataset to annotate", filetypes=(("csv files", "*.csv"), ("all files", "*.*"))) 
        master.deiconify() # make the root window appear again
        print(filename)
        
        self.annotations = AnnotationFragment(master, filename)
        # hLeft = tk.DoubleVar(value = 0.2)  #left handle variable initialised to value 0.2
        # hRight = tk.DoubleVar(value = 0.85)  #right handle variable initialised to value 0.85
        # self.hSlider = RangeSliderH(master, [hLeft, hRight] , padX=10, Height=50, font_size=10, bgColor='#f0f0f0')

        # self.annotations = AnnotationFragment(master, 'Datasets/GameDatasets/user123_league of legends_2024-01-15/user123_league of legends_2024-01-15_22-59.json')
        