"""
XIAO RP2040 Macropad - KMK Firmware
Main entry point for CircuitPython

This file imports and runs the keyboard configuration
"""

try:
    from kb import keyboard
    keyboard.go()
except Exception as e:
    print(f"Keyboard initialization error: {e}")
    # Keep USB serial alive for debugging
    import time
    while True:
        print("Error - check kb.py configuration")
        time.sleep(5)
