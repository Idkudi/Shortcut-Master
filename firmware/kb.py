import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB
from kmk.modules.encoder import EncoderHandler

# Keyboard Definition
keyboard = KMKKeyboard()

# Pin Configuration for XIAO RP2040
# Rows: D6, D7, D10
# Cols: Via Rotary Encoder switches (need to map actual pins)
keyboard.col_pins = (board.D0, board.D1)  # Anpassen basierend auf tatsächlicher Verdrahtung
keyboard.row_pins = (board.D6, board.D7, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB LED Configuration (SK6812MINI)
rgb = RGB(
    pixel_pin=board.D3,  # LED_SIG Pin - bitte anpassen falls anders
    num_pixels=6,
    hue_default=100,
    sat_default=100,
    val_default=50,
    animation_mode='rainbow',
)
keyboard.extensions.append(rgb)

# Rotary Encoder Configuration
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Encoder: Pin1 (A), Pin2 (B) - bitte anpassen
encoder_handler.pins = (
    (board.D8, board.D9, board.D4),  # (Pin A, Pin B, Button Pin)
)

# Keymap
# Layout:
# [0] [1]
# [2] [3]
# [4] [5]

keyboard.keymap = [
    # Layer 0 (Default)
    [
        KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK,  # Row 0
        KC.MEDIA_VOLUME_DOWN, KC.MEDIA_VOLUME_UP,  # Row 1
        KC.MEDIA_PLAY_PAUSE, KC.MEDIA_MUTE,         # Row 2
    ],
    # Layer 1 (Function Layer - via Encoder button hold)
    [
        KC.N1, KC.N2,
        KC.N3, KC.N4,
        KC.N5, KC.N6,
    ],
]

# Encoder Map
# Rotation: Volume Up/Down
# Button: Layer toggle
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MO(1)),),  # (CW, CCW, Press)
]

if __name__ == '__main__':
    keyboard.go()
