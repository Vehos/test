import serial

port = "COM6"
conn = serial.Serial(port, 115200)

msg = input("Message: ")

conn.write(msg.encode())