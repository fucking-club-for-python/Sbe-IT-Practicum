"""流れるLED(gpiozero)"""

import time
from gpiozero import LED

LEDS = [LED(i) for i in (17, 13, 26)]
INTERVAL = 0.2


try:
    while True:
        for led in LEDS[:-1]:
            led.on()
            time.sleep(INTERVAL)
            led.off()

        for led in LEDS[::-1][:-1]:
            led.on()
            time.sleep(INTERVAL)
            led.off()

except KeyboardInterrupt:
    pass
finally:
    for led in LEDS:
        led.close()
