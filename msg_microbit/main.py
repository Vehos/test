import serial

port = "COM6"
conn = serial.Serial(port, 115200)

while True:
    msg = input("Message: ")

    conn.write(msg.encode())
