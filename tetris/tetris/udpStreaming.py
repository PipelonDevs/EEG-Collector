import asyncio
import socket
import numpy as np
import sklearn
import pickle
import warnings
warnings.filterwarnings("ignore")

async def main():
    print("Unicorn Frequency Band UDP Receiver Example")
    print("-------------------------------------------")
    print()
     # Create a file to store data.
    DataResultFile = "modelTest3_result.csv";
    DataFile = "modelTest3.csv";  
    file = open("../../Datasets/"+DataFile, "wb")
    resultFile = open("../../Datasets/"+DataResultFile,"w")

    boredom_classifier = pickle.load(open('../../SKLEARN/boredom_classifier002.sav', 'rb'))
    try:
             
        


        # Define an IP endpoint
        destination_port = 1000
        ip = "127.0.0.1"
        end_point = (ip, destination_port)
        print(f"Listening on port '{destination_port}'...")

        # Initialize UDP socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(end_point)
        receive_buffer_byte = bytearray(1024)

        # Acquisition loop
        while True:
            number_of_bytes_received, _ = udp_socket.recvfrom_into(receive_buffer_byte)
            if number_of_bytes_received > 0:
                message_byte = receive_buffer_byte[:number_of_bytes_received]
                message = message_byte.decode("ascii")

                np_data = np.array(message.split(',')).reshape(1, -1)
                result = boredom_classifier.predict(np_data[:,8:56])[0]
                print(result)
                resultFile.write(str(result)+" ")
                file.write(message_byte)
                yield result
                
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        print("Press ENTER to terminate the application.")
        file.close()
        resultFile.close()
        input()

async def run_main():
    async for result in main():
        print(result)

if __name__ == "__main__":
    asyncio.run(run_main())
