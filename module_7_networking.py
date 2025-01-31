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
