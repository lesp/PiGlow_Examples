from piglow import PiGlow
from time import sleep

piglow = PiGlow()

print("You will now be asked how bright you would like each LED to be, choose a number between 0 and 255")
sleep(3)
val1 = input("White: ")
val2 = input("Blue: ")
val3 = input("Green: ")
val4 = input("Yellow: ")
val5 = input("Orange: ")
val6 = input("Red: ")
delay = input("How long is the delay between flashes? :")

while True:
    piglow.white(val1)
    sleep(delay)
    piglow.blue(val2)
    sleep(delay)
    piglow.green(val3)
    sleep(delay)
    piglow.yellow(val4)
    sleep(delay)
    piglow.orange(val5)
    sleep(delay)
    piglow.red(val6)
    sleep(delay)
    piglow.all(0)
