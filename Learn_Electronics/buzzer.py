from gpiozero import Buzzer
from time import sleep

buzz = Buzzer(12)

print("Beeping the buzzer")

for i in range(5):
    buzz.on()
    sleep(0.5)
    buzz.off()
    sleep(0.5)