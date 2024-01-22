import time
from tkinter import ttk, messagebox
import tkinter as tk
from program_state import program_state
from utils.dict_types import Annotations, Device, Meta
from utils.paths import list_files
from utils.udpStreaming import listen_udp
import threading
from datetime import datetime
import os

from consts import DEVICES_PATH, GAME_DATASET_PATH, BASE_DATASET_PATH
from views.AnnotationFragment import AnnotationFragment

class GameView(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.style = ttk.Style()

        self.view_name_label = ttk.Label(self, text="Collect Data", font=("Helvetica", 24))
        self.description_label = ttk.Label(self, text="Fil the meta data and start collecting the data from a device.", font=("Helvetica", 12))

        self.user_id = tk.StringVar()
        self.user_id_label = ttk.Label(self, text="User ID: ")
        self.user_id_entry = ttk.Entry(self, width=20, textvariable=self.user_id)

        self.game_name = tk.StringVar()
        self.game_label = ttk.Label(self, text="Game: ")
        self.game_entry = ttk.Entry(self, width=20, textvariable=self.game_name)

        self.device_label = ttk.Label(self, text="Device: ")
        self.devices_dropdown = ttk.Combobox(self, width=20, state="readonly")
        self.devices_dropdown["values"] = list_files(DEVICES_PATH, "json")

        self.notes = tk.StringVar()
        self.notes_label = ttk.Label(self, text="Notes: ")
        self.notes_entry = ttk.Entry(self, width=20, textvariable=self.notes)

        self.record_button = ttk.Button(self, text="Start recording",  style="TButton", command=self.start_recording)
        program_state.recording_on = False
        self.arrange()

    def on_destroy(self):
        if program_state.recording_on:
            if not self.ask_stop_recording():
                return
        self.destroy()
        

    def arrange(self):
        self.view_name_label.grid(row=0, column=0, sticky=tk.W, pady=10)
        self.description_label.grid(row=1, column=0, columnspan=2, sticky=tk.N, pady=(10, 30))

        self.user_id_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.user_id_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        self.game_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.game_entry.grid(row=3, column=1, sticky=tk.W, pady=5)

        self.device_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.devices_dropdown.grid(row=4, column=1, sticky=tk.W, pady=10)

        self.notes_label.grid(row=5, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.record_button.grid(row=5, column=0, sticky=tk.W, pady=10)

        self.pack(anchor=tk.CENTER)

    def is_valid_meta_data(self):
        if not self.user_id.get() or not self.game_name.get() or not self.devices_dropdown.get():
            messagebox.showerror("Error", "Please fill in all the fields.")
            return False

        invalid_chars = ["*", "_", "|", ":", "\"", "<", ">", "?", "/"]
        if any(char in self.user_id.get() for char in invalid_chars):
            messagebox.showerror("Error", f"User ID cannot contain the following characters: {invalid_chars}")
            return False

        if any(char in self.game_name.get() for char in invalid_chars):
            messagebox.showerror("Error", f"Game name cannot contain the following characters: {invalid_chars}")
            return False
        
        return True

    def create_dir(self, dir_name):
        path = os.path.join(BASE_DATASET_PATH, GAME_DATASET_PATH, dir_name)
        return path

    def disable_entries(self):
        self.user_id_entry.configure(state="disabled")
        self.game_entry.configure(state="disabled")
        self.devices_dropdown.configure(state="disabled")

    def enable_entries(self):
        self.user_id_entry.configure(state="normal")
        self.game_entry.configure(state="normal")
        self.devices_dropdown.configure(state="normal")

        self.user_id.set("")
        self.game_name.set("")
        self.devices_dropdown.set("")

    def start_recording(self):
        if not self.is_valid_meta_data():
            return

        self.disable_entries()

        program_state.user_id = self.user_id.get()
        program_state.played_game = self.game_name.get()

        self.device_path = os.path.join(DEVICES_PATH, self.devices_dropdown.get())
        # program_state.device = self.devices_dropdown.get()
        self.annotations = Annotations(
            meta = Meta(
                device=Device(
                    **program_state.saving_strategy.pull(url=self.device_path)
                ),
                notes= self.notes.get()
            ),
            data=[]
        )

        self.started_at = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"{program_state.user_id}_{program_state.played_game}_{self.started_at}"
        dirname = self.create_dir(dir_name=filename[:filename.rfind("_")]) # remove _HH:MM from directory name

        self.style.configure("TButton", foreground='red')
        self.record_button.configure(text="Stop recording", command=self.ask_stop_recording)

        os.makedirs(dirname, exist_ok=True)
        full_path = os.path.join(dirname, filename)

        program_state.saving_strategy.push(data=self.annotations, url=f"{full_path}.json")
        self.annotations_fragment = AnnotationFragment(self.master, f"{full_path}.json")
        self.annotations_fragment.arrange()

        self.recording_thread = threading.Thread(target=listen_udp, args=(full_path,))
        program_state.recording_on = True
        self.recording_thread.start()

    def ask_stop_recording(self):
        if messagebox.askokcancel("Stop recording", "Do you want to stop recording?"):
            self.stop_recording()
            return True
        return False


    def stop_recording(self):
        self.style.configure("TButton", foreground='green')
        program_state.recording_on = False
        self.enable_entries()
        
        self.record_button.configure(text="Start recording", command=self.start_recording)
        self.recording_thread.join()

        duration = datetime.now() - datetime.strptime(self.started_at, "%Y-%m-%d_%H-%M")
        messagebox.showinfo("Success", f"Recording stopped. Duration: {duration}")


    def destroy(self) -> None:
        try:
            self.annotations_fragment.destroy()
        except:
            print("Annotations not created")
        super().destroy()
