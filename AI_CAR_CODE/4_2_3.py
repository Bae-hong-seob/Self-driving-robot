import serial

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

try:
    while True:
        data = bleSerial.readline()
        data = data.decode()
        if data.find("go") >= 0:
            print("ok go")
        elif data.find("back") >= 0:
            print("ok back")
        elif data.find("left") >= 0:
            print("ok left")
        elif data.find("right") >= 0:
            print("ok right")
        elif data.find("stop") >= 0:
            print("ok stop")
        
        
except KeyboardInterrupt:
    pass

bleSerial.close()


