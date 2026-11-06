"""3つのLEDを、順番に点灯・消灯させるコード"""

import time
import RPi.GPIO as GPIO

# GPIO17, GPIO13, GPIO26にLEDの+を接続
# 「応用1, 2回路図.jpg」を参照してください
LED_PINS = [17, 13, 26]


def setup():
    # GPIOxxのxxでピン番号を指定するモード
    GPIO.setmode(GPIO.BCM)
    # 使うLEDのGPIOをまとめて初期化、電圧はLOW(0.0V)
    GPIO.setup(LED_PINS, GPIO.OUT, initial=GPIO.LOW)


def loop():
    while True:
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(1)

        # [::-1]で逆順に
        for pin in LED_PINS[::-1]:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(1)


def destroy():
    GPIO.output(LED_PINS, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
