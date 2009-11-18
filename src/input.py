import pygame

last_frame = {}

# These constants represent game-relevant inputs.
UD_AXIS_XY = 0          # up/down for the on-screen positional dimensions
LR_AXIS_XY = 1          # left/right for same
UD_AXIS_ZW = 2          # up/down for the color dimensions, as seen in the HUD
LR_AXIS_ZW = 3          # left/right for same
AXIS_SWITCH = 4         # a request to swap axes (may be ignored if one in progress)
PRIMARY_FIRE = 5        # primary weapon
SECONDARY_FIRE = 6      # secondary weapon
TERTIARY_FIRE = 7       # tertiary weapon

def read_input():
    """
    Reads input from the configured input sources, translating
    keypresses/analog input into game input, and then places that
    translated input into a global structure so that the game logic
    can read it.

    Meta-inputs such as pausing are returned directly.
    """

    global last_frame

    pass
