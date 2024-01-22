import socket
import os
import warnings
from tkinter import messagebox

from program_state import program_state
warnings.filterwarnings("ignore")

IP = "127.0.0.1"
PORT = 1000
TIMEOUT = 5 # in seconds

def listen_udp(full_path):
    file = open(f"{full_path}.csv", "wb+")

    try:
        end_point = (IP, PORT)

        # Initialize UDP socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.settimeout(TIMEOUT)
        udp_socket.bind(end_point)
        receive_buffer_byte = bytearray(1024)

        print(f"Listening on {end_point}")
        # timer = Timer()

        # Acquisition loop
        while program_state.recording_on:
            number_of_bytes_received, _ = udp_socket.recvfrom_into(receive_buffer_byte)
            # timer.print_stopwatch()
            if number_of_bytes_received > 0:
                message_byte = receive_buffer_byte[:number_of_bytes_received]
                file.write(message_byte)

    except Exception as ex:
        messagebox.showerror("Error", f"Error during UDP data acquisition: {ex}")
    finally:
        file.close()
        print("\nAcquisition has terminated")



if __name__ == "__main__":
    listen_udp("test")
