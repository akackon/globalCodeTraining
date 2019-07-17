from gpiozero import *
from signal import pause

led = LED(17)
button = Button(2)
buzzer = Buzzer(15)
status  = 0


button.when_pressed = buzzer.on
button.when_released = buzzer.off
pause()