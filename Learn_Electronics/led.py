from gpiozero import LED
from time import sleep

led = LED(14)

print("Blinking the LED")

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)