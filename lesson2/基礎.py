"""ボタンを押している間だけLEDを点灯させる"""

import RPi.GPIO as GPIO

LED_PIN = 17  # LEDをGPIO17に
BUTTON_PIN = 18  # ボタンをGPIO18に


def setup():
    print("-----setup-----")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)  # 出力として設定
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 入力(ボタン)として設定


def loop():
    print("-----loop-----")
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # もしボタンが押されているなら
            GPIO.output(LED_PIN, GPIO.HIGH)  # LEDをオンに
        else:  # ボタンが押されていないなら
            GPIO.output(LED_PIN, GPIO.LOW)  # LEDをオンに


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
