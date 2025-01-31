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
from adafruit_httpserver import Server, Request, Response

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
        2. /insert_your_own_page_here
    """
    return Response(request, message)

@server.route("/temperature")
def get_sensor_data(request: Request):
    temp_c = microcontroller.cpu.temperature
    temp_f = (temp_c * 9/5) + 32

    temp_response = f"Celsius: {temp_c:.1f} Farenheit: {temp_f:.1f}"
    return Response(request, str(temp_response))

print(f"Created access point {AP_SSID} with page hosted @ {wifi.radio.ipv4_address_ap}")
server.serve_forever(str(wifi.radio.ipv4_address_ap))
