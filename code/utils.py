import RPi.GPIO as GPIO
import time

# Set GPIO Mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for HC-SR04
TRIG = 23
ECHO = 24

# Set up GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    """
    Returns the measured distance from the ultrasonic sensor in cm.
    """
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    pulse_end = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound formula
    return round(distance, 2)

def cleanup_gpio():
    """
    Cleanup GPIO settings.
    """
    GPIO.cleanup()
