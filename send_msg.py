from microbit import *
import radio

radio.on()

radio.config(channel=13)

while True:
    radio.send("Fatigué")
    sleep(2000)
