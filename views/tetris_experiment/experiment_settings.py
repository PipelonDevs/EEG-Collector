from tkinter import ttk
import tkinter as tk
import threading
import time

from program_state import program_state
from .GamePhase import GamePhase
from tetris.tetris_boring.tetris import start_game 
# PHASES = [
#     {'phase_name': 'Phase 1 - Game', 'time': 7 * 60},
#     {'phase_name': 'Phase 1 - Rest', 'time': 2 * 60},
#     {'phase_name': 'Phase 1 - form', 'time': 2 * 60},

#     {'phase_name': 'Phase 2 - Game', 'time': 7 * 60},
#     {'phase_name': 'Phase 2 - Rest', 'time': 2 * 60},
#     {'phase_name': 'Phase 2 - form', 'time': 2 * 60},

#     {'phase_name': 'Phase 3 - Game', 'time': 7 * 60},
#     {'phase_name': 'Phase 3 - Rest', 'time': 2 * 60},
#     {'phase_name': 'Phase 3 - form', 'time': 2 * 60},
# ]

PHASES = [
    lambda: GamePhase('Phase 1 - Game', 1 * 15, start_game),
    lambda: GamePhase('Phase 2 - Game', 7 * 60, start_game),
]


phases_iterator = iter(PHASES)