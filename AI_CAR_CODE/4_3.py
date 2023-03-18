import threading
import serial
import time

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)


def serial_thread():
    while True:
        data = bleSerial.readline()
        data = data.decode()
        print("serial:",data)

def main():
    try:
        while True:
            print("hello")
            time.sleep(1.0)

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()
    