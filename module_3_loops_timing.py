"""
CircuitPython Intro Tutorials - Module 3: Loops and Timing

In this lesson, we'll learn about different types of loops and how to control timing.
We'll make LED patterns that you might see on police cars or emergency vehicles!
"""

import board
import digitalio
import time

# Set up our LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def blink_pattern_1():
    """This is a function - it's a reusable chunk of code we can call later"""
    # Fast blink pattern
    for _ in range(3):  # Do this 3 times
        led.value = True
        time.sleep(0.1)  # Very short delay
        led.value = False
        time.sleep(0.1)

def blink_pattern_2():
    """A different pattern with varying delays"""
    # Slow, then fast pattern
    led.value = True
    time.sleep(0.5)  # Longer delay
    led.value = False
    time.sleep(0.2)
    led.value = True
    time.sleep(0.1)  # Short delay
    led.value = False
    time.sleep(0.2)

print("Watch the LED make different patterns!")
pattern_count = 0  # Keep track of which pattern we're on

while True:  # Main program loop
    # Pattern 1: Three quick blinks
    print("Pattern 1: Quick blinks")
    for _ in range(2):  # Repeat the pattern twice
        blink_pattern_1()
        time.sleep(0.5)  # Wait between repetitions
    
    time.sleep(1)  # Pause between patterns
    
    # Pattern 2: Long-short pattern
    print("Pattern 2: Long-short pattern")
    for _ in range(2):  # Repeat the pattern twice
        blink_pattern_2()
        time.sleep(0.5)  # Wait between repetitions
    
    time.sleep(1)  # Pause before starting over
    pattern_count += 1
    print(f"Completed {pattern_count} rounds of patterns")

"""
Things we learned:
1. We can use different types of loops:
   - while True: runs forever
   - for _ in range(3): runs a specific number of times
2. We can create functions to reuse code
3. Different sleep times create different patterns
4. We can combine loops to make complex patterns

Try this: Can you create your own pattern function and add it to the sequence?
(Hint: copy one of the existing patterns and change the timing)
""" 