from microbit import *

def set_pixel(msg):
        msg = msg
        x = chr(msg[0])
        x = int(x)

        y = chr(msg[1])
        y = int(y)

        z = chr(msg[2])
        z = int(y)

        if display.get_pixel(x, y) > 0:
            return("Not okey! ")

        else:
            display.set_pixel(x,y,z)
            return("OK! ")


while True:
    msg = uart.read()

    if msg:
        result = set_pixel(msg)
        print(result)
