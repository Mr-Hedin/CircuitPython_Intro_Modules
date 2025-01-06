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