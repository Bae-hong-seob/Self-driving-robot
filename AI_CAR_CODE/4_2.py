import serial

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

try:
    while True:
        data = bleSerial.readline()
        print(data)
        
except KeyboardInterrupt:
    pass

bleSerial.close()
