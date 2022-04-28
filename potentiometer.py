# potentiometer.py
import os
import serial
import time

import database

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

while True:
    try:
        print("Pulsa un botón")
        line = ser.readline()   # read a byte
        if line:
            string = line.decode().strip()  # convert the byte string to a unicode string
            print("Has pulsado el botón " + string)
            os.system("python3 " + database.getPath(string))
    except:
        print("Error")
        
ser.close()