"""
CircuitPython Intro Tutorials - Module 5: Basic Sensors

In this lesson, we'll learn how to read sensors! We'll use the built-in temperature
sensor that comes with many CircuitPython boards, and also read light levels.
"""

import board
import analogio  # For reading analog sensors
import microcontroller  # For the temperature sensor
import time

# Set up a light sensor on analog pin A0
light_sensor = analogio.AnalogIn(board.A0)

def get_voltage(pin):
    """Convert analog reading to voltage"""
    return (pin.value * 3.3) / 65536

def get_light_level():
    """Convert light sensor reading to percentage"""
    voltage = get_voltage(light_sensor)
    # Convert voltage to rough percentage (0-100)
    return int((voltage / 3.3) * 100)

print("Reading temperature and light levels...")
print("Cover the light sensor or shine a light on it to see values change!")

while True:
    # Read temperature (in Celsius)
    temp_c = microcontroller.cpu.temperature
    temp_f = (temp_c * 9/5) + 32  # Convert to Fahrenheit
    
    # Read light level
    light = get_light_level()
    
    # Print the readings
    print("----------------------------------------")
    print(f"Temperature: {temp_c:.1f}°C ({temp_f:.1f}°F)")
    print(f"Light Level: {light}%")
    
    # Create a simple bar graph for light level
    bars = "█" * (light // 5)  # One block for every 5%
    print(f"Light Graph: {bars}")
    
    time.sleep(1)  # Take readings every second

"""
Things we learned:
1. We can read the built-in temperature sensor
2. Analog pins can read varying voltage levels (0V to 3.3V)
3. We can convert sensor readings to more useful values
4. We can create simple visualizations of data

Try this: Can you make the program only print when there's a big change
in temperature or light level? (Hint: save the last reading in a variable
and compare it to the new reading)
""" 