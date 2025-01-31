"""
CircuitPython Intro Tutorials - Module 8: Web Dashboard (Final Project)

This is our final project! We'll create a web server that shows a dashboard
of our sensor readings. This combines everything we've learned about:
- Sensors (temperature)
- Displays (showing status)
- Networking (serving a webpage)
- Variables and loops
"""

import board
import microcontroller
import wifi
import socketpool
import time
import ssl
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_ssd1306 import SSD1306_I2C
import adafruit_requests

# WiFi credentials - change these!
WIFI_SSID = "YOUR_WIFI_NAME"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# Set up the display
displayio.release_displays()
i2c = board.I2C()
display = SSD1306_I2C(128, 32, i2c)

# Create display labels
status_label = label.Label(terminalio.FONT, text="Starting...", x=0, y=15)
group = displayio.Group()
group.append(status_label)
display.show(group)

# HTML template for our webpage
HTML = """<!DOCTYPE html>
<html>
  <head>
    <title>CircuitPython Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      body { font-family: Arial; margin: 0 auto; max-width: 800px; padding: 20px; }
      .card { background: #f0f0f0; border-radius: 10px; padding: 20px; margin: 10px 0; }
      .temp { font-size: 48px; }
      .refresh { background: #4CAF50; color: white; padding: 10px 20px; 
                border: none; border-radius: 5px; cursor: pointer; }
    </style>
  </head>
  <body>
    <h1>CircuitPython Sensor Dashboard</h1>
    <div class="card">
      <h2>Temperature</h2>
      <div class="temp">TEMPERATURE_C°C</div>
      <div>(TEMPERATURE_F°F)</div>
    </div>
    <p>Last updated: TIMESTAMP</p>
    <button class="refresh" onclick="location.reload()">Refresh Data</button>
  </body>
</html>
"""

# Connect to WiFi
print("Connecting to WiFi...")
status_label.text = "Connecting..."
wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)

print(f"Connected to WiFi! IP: {wifi.radio.ipv4_address}")
status_label.text = f"IP: {wifi.radio.ipv4_address}"

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

def get_temperature():
    """Get formatted temperature strings"""
    temp_c = microcontroller.cpu.temperature
    temp_f = (temp_c * 9/5) + 32
    return f"{temp_c:.1f}", f"{temp_f:.1f}"

def webpage():
    """Create the webpage with current readings"""
    temp_c, temp_f = get_temperature()
    return HTML.replace("TEMPERATURE_C", temp_c)\
              .replace("TEMPERATURE_F", temp_f)\
              .replace("TIMESTAMP", time.monotonic())


"""
CircuitPython Intro Tutorials - Module 7: Basic Networking

In this lesson, we'll learn how to create a server on a WiFi network and send data over the network to any device that connects.
We'll create a simple program that serves the home page, the temperature of the MCU, or infrared pulses depending on the endpoint we connect to! 
"""

import board
import microcontroller
import wifi
import socketpool
import time
from adafruit_httpserver import Server, Request

AP_SSID = "IR Receiver"
AP_PASSWORD = "hacktheplanet"

print("Creating access point...")
wifi.radio.start_ap(ssid=AP_SSID, password=AP_PASSWORD)
pool = socketpool.SocketPool(wifi.radio)

# Our server folder is the /static folder on our MCU, but we're not using it this time!
server = Server(pool, "/static", debug=True)


# Here we create a 'route', a route is a simple way to attach a function to an URL endpoint. 
# For example, something like 192.168.4.1/temperature would activate the get_temperature() function and return the MCU's temperature.
@server.route("/")
def base(request: Request):
    message = """
    Hello from the CircuitPython HTTP Server!
        1. /temperature
        2. /readIR
        3. /???
    """
    return Response(request, message)

@server.route("/temperature")
def get_sensor_data(request: Request):
    temp_c = microcontroller.cpu.temperature
    temp_f = (temp_c * 9/5) + 32

    temp_response = {
        "temperature_c": f"{temp_c:.1f}",
        "temperature_f": f"{temp_f:.1f}"
    }
    return Response(request, str(temp_response))

@server.route("/readIR")
def get_IR_data(request: Request):
    pulses = decoder.read_pulses(pulsein)
    print("Heard", len(pulses), "Pulses: ", pulses)
    print("-----------------------")
    if pulses:
        return Response(request, str(pulses))
    else:
        return Response(request, "Error: Pulses not read!")

@server.route("/secrets")
def easter_egg(request: Request):
    page = """Try putting this in the golden machine: NZVAIYEKT"""
    return Response(request, page)


    

print(f"Created access point {AP_SSID} with page hosted @ {wifi.radio.ipv4_address_ap}")
server.serve_forever(str(wifi.radio.ipv4_address_ap))

# Start the web server
socket = pool.socket()
socket.bind(['0.0.0.0', 80])
socket.listen(1)

print("Web server started!")
status_label.text = "Server running!"

while True:
    try:
        # Accept incoming connections
        conn, addr = socket.accept()
        print(f"Got a request from {addr}")
        
        # Read the request
        request = conn.recv(1024).decode()
        
        # Generate and send the response
        response = webpage()
        conn.send('HTTP/1.1 200 OK\r\n')
        conn.send('Content-Type: text/html\r\n')
        conn.send('Connection: close\r\n\r\n')
        conn.send(response)
        
        # Clean up
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")
        continue

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

Try this: Can you add more sensors to the dashboard? Or make the webpage
auto-refresh every few seconds? (Hint: look up "HTML meta refresh")
""" 
