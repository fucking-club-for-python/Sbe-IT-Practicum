"""LEDを点滅させるコード"""

import time
import RPi.GPIO as GPIO

LED_PIN = 17


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)
    print("using pin%d" % LED_PIN)


def loop():
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("...led on")
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        print("led off...")
        time.sleep(1)


def destroy():
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
