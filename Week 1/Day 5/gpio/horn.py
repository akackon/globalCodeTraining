from gpiozero import LED, Button, Buzzer
from signal import pause

buzzer = Buzzer(17)
button = Button(2)

button.when_pressed = print("Hello")
button.when_released = buzzer.off