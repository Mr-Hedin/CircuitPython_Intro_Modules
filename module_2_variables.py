"""
CircuitPython Intro Tutorials - Module 2: Variables and Counting

In this lesson, we'll learn about variables - they're like containers that can hold different types of information.
We'll use them to count how many times a button is pressed!
"""

import board
import digitalio
import time

# Set up our LED and button like in Module 1
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Create variables to store our numbers
button_presses = 0          # This is a number variable
was_button_pressed = False  # This is a True/False variable

print("Press the button! I'll count how many times you press it.")
print("Current count: 0")

while True:
    # Check if button is pressed
    if not button.value:  # Button is pressed
        if not was_button_pressed:  # Only count if this is a new press
            button_presses = button_presses + 1  # Add 1 to our count
            print(f"Current count: {button_presses}")  # f-strings let us put variables in text!
            
            # Make LED blink the number of times we've pressed
            for i in range(button_presses):  # Loop the number of times we've pressed
                led.value = True
                time.sleep(0.2)
                led.value = False
                time.sleep(0.2)
                
        was_button_pressed = True  # Remember the button is being held
    else:
        was_button_pressed = False  # Button was released
        
    time.sleep(0.01)  # Small delay to make everything run smoothly

"""
Things we learned:
1. Variables can store different types of information:
   - Numbers (like button_presses = 0)
   - True/False values (like was_button_pressed = False)
   - Text (like in our print statements)
2. We can do math with variables (button_presses + 1)
3. We can use variables to make decisions (if not was_button_pressed)
4. We can use variables in our print statements with f-strings

Try this: Can you modify the code to make the LED blink faster when you've
pressed the button more times? (Hint: try dividing the sleep time by button_presses)
""" 