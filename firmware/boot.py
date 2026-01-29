import supervisor
import board
import digitalio
import storage

# Disable USB drive if not in bootloader mode
# This prevents accidental file modifications while the keyboard is running

# Optional: Use a key combination to enable USB drive
# For example, hold SW0 (first key) during boot to enable USB drive
try:
    key_pin = digitalio.DigitalInOut(board.D6)  # First row pin
    key_pin.direction = digitalio.Direction.INPUT
    key_pin.pull = digitalio.Pull.UP
    
    # If key is pressed (pulled low), enable USB drive
    if not key_pin.value:
        storage.remount("/", readonly=False)
        print("USB Drive enabled")
    else:
        storage.remount("/", readonly=True)
        print("USB Drive disabled - hold first key during boot to enable")
except Exception as e:
    print(f"Boot configuration error: {e}")
    # Default to read-only
    storage.remount("/", readonly=True)
