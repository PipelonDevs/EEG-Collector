from tkinter import ttk
import tkinter as tk

from program_state import program_state

class TetrisExperiment(tk.Frame):
    def __init__(self, phase_name, time):
        super().__init__(master=program_state.master)
        self.phase_name = phase_name
        self.time = time

        self.user_id_label = ttk.Label(self, text=f"User ID: {program_state.user_id}")
        self.phase_label = ttk.Label(self, text=f"Phase {phase_name}")
        self.time_label = ttk.Label(self, text=f"Time to the phase end: {self.time}")

        self.arrange()

        self.show_time()


    def show_time(self):
        if self.time == 0:
            self.destroy()
            program_state.current_view = next(program_state.phases_iterator)()
            return
        
        self.time_label.configure(text=f"Time: {self.time} s")
        self.time -= 1
        self.after(1000, self.show_time)

    def arrange(self):
        self.user_id_label.grid(row=0, column=0, sticky=tk.W)
        self.phase_label.grid(row=1, column=0, sticky=tk.W)
        self.time_label.grid(row=1, column=1, sticky=tk.W)
        self.pack(anchor=tk.CENTER)

