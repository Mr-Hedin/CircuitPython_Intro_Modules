# This is a simple file to read the raw pulse lengths from an IR remote!
# You can reuse the array of pulses in a trasmitter script to duplicate just about any infrared remote.

import pulseio
import board
import adafruit_irremote

pulsein = pulseio.PulseIn(board.A0, maxlen = 120, idle_state = True)
decoder = adafruit_irremote.GenericDecode()

while True:
    pulses = decoder.read_pulses(pulsein)
    print("Heard", len(pulses), "Pulses: ", pulses)
    print("-----------------------")
