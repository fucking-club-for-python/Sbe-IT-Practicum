"""2個のボタンでを押すことで、5個のLEDを順方向・逆方向に流す"""

import RPi.GPIO as GPIO
import time

LED_PINS = [5, 6, 13, 19, 26]  # 光らせるLEDの順番にGPIO番号を書く
BTN_PIN1 = 20  # 順方向に流すボタン
BTN_PIN2 = 21  # 逆方向に流すボタン
INTERVAL = 0.1  # LED1個の光らせる間隔


def setup():
    print("-----setup-----")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PINS, GPIO.OUT, initial=GPIO.LOW)
    # ボタン1と2をまとめて(タプルにして)入力に設定
    GPIO.setup((BTN_PIN1, BTN_PIN2), GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop():
    print("-----loop-----")
    while True:
        if GPIO.input(BTN_PIN1) == GPIO.LOW:  # もしボタン1が押されているとき
            print("event: button1 (GPIO20)")
            for led in LED_PINS:  # LEDを一個ずつ順番に取り出す
                GPIO.output(led, GPIO.HIGH)  # 取り出したLEDをonに
                time.sleep(INTERVAL)  # 指定秒数待つ
                GPIO.output(led, GPIO.LOW)  # 取り出したLEDをoffに

        elif GPIO.input(BTN_PIN2) == GPIO.LOW:  # もしボタン2が押されているとき
            print("event: button2 (GPIO21)")
            for led in reversed(LED_PINS):  # LEDを一個ずつ逆順に取り出す
                GPIO.output(led, GPIO.HIGH)
                time.sleep(INTERVAL)
                GPIO.output(led, GPIO.LOW)

        else:  # 両方のボタンが押されてないとき
            GPIO.output(LED_PINS, GPIO.LOW)


def destroy():
    print("-----destroy-----")
    GPIO.output(LED_PINS, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
