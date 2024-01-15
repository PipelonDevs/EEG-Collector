import time
from tkinter import ttk, messagebox
import tkinter as tk
from program_state import program_state
from utils.udpStreaming import listen_udp
import threading
from datetime import datetime
import os

from consts import GAME_DATASET_PATH, BASE_DATASET_PATH

class GameView(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.user_id_label = ttk.Label(self, text=f"User ID: {program_state.user_id}")
        self.game_label = ttk.Label(self, text=f"Game: {program_state.played_game}")

        self.record_button = ttk.Button(self, text="Start recording",  style="TButton", command=self.start_recording)
        self.arrange()


    def arrange(self):
        self.style = ttk.Style()
        self.style.configure("TButton", foreground='green')
    
        self.user_id_label.grid(row=0, column=0, sticky=tk.W)
        self.game_label.grid(row=1, column=0, sticky=tk.W)
        self.record_button.grid(row=2, column=0, sticky=tk.W)

        self.pack(anchor=tk.CENTER)

    def create_dir(self, dir_name):
        path = os.path.join(BASE_DATASET_PATH, GAME_DATASET_PATH, dir_name)
        os.makedirs(path, exist_ok=True)
        return path

    def start_recording(self):
        self.started_at = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"{program_state.user_id}_{program_state.played_game}_{self.started_at}"
        dirname = self.create_dir(dir_name=filename[:filename.rfind("_")]) # remove _HH:MM from directory name

        print('filename: ', filename)
        self.style.configure("TButton", foreground='red')
        self.record_button.configure(text="Stop recording", command=self.ask_stop_recording)
        
        self.recording_thread = threading.Thread(target=listen_udp, args=(dirname, filename))
        program_state.recording_on = True
        self.recording_thread.start()

    def ask_stop_recording(self):
        if messagebox.askokcancel("Stop recording", "Do you want to stop recording?"):
            self.stop_recording()


    def stop_recording(self):
        program_state.recording_on = False
        self.style.configure("TButton", foreground='green')
        self.record_button.configure(text="Start recording", command=self.start_recording)
        self.recording_thread.join()
        duration = datetime.now() - datetime.strptime(self.started_at, "%Y-%m-%d_%H-%M")
        print("duration:", duration)
        # self.destroy()
        # program_state.current_view = MenuView(self.master)