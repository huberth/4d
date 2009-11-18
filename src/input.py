import pygame

last_frame = {}

# These constants represent translated inputs.
X_AXIS = 0          # l/r for the on-screen positional dimensions
Y_AXIS = 1          # u/d for same
Z_AXIS = 2          # l/r for the color dimensions, as seen in the HUD
W_AXIS = 3          # u/d for same
AXIS_SWITCH = 4     # a request to swap axes (may be ignored if one in progress)
PRIMARY_FIRE = 5    # primary weapon
SECONDARY_FIRE = 6  # secondary weapon
TERTIARY_FIRE = 7   # tertiary weapon

def _clear_last_frame():
    last_frame[X_AXIS] = 0
    last_frame[Y_AXIS] = 0
    last_frame[Z_AXIS] = 0
    last_frame[W_AXIS] = 0
    last_frame[AXIS_SWITCH] = 0
    last_frame[PRIMARY_FIRE] = 0
    last_frame[SECONDARY_FIRE] = 0
    last_frame[TERTIARY_FIRE] = 0

def read_input():
    """
    Reads input from the configured input sources, translating
    keypresses/analog input into game input, and then places that
    translated input into a global structure so that the game logic
    can read it.
    """

    _clear_last_frame()

    pygame.event.pump()

    # keypresses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  last_frame[X_AXIS] = -0.01
    if keys[pygame.K_RIGHT]: last_frame[X_AXIS] = 0.01
    if keys[pygame.K_UP]:    last_frame[Y_AXIS] = -0.01
    if keys[pygame.K_DOWN]:  last_frame[Y_AXIS] = 0.01
    if keys[pygame.K_a]:     last_frame[Z_AXIS] = -0.01
    if keys[pygame.K_d]:     last_frame[Z_AXIS] = 0.01
    if keys[pygame.K_w]:     last_frame[W_AXIS] = -0.01
    if keys[pygame.K_s]:     last_frame[W_AXIS] = 0.01
    if keys[pygame.K_SPACE]: last_frame[PRIMARY_FIRE] = 1
