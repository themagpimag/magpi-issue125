from gpiozero import LED, Button

led = LED(14)
button = Button(23)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()