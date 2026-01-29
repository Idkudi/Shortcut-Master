import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

# Keyboard Definition
keyboard = KMKKeyboard()

# Add modules
encoder_handler = EncoderHandler()
layers = Layers()
keyboard.modules = [encoder_handler, layers]

# Pin Configuration for XIAO RP2040 based on schematic
# Matrix: 3 rows x 2 columns = 6 keys
# 
# ROW0 = D6 (GPIO28)
# ROW1 = D7 (GPIO29)  
# ROW2 = D10 (GPIO3)
# 
# COL0 and COL1 need to be determined from RotarySwitch connections
# Assuming standard GPIO pins for columns

keyboard.row_pins = (board.D6, board.D7, board.D10)
keyboard.col_pins = (board.D26, board.D27)  # ANPASSEN! Diese Pins basierend auf RotarySwitch verdrahtung

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB LED Configuration
# SK6812MINI LEDs connected in series
# LED_SIG pin needs to be identified from schematic
rgb = RGB(
    pixel_pin=board.D1,  # ANPASSEN! Check welcher Pin für LED_SIG verwendet wird
    num_pixels=6,
    hue_default=100,
    sat_default=100,
    val_default=30,  # Niedrigere Helligkeit um Augen zu schonen
    animation_mode='static_rainbow',
    val_limit=100,
    hue_step=5,
    sat_step=5,
    val_step=5,
    animation_speed=1,
)
keyboard.extensions.append(rgb)

# Rotary Encoder Configuration
# Based on schematic: RotaryEncoder_Switch with Pin1 (GND) and Pin2
encoder_handler.pins = (
    # (pin_a, pin_b, pin_button, is_inverted)
    (board.D8, board.D9, board.D4, False),  # ANPASSEN! Basierend auf tatsächlicher Verdrahtung
)

# Keymap Definition
# Physical layout:
#   SW0  SW2  SW4
#   SW1  SW3  SW5
#
# Matrix layout:
#   [0,0] [0,1]
#   [1,0] [1,1]
#   [2,0] [2,1]

keyboard.keymap = [
    # Layer 0 - Media Controls
    [
        KC.MEDIA_PREV_TRACK,    KC.MEDIA_NEXT_TRACK,    # Row 0
        KC.MEDIA_VOLUME_DOWN,   KC.MEDIA_VOLUME_UP,     # Row 1
        KC.MEDIA_PLAY_PAUSE,    KC.MEDIA_MUTE,          # Row 2
    ],
    
    # Layer 1 - Function Keys (via encoder press)
    [
        KC.F13, KC.F14,  # Row 0
        KC.F15, KC.F16,  # Row 1
        KC.F17, KC.F18,  # Row 2
    ],
    
    # Layer 2 - Numpad
    [
        KC.N7, KC.N8,  # Row 0
        KC.N4, KC.N5,  # Row 1
        KC.N1, KC.N2,  # Row 2
    ],
    
    # Layer 3 - RGB Controls
    [
        KC.RGB_TOG,  KC.RGB_MODE_FORWARD,   # Toggle / Next Mode
        KC.RGB_HUI,  KC.RGB_HUD,            # Hue +/-
        KC.RGB_SAI,  KC.RGB_SAD,            # Saturation +/-
    ],
]

# Encoder Mapping
# Format: ((clockwise, counter_clockwise, button_press),)
encoder_handler.map = [
    # Layer 0 - Volume Control
    ((KC.VOLU, KC.VOLD, KC.MO(1)),),
    
    # Layer 1 - Mouse Scroll
    ((KC.MS_WH_UP, KC.MS_WH_DOWN, KC.TO(2)),),
    
    # Layer 2 - Arrow Keys
    ((KC.UP, KC.DOWN, KC.TO(3)),),
    
    # Layer 3 - RGB Brightness
    ((KC.RGB_VAI, KC.RGB_VAD, KC.TO(0)),),
]

# Debugging
print("XIAO RP2040 Macropad initialized")
print("Layers:", len(keyboard.keymap))
print("Keys per layer:", len(keyboard.keymap[0]))

if __name__ == '__main__':
    keyboard.go()
