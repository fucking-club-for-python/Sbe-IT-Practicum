"""流れるLED"""

import time
import RPi.GPIO as GPIO

# GPIO17, GPIO13, GPIO26にLEDの+を接続
# 「応用1, 2回路図.jpg」を参照してください
LED_PINS = [17, 13, 26]
# 待機する秒数の変数
INTERVAL = 0.2


def setup():
    # GPIOxxのxxでピン番号を指定するモード
    GPIO.setmode(GPIO.BCM)
    # 使うLEDのGPIOをまとめて初期化、電圧はLOW(0.0V)
    GPIO.setup(LED_PINS, GPIO.OUT, initial=GPIO.LOW)


def loop():
    while True:
        # [:-1]は、端っこのLEDが二回点滅するのを収めるため
        for pin in LED_PINS[:-1]:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(INTERVAL)
            GPIO.output(pin, GPIO.LOW)

        # [::-1]で逆順に
        for pin in LED_PINS[::-1][:-1]:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(INTERVAL)
            GPIO.output(pin, GPIO.LOW)


def destroy():
    GPIO.output(LED_PINS, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
