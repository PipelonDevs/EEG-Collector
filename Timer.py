import time

class Timer:
    def __init__(self):
        self.start_time = time.time()

    def get_stopwatch(self):
        hours, minutes = divmod(time.time() - self.start_time, 3600)
        minues, seconds = divmod(minutes, 60)
        return f"{int(hours)}:{int(minues):02d}:{int(seconds):02d}"
    
    def print_stopwatch(self):
        print(f"\r{self.get_stopwatch()}", end="")