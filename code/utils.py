import RPi.GPIO as GPIO
import time

# Pin configuration
TRIG = 23  # GPIO23 (Pin 16)
ECHO = 24  # GPIO24 (Pin 18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
time.sleep(2)  # Stabilize sensor

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10 microseconds
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # in cm

    return round(distance, 2)

def cleanup_gpio():
    GPIO.cleanup()