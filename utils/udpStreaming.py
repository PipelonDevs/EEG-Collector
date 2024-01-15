import socket
import os
import warnings

from utils.custom_printing import print_as_red
from utils.Timer import Timer
warnings.filterwarnings("ignore")

IP = "127.0.0.1"
PORT = 1000
TIMEOUT = 5 # in seconds

def listen_udp(filename, dirname="./Datasets/"):
    os.makedirs(os.path.dirname(dirname), exist_ok=True)
    file = open(os.path.join(dirname, f"{filename}.csv"), "wb+")

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
        while True:
            number_of_bytes_received, _ = udp_socket.recvfrom_into(receive_buffer_byte)
            # timer.print_stopwatch()
            if number_of_bytes_received > 0:
                message_byte = receive_buffer_byte[:number_of_bytes_received]
                file.write(message_byte)

    except Exception as ex:
        print_as_red(f"Error during UDP data acquisition: {ex}")
    finally:
        file.close()
        print("\nAcquisition has terminated. Press ENTER to continue.")
        input()



if __name__ == "__main__":
    listen_udp("test")
