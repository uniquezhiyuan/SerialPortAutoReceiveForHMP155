import serial
import os
import time

ser=serial.Serial('com5', 9600, timeout=1)


while 1:
    string = ser.read(19).decode()
    if string[0] == '$':
        t1 = string[3:5] + '.' + string[5:7]
        t2 = string[9:11] + '.' + string[11:13]
        t3 = string[15:17] + '.' + string[17:19]
        write_line = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' ' + t1 + ' ' + t2 + ' ' + t3
        record = open('c:/data/record.csv', 'a+')
        record.write(write_line + '\n')
        print(time.strftime("%H:%M:%S", time.localtime()))
        print(write_line)
        time.sleep(1)
    else:
        pass




