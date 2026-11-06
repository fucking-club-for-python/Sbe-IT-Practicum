"""ボタンを押したときにLEDを1秒間隔で3回点滅"""

import RPi.GPIO as GPIO
import time

LED_PIN = 17  # GPIO17
BUTTON_PIN = 18  # GPIO18


def setup():
    print("-----setup-----")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 入力(ボタン)として設定


def loop():
    print("-----loop-----")
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # もしボタンが押されているなら
            # iをループ内で使わない場合は、「_」を変数名にすると美しい
            for _ in range(3):  # 三回繰り返す
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(1)
        else:  # ボタンが押されていないなら
            GPIO.output(LED_PIN, GPIO.LOW)


def destroy():
    print("-----destroy-----")
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
