import serial
import requests

port = "COM6"
conn = serial.Serial(port, 115200)

message = input("Message: ")
conn.write(message.encode())
