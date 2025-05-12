# utils.py

import random

def get_distance():
    # Simulate ultrasonic distance (replace with actual sensor code if available)
    return round(random.uniform(30, 150), 2)  # in centimeters

def cleanup_gpio():
    print("GPIO cleanup done (dummy function)")
