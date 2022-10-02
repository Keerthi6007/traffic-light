from gpiozero import LED, Button
from time import sleep

green= LED (17)
red= LED(18)
yellow= LED(2)
button=(3)

print("press the button when you want to cross")

green.on(0)
yellow.off()
red.off()

while True:
    prinnt("wait")
    button.wait_for_press()
    green.off()
    yellow.off()
    red.on()
    print("cross now")
    sleep(10)
    yellow.on()
    sleep(5)
    green.on()
    yellow.off()
    red.off()
