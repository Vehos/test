import serial
import requests

port = "COM6"
conn = serial.Serial(port, 115200)

def ask_position():
    x = input("x: ")
    y = input("y: ")
    z = input("Intensité de 0 à 9: ")

    message = str(x) + str(y) + str(z)
    return message

while True:

    position = ask_position()
    conn.write(position.encode())

    incoming = conn.readline()
    if incoming.decode().strip() == "OK":
        print("Pixel bien placé !")
    else:
        print("Erreur")
