"""3つのLEDを、順番に点灯・消灯させるコード(gpiozero)"""

import time
from gpiozero import LED

LEDS = [LED(i) for i in (17, 13, 26)]


try:
    while True:
        for led in LEDS:
            led.on()
            time.sleep(1)

        for led in LEDS[::-1]:
            led.off()
            time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    for led in LEDS:
        led.close()
