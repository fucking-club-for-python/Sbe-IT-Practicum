"""順方向 -> 逆方向にLEDを流す"""

import RPi.GPIO as GPIO
import time

# ピン番号(GPIO x)のリストの宣言
SPIMOSI = 10
SPIMISO = 9
SPISCLK = 11
EEDATA = 0
LED_PINS = [17, 27, 22, SPIMOSI, SPIMISO, SPISCLK, EEDATA, 5]

# LEDの発光する間隔
INTERVAL = 0.1


def setup():
    print("-----setup-----")
    GPIO.setmode(GPIO.BCM)
    # 全てのLEDをまとめて出力モード＋電圧LOW(0V)に設定
    GPIO.setup(LED_PINS, GPIO.OUT, initial=GPIO.LOW)


def loop():
    print("-----loop-----")
    while True:
        # [:-1]で一番最後のLEDを除く
        for pin in LED_PINS[:-1]:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(INTERVAL)
            GPIO.output(pin, GPIO.LOW)

        # [::-1]でLEDを逆順に
        for pin in LED_PINS[::-1][:-1]:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(INTERVAL)
            GPIO.output(pin, GPIO.LOW)


def destroy():
    print("-----destroy-----")
    # 全てのLEDをまとめて、電圧LOW(0V)に設定
    GPIO.output(LED_PINS, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass
    finally:
        destroy()
