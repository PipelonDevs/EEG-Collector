
from tkinter import ttk
import tkinter as tk
from multiprocessing import Process
import threading
import time
from utils.udpStreaming import listen_udp
from .TetrisExperiment import TetrisExperiment


class GamePhase(TetrisExperiment):
    def __init__(self, phase_name, time, game):
        super().__init__(phase_name, time)

        self.game = game
        self.game_process = Process(target=game,  daemon=True)
        self.game_process.start()

    def show_time(self):
        print("inside kiddo")
        if self.time == 0:
            # pygame.quit()
            self.game_process.terminate()
            # sleep
            time.sleep(1)
        
        super().show_time()
        

