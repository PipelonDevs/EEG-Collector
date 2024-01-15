import time
from tkinter import ttk
import tkinter as tk
from program_state import program_state
from utils.udpStreaming import listen_udp
import threading

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

    def start_recording(self):
        filename = f"{program_state.user_id}_{program_state.played_game}_{time.time()}.csv"
        self.style.configure("TButton", foreground='red')
        self.record_button.configure(text="Stop recording", command=self.stop_recording)
        
        self.recording_thread = threading.Thread(target=listen_udp, args=(filename,))
        self.recording_thread.start()

    def stop_recording(self):
        self.style.configure("TButton", foreground='green')
        self.record_button.configure(text="Start recording", command=self.start_recording)
        self.recording_thread.join()
        # self.destroy()
        # program_state.current_view = MenuView(self.master)