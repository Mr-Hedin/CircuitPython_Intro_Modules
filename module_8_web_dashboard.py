"""
CircuitPython Intro Tutorials - Module 8: Web Dashboard (Final Project)

This is our final project! We'll create a web server that shows a dashboard
of our sensor readings. This combines everything we've learned about:
- Sensors (temperature)
- Networking (serving a webpage)
- Variables
"""
import board
import microcontroller
import wifi
import socketpool
import time
import digitalio
from adafruit_httpserver import FileResponse, Response, Request, Server
# ssid is the network name
SSID = "My Web Dashboard SSID"
# create a secure password
password = "hacktheplanet"

green_pin = board.GP13
red_pin = board.GP14

green_led = digitalio.DigitalInOut(green_pin)
red_led = digitalio.DigitalInOut(red_pin)

green_led.direction = digitalio.Direction.OUTPUT
red_led.direction = digitalio.Direction.OUTPUT


print("Connecting...")
wifi.radio.start_ap(ssid=SSID, password=password)
pool = socketpool.SocketPool(wifi.radio)

# sets the '/static' folder to our server's default folder
server = Server(pool, "/static", debug=True)
count = 0


# Here we create a 'route', a route is a simple way to attach a function to an URL endpoint. 
# For example, something like 192.168.4.1/temperature would activate the red_page() function and return the MCU's temperature.
@server.route("/")
def base(request: Request):
    message = """
    Hello from the CircuitPython HTTP Server!
        1. /red
        2. /green
        3. /image
        4. /temperature
    """
    return Response(request, message)

@server.route("/red")
def red_page(request: Request):
    message = """
    Red LED is toggled!
    """
    
    # Turn on the LED
    
    
    return Response(request, str(message))

@server.route("/green")
def green_page(request: Request):
    message = """
    Green LED toggled!
    """

    # Turn on the LED
    
    
    return Response(request, str(message))

# If you want to display an image to your user
@server.route("/image")
def image_page(request: Request):
    return FileResponse(request, "image.jpg","/static")

print(f" Created access point {SSID} with page hosted @ {wifi.radio.ipv4_address_ap}")
server.serve_forever(str(wifi.radio.ipv4_address_ap))

"""
Congratulations! You've completed all the modules!
This final project combines everything you've learned:
1. Reading sensors
2. Using displays
3. Connecting to WiFi
4. Creating a web server
5. Generating HTML
6. Using variables and functions
7. Error handling

Try this: Can you add more sensors to the dashboard? 
Or make the webpage auto-refresh every few seconds? (Hint: look up "HTML meta refresh")
""" 
