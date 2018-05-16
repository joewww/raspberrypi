from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

LedPin = 11    # pin11

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output

setup()

@app.route("/")
def toggle():
    state = GPIO.input(LedPin)

    # turn led off if on, otherwise turn on
    GPIO.output(LedPin, GPIO.LOW) if state else GPIO.output(LedPin, GPIO.HIGH)

    return "toggle\n"

@app.route("/blink")
def blink():

    import time

    for i in range(0,10):
        GPIO.output(LedPin, GPIO.HIGH)  # led on
        time.sleep(0.2)
        GPIO.output(LedPin, GPIO.LOW)   # led off
        time.sleep(0.1)

    return "blink!\n"


import atexit

@atexit.register
def cleanup():
    GPIO.output(LedPin, GPIO.LOW)   # led off
    GPIO.cleanup()                  # release resource

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


