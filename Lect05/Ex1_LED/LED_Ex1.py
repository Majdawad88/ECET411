import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use physical pin numbering
LED = 21
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)   # Set pin 21 to be an output pin and set initial value to low (off)

while True: # Run forever
        GPIO.output(LED, GPIO.HIGH) # Turn on
        print('LED ON')
        sleep(1)                  # Sleep for 1 second
        GPIO.output(LED, GPIO.LOW)  # Turn off
        print('LED OFF')
        sleep(1)                  # Sleep for 1 second
