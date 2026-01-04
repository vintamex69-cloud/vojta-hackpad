import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# -------------------------
# DIRECT-WIRED BUTTONS (9)
# -------------------------
keyboard.coord_mapping = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

keyboard.col_pins = (
    board.GP26, # SW1
    board.GP27, # SW2
    board.GP28, # SW3
    board.GP29, # SW4
    board.GP6, # SW5
    board.GP7, # SW6
    board.GP0, # SW7
    board.GP1, # SW8
    board.GP2, # SW9
)

keyboard.row_pins = ()
keyboard.diode_orientation = None

# -------------------------
# KEYMAP
# -------------------------
keyboard.keymap = [
    [
        KC.F13, KC.F14, KC.F15,
        KC.F16, KC.F17, KC.F18,
        KC.F19, KC.F20, KC.F21,
    ]
]

# -------------------------
# ROTARY ENCODER (NO SWITCH)
# -------------------------
encoder = EncoderHandler()
encoder.pins = ((board.GP3, board.GP4),) # A, B
encoder.map = [
    ((KC.VOLD, KC.VOLU),)
]

keyboard.modules.append(encoder)

# -------------------------
# START KEYBOARD
# -------------------------
if __name__ == '__main__':
    keyboard.go()