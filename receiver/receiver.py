# potentiometer.py
import os
import serial
import time
import data.database as database

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

button = 0

while button != 12:
    try:
        print("Pulsa un botón")
        line = ser.readline()   # read a byte
        if line:
            string = line.decode().strip()  # convert the byte string to a unicode string
            print("Has pulsado el botón " + string)
            button = int(string)
            os.system("python3 " + database.getPath(button))
    except:
        print("Error")
        
ser.close()