import time
import cv2
import RPi.GPIO as GPIO


camera = cv2.VideoCapture(-1)
camera.set(3, 640)
camera.set(4, 480)
        
def main():
    try:
        while True:
            
            keyValue = cv2.waitKey(1)
        
            if keyValue == ord('q'):
                break
                
            _, image = camera.read()
            image = cv2.flip(image,-1)
            cv2.imshow('Original', image)
            height, _, _ = image.shape
            image = image[int(height/2):,:,:]
            image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
            image = cv2.resize(image, (200,66))
            image = cv2.GaussianBlur(image,(5,5),0)
            _,image = cv2.threshold(image,160,255,cv2.THRESH_BINARY_INV)
            cv2.imshow('processed', image)
            
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()

