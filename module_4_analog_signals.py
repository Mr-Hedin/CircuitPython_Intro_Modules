"""
CircuitPython Intro Tutorials - Module 4: Analog Signals

In this lesson, we'll learn about analog signals - these are signals that can vary,
not just be on or off. We'll use this to make an LED fade in and out!
"""

import board
import pwmio  # PWM lets us control brightness
import time

# Instead of digitalio, we use pwmio for varying brightness
led = pwmio.PWMOut(board.LED, frequency=5000, duty_cycle=0)

# Create some helper functions to convert percentages to PWM values
def percent_to_pwm(percent):
    """Convert a percentage (0-100) to PWM duty cycle (0-65535)"""
    return int((percent * 65535) / 100)

print("Watch the LED fade in and out!")

while True:
    # Fade LED in (get brighter)
    print("Fading in...")
    for brightness in range(0, 101, 2):  # 0% to 100% in steps of 2
        led.duty_cycle = percent_to_pwm(brightness)
        time.sleep(0.02)
    
    time.sleep(0.5)  # Pause at full brightness
    
    # Fade LED out (get dimmer)
    print("Fading out...")
    for brightness in range(100, -1, -2):  # 100% to 0% in steps of 2
        led.duty_cycle = percent_to_pwm(brightness)
        time.sleep(0.02)
    
    time.sleep(0.5)  # Pause at zero brightness

"""
Things we learned:
1. Analog signals can have many values (not just on/off)
2. PWM (Pulse Width Modulation) lets us control LED brightness
3. We can convert between percentages (0-100) and PWM values (0-65535)
4. We can use range() with different step sizes and directions

Try this: Can you make the LED fade in quickly but fade out slowly?
(Hint: change the time.sleep() values in the fade loops)
""" 