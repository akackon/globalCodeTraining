from gpiozero import *
from signal import pause
import requests
led = LED(17)
button = Button(2)
buzzer = Buzzer(15)
status  = 0

def ifttt():
    payload = {"value1" : "Kay", "value2" : "Adrian", "value3" : "Chris" }
    r = requests.get("https://maker.ifttt.com/trigger/globalcode/with/key/dnQRBX25f67fldZx2hf9u", params=payload)
    if r.status_code == 200:
        buzzer.beep()
    return led.blink()

button.when_pressed = ifttt
# button.when_released = buzzer.blink


pause()