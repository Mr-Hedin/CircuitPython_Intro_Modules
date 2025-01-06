"""
CircuitPython Intro Tutorials - Module 6: Display and Text

In this lesson, we'll learn how to use a small OLED display to show text and
simple graphics. We'll combine this with our temperature sensor from Module 5!
"""

import board
import displayio
import terminalio
import microcontroller
import time
from adafruit_display_text import label
from adafruit_ssd1306 import SSD1306_I2C

# Set up the display (using common 128x32 OLED display)
displayio.release_displays()
i2c = board.I2C()  # uses board.SCL and board.SDA
display = SSD1306_I2C(128, 32, i2c)

# Create the text labels
title = label.Label(
    terminalio.FONT,
    text="Temperature Monitor",
    color=1,
    x=0,
    y=5
)

temp_label = label.Label(
    terminalio.FONT,
    text="Loading...",
    color=1,
    x=0,
    y=20
)

# Create a display group and add our labels
group = displayio.Group()
group.append(title)
group.append(temp_label)

# Show the group on the display
display.show(group)

print("Temperature monitor starting...")
print("Watch the OLED display!")

while True:
    # Get the temperature
    temp_c = microcontroller.cpu.temperature
    temp_f = (temp_c * 9/5) + 32
    
    # Update the temperature text
    temp_label.text = f"{temp_c:.1f}C / {temp_f:.1f}F"
    
    # Create a simple animation effect
    display.fill(0)  # Clear the display
    display.show(group)  # Show the updated text
    
    time.sleep(1)

"""
Things we learned:
1. We can use I2C to communicate with displays
2. Displays can show text and simple graphics
3. We can create and update text labels
4. We can organize display elements in groups

Try this: Can you add a third line to show if the temperature is
'Normal', 'High', or 'Low'? (Hint: create another label and use if/else
statements to set its text)
""" 