
import os
import tkinter as tk
import json
import time
from tkinter import ttk, messagebox
from consts import DEVICES_PATH
from program_state import program_state
from utils.paths import list_files
#     "meta": {
        # "device": "unicorn",
        # "unit_name": "unicorn e23",
        # "clock_rate": 250,
        # "channels": 8,
        # "displayable_rows": {
            # <channel_name>: [rows]

class ManageDevicesView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.view_name_label = ttk.Label(self, text="Manage Devices", font=("Helvetica", 24))
        
        self.your_devices_label = ttk.Label(self, text="Your devices: " )
        self.dropdown = ttk.Combobox(self, width=20, state="readonly")
        self.dropdown["values"] = list_files(DEVICES_PATH, "json")
        self.dropdown.bind("<<ComboboxSelected>>", self.on_select)

        self.manage_device_label = ttk.Label(self, text="Add New Device", font=("Helvetica", 16))

        self.device_name = tk.StringVar()
        self.device_label = ttk.Label(self, text="Device: ")
        self.device_entry = ttk.Entry(self, width=20, textvariable=self.device_name)

        self.unit_name = tk.StringVar()
        self.unit_label = ttk.Label(self, text="Unit name: ")
        self.unit_entry = ttk.Entry(self, width=20, textvariable=self.unit_name)

        self.clock_rate = tk.StringVar()
        self.clock_label = ttk.Label(self, text="Clock rate: ")
        self.clock_entry = ttk.Entry(self, width=20, textvariable=self.clock_rate)

        self.channels = tk.StringVar()
        self.channels_label = ttk.Label(self, text="Channels: ")
        self.channels_entry = ttk.Entry(self, width=20, textvariable=self.channels)

        # dispalyable_rows

        self.save_button = ttk.Button(self, text="Save", command=self.save)

        self.arrange()


    def arrange(self):
        self.view_name_label.grid(row=0, column=0, sticky=tk.W, pady=10)

        self.your_devices_label.grid(row=1, column=0, sticky=tk.W, pady=30)
        self.dropdown.grid(row=1, column=1, sticky=tk.W, pady=30)

        self.manage_device_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.device_label.grid(row=5, column=0, sticky=tk.W, pady=5)
        self.device_entry.grid(row=5, column=1, sticky=tk.W, pady=5)

        self.unit_label.grid(row=7, column=0, sticky=tk.W, pady=5)
        self.unit_entry.grid(row=7, column=1, sticky=tk.W, pady=5)

        self.clock_label.grid(row=9, column=0, sticky=tk.W, pady=5)
        self.clock_entry.grid(row=9, column=1, sticky=tk.W, pady=5)

        self.channels_label.grid(row=11, column=0, sticky=tk.W)
        self.channels_entry.grid(row=11, column=1, sticky=tk.W)

        self.save_button.grid(row=12, column=0, sticky=tk.W, pady=10)

        self.pack(anchor=tk.CENTER)

    def on_select(self, event):
        device_name = self.dropdown.get()
        path = os.path.join(DEVICES_PATH, device_name)
        with open(path, "r") as f:
            device = json.load(f)

        self.manage_device_label["text"] = f"Manage {device_name}"
        
        self.device_name.set(device["device"])
        self.unit_name.set(device["unit_name"])
        self.clock_rate.set(device["clock_rate"])
        self.channels.set(device["channels"])


    def save(self):
        device_name = self.device_name.get()
        unit_name = self.unit_name.get()
        clock_rate = self.clock_rate.get()
        channels = self.channels.get()

        if device_name == "" or unit_name == "" or clock_rate == "" or channels == "":
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            clock_rate = int(clock_rate)
            channels = int(channels)
        except ValueError:
            messagebox.showerror("Error", "Clock rate and channels must be integers.")
            return

        new_device = {
            "device": device_name,
            "unit_name": unit_name,
            "clock_rate": clock_rate,
            "channels": channels,
            "displayable_rows": {}
        }

        path = os.path.join(DEVICES_PATH, f"{device_name}.json")
        if os.path.exists(path):
            if not messagebox.askyesno("Warning", "Device already exists. Do you want to overwrite it?"):
                return
        
        with open(path, "w+") as f:
            json.dump(new_device, f, indent=4)

        messagebox.showinfo("Success", "Device saved.")
        
        self.clear_entries()
        self.dropdown.configure(values=list_files(DEVICES_PATH, ".json"))

    def clear_entries(self):
        self.manage_device_label["text"] = "Add New Device"
        self.dropdown.set("")

        self.device_name.set("")
        self.unit_name.set("")
        self.clock_rate.set("")
        self.channels.set("")