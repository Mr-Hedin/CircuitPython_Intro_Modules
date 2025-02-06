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
# create a folder named static on your circuitpy drive to easily serve images and web pages!
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
        4. /infrared
    """
    return Response(request, message)

@server.route("/red")
def red_page(request: Request):
    message = """
    Red LED is toggled!
    """
    
    # Turn on the LED
    if red_led.value == True:
      red_led.value = False
    else:
      red_led.value = True
    
    return Response(request, str(message))

@server.route("/green")
def green_page(request: Request):
    message = """
    Green LED toggled!
    """

    # Turn on the LED
    if green_led.value == True:
      green_led.value = False
    else:
      green_led.value = True
    
    return Response(request, str(message))


### IMAGES
# If you want to display an image to your user
# First, make sure your circuitpy drive has a 'static' folder.
# Open the static folder. Then, inside of the static folder, save your image file as "image". 
# your image should be a .jpg (.jpeg is fine) or .png!
# Once your image is saved it should be accessible at ip.address:5000/image.jpg!

@server.route("/image")
def image_page(request: Request):
    return FileResponse(request, "image.jpg","/static")


# Try creating some useful web pages that display data from the sensors we've used in class or output signals to devices like the infrared remote!

### INFRARED REMOTE
@server.route("/infrared")
def power_send(request: Request):
    # You'll need to use this code to initialize the IR!
    # Place it at the top of your file if you want the infrared remote on your server!
    # import board
    # import pulseio
    # import pwmio
    # import array
    # IR_OUT = board.A0
    # pulseOut = pulseio.PulseOut(IR_OUT)
    # This variable contains the delays between infrared light pulses
    # Each number is a number of microseconds!
    PowerPulse = [8984, 4468, 590, 1661, 590, 1662, 589, 538, 589, 539, 589, 538, 
              589, 538, 589, 539, 589, 1662, 589, 1663, 588, 539, 589, 1662, 
              589, 539, 588, 1663, 588, 540, 587, 1664, 588, 540, 587, 540, 587,
              540, 588, 540, 587, 540, 587, 1664, 587, 541, 586, 541, 587, 1665,
              586, 1665, 586, 1665, 586, 1665, 586, 1666, 585, 542, 585, 1666,
              585, 1666, 585, 543, 584]
    # This line does some encoding magic to make the pulses readable! 
    code = array.array('H', [PowerPulse[x] for x in range(len(PowerPulse))])
    # Finally, we send the encoded pulses through our LED:
    pulseOut.send(code)

    # Let the user know that their request was successfully served!
    message = "Power signal sent! Request Success!"
    return Response(request, message)

# PHOTORESISTOR
@server.route("/lightlevel")
def get_light_level(request:Request):
    # You'll need the following code to get your analog sensor set up!
    # import board
    # import analogio
    # light_sensor = analogio.AnalogIn(board.A0)
    """Convert light sensor reading to percentage"""
    voltage = (light_sensor.value * 3.3) / 65536
    # Convert voltage to rough percentage (0-100)
    light_level = int((voltage / 3.3) * 100)
    # Finally, create our response message with the actual light level included!
    message = "Current light level is: " + str(light_level)
    return Response(request, message)
    





print(f" Created access point {SSID} with page hosted @ {wifi.radio.ipv4_address_ap}")
server.serve_forever(str(wifi.radio.ipv4_address_ap))
