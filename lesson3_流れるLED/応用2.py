"""ボタンを押したときに、LEDを順方向に点灯 -> 順方向に消灯"""

import RPi.GPIO as GPIO
import time

# ピン番号(GPIO x)のリストの宣言
SPIMOSI = 10
SPIMISO = 9
SPISCLK = 11
EEDATA = 0
LED_PINS = [17, 27, 22, SPIMOSI, SPIMISO, SPISCLK, EEDATA, 5]

# ボタンのピン番号
BTN_PIN = 26
# LEDの発光する間隔
INTERVAL = 0.1


def setup():
    print("-----setup-----")
    GPIO.setmode(GPIO.BCM)
    # 全てのLEDをまとめて出力モード＋電圧LOW(0V)に設定
    GPIO.setup(LED_PINS, GPIO.OUT, initial=GPIO.LOW)
    # ボタンを入力モードに設定
    GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop():
    print("-----loop-----")
    while True:
        # もしボタンが押されているなら
        if GPIO.input(BTN_PIN) == GPIO.LOW:
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(INTERVAL)

            for pin in LED_PINS:
                GPIO.output(pin, GPIO.LOW)
                time.sleep(INTERVAL)


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
