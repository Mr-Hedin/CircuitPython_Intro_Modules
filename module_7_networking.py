"""
CircuitPython Intro Tutorials - Module 7: Basic Networking

In this lesson, we'll learn how to connect to WiFi and send data over the network.
We'll create a simple program that connects to WiFi and sends temperature readings
to a test server.
"""

import board
import microcontroller
import wifi
import socketpool
import time
import ssl
import adafruit_requests

# WiFi credentials - you'll need to change these!
WIFI_SSID = "YOUR_WIFI_NAME"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# Test URL - this is a simple test service that accepts GET requests
URL = "https://httpbin.org/get"

print("Connecting to WiFi...")

# Connect to WiFi
wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)

print("Connected to WiFi!")
print(f"My IP address: {wifi.radio.ipv4_address}")

# Create a socket pool and requests session
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# Function to get sensor data
def get_sensor_data():
    temp_c = microcontroller.cpu.temperature
    temp_f = (temp_c * 9/5) + 32
    return {
        "temperature_c": f"{temp_c:.1f}",
        "temperature_f": f"{temp_f:.1f}"
    }

while True:
    try:
        # Get the current sensor readings
        data = get_sensor_data()
        
        print("\nSending data to server...")
        print(f"Temperature: {data['temperature_c']}°C")
        
        # Send the data to our test server
        response = requests.get(URL, params=data)
        
        # Print the response from the server
        print("Server response:")
        print(f"Status code: {response.status_code}")
        
        # Clean up
        response.close()
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Will retry in 10 seconds...")
    
    time.sleep(10)  # Wait 10 seconds before next reading

"""
Things we learned:
1. We can connect to WiFi networks
2. We can send data over the internet using HTTP requests
3. We need to handle network errors gracefully
4. We can send sensor data as parameters in our requests

Try this: Can you modify the program to send data to a different test URL?
(Hint: try using https://httpbin.org/post with a POST request instead of GET)

Important note: In a real project, never share your WiFi password! Keep it
in a separate secrets.py file that isn't shared with others.
""" 