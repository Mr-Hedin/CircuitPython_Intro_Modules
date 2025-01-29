"""
This test will initialize the display using displayio and draw a solid white
background and some text
"""
import time
import board
import displayio
import busio
from displayio import I2CDisplay as I2CDisplayBus
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

# Use for I2C
i2c = busio.I2C(board.GP21, board.GP20)  # uses board.SCL and board.SDA
display_bus = I2CDisplayBus(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 32
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Make the display group to hold all of our drawings
splash = displayio.Group()

# Set that group as the root group the screen displays
display.root_group = splash

# Create a canvas to draw on and define what colors we have available
bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(2)
color_palette[0] = 0xFFFFFF  # White
color_palette[1] = 0x000000  # Black

# Add the canvas to our grid of drawing
bg_sprite = displayio.TileGrid(bitmap, pixel_shader=color_palette, x=0, y=0)

# add the text to the background
splash.append(bg_sprite)

# Draw a label
text = "Mr. Hedin so cool"
text_area = label.Label(terminalio.FONT, text=text, color=color_palette[1], x=5, y=15)
splash.append(text_area)



# All of the above is boilerplate you can include and adjust as you see fit to create your own designs!
# In our while True loop we can modify the text_area.text to update the label we created
while True:
    text_area.text = "Mr. Hedin"
    time.sleep(1)
    text_area.text = "is so cool wow"
    time.sleep(1)
    new_word = "animated text, wow"
    for i in range(len(new_word)):
        text_area.text = new_word[0:i+1]
        #text_area.text = ""
        time.sleep(.2)
    time.sleep(1)
