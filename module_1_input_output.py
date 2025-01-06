"""
CircuitPython Intro Tutorials - Module 1: Basic Input and Output

In this lesson, we'll learn about inputs and outputs using a button and LED.
Think of it like this: 
- OUTPUT is when our board sends out a signal (like turning on an LED)
- INPUT is when our board receives a signal (like detecting a button press)
"""

import board
import digitalio
import time  # We need this to add delays

# Let's set up our LED (this is our OUTPUT)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Now let's set up a button (this is our INPUT)
# We'll use GP15 pin - but you can change this to match your setup
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # This makes the button work properly

# Main program: When button is pressed, LED turns on!
print("Press the button to turn on the LED!")

while True:
    # button.value is False when pressed (because of Pull.UP)
    if not button.value:  # If button is pressed...
        led.value = True  # Turn LED on
    else:
        led.value = False  # Turn LED off
    
    # Add a tiny delay to make the program run smoothly
    time.sleep(0.01)

"""
Things we learned:
1. INPUT devices (like buttons) send signals TO our board
2. OUTPUT devices (like LEDs) receive signals FROM our board
3. We can use if/else to make decisions based on input
4. The program runs in a loop to constantly check the button

Try this: Can you modify the code to make the LED stay on for 1 second
when the button is pressed? (Hint: use time.sleep(1))
""" 