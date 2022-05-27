import board
import neopixel
import digitalio

import picoledrace
import picoledreaction

output_signal = digitalio.DigitalInOut(board.GP7)
output_signal.direction = digitalio.Direction.OUTPUT
output_signal.value = False

signal_listener = digitalio.DigitalInOut(board.GP8)
signal_listener.direction = digitalio.Direction.INPUT
signal_listener.pull = digitalio.Pull.UP

if signal_listener.value:
    picoledrace.setup_and_standby()
else:
    picoledreaction.setup_and_standby()

