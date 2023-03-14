from gpiozero import LED, Button, Buzzer
from time import sleep
from signal import pause

led = LED(14)
button = Button(23)
buzz = Buzzer(12)

def ring():
    for i in range(5):
        buzz.on()
        led.on()
        sleep(0.5)
        buzz.off()
        led.off()
        sleep(0.5)

button.when_pressed = ring

pause()