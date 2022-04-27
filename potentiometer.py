# potentiometer.py
import os
import serial
import time

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
            if string=="1":
                print(string)
                os.system('ls -l')
            elif string=="2":
                print(string)
                os.system('ls -l')
            elif string=="3":
                print(string)
                os.system('ls -l')
            else:
                print(string)
                os.system('ls -l')
    except:
        print("Error")
        
ser.close()