from microbit import *
import radio

radio.on()

while True:
    msg = uart.read()

    if msg:
        display.scroll(msg)
