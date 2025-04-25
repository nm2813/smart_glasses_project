import RPi.GPIO as GPIO
import time

# Set up GPIO pins for HC-SR04
TRIG = 23  # GPIO pin for Trigger
ECHO = 24  # GPIO pin for Echo

# Set GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    """
    Returns the distance measured by the ultrasonic sensor in cm.
    """
    GPIO.output(TRIG, False)
    time.sleep(2)  # Wait for sensor to settle

    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # Send a pulse
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    pulse_end = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound in cm
    return round(distance, 2)

def cleanup_gpio():
    """
    Cleans up GPIO settings after use.
    """
    GPIO.cleanup()
