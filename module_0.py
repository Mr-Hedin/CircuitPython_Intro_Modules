""" 
CircuitPython Intro Tutorials - Module 0

The first step to using any microcontroller is making sure it isn't broken!
Start with a simple "Hello World!" and a blink of the LED
"""

# First, import board and digitalio - they give us control over the pins on our microcontroller
import board
import digitalio
import time
# Print works just like Python!
print("Hello World!")

# Now, get the LED pin from our board
led = board.LED

# then, use digitalio to get the pin ready to be an output
led = digitalio.DigitalInOut(led)
led.direction = digitalio.Direction.OUTPUT

# finally, turn it on!
while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)


"""
Important things to remember:
1. Pins need to be set up to use them
2. import board gives us the pins
3. digitalio turns them into an input or output (electricity on/off)
"""
    

