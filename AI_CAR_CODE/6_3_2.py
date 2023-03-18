import cv2
import RPi.GPIO as GPIO
import time

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3, 640)
    camera.set(4, 480)
    filepath = "/home/pi/AI_CAR/video/test"
    i = 0
    
    while( camera.isOpened() ):
        
        keyValue = cv2.waitKey(10)
        
        if keyValue == ord('q'):
            break
        
        _, image = camera.read()
        image = cv2.flip(image,-1)
        cv2.imshow('Original', image)
        
        cv2.imwrite("%s_%05d.png" % (filepath, i), image)
        i = i + 1
        
        time.sleep(1.0)
            
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
    GPIO.cleanup()

