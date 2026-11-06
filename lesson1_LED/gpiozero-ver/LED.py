"""LEDを点滅させるコード(gpiozero)"""

import time
from gpiozero import LED

# GPIOxxのxx
led = LED(17)

try:
    while True:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

# Ctrl + Cが押されたらプログラム終了
except KeyboardInterrupt:
    pass
finally:
    # LEDのピンを開放
    led.close()
