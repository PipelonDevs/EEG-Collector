class __State:
    def __init__(self):
        # general
        self.master = None
        self.current_view = None
        self.user_id = None
        
        # options related
        ## game related
        self.played_game = None

        # tetris experiment related
        phases_iterator = None

        # time related
        self.start_time = None
        self.end_time = None
        self.stopwatch = None


program_state = __State()