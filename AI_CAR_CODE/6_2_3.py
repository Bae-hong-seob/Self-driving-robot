import cv2
import RPi.GPIO as GPIO
import time

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3, 640)
    camera.set(4, 480)
  
    while( camera.isOpened() ):
        
        keyValue = cv2.waitKey(10)
        #print(str(keyValue))
        
        if keyValue == ord('q'):
            break
        elif keyValue == 82:
            print("up")
        elif keyValue == 84:
            print("down")
        elif keyValue == 81:
            print("left")
        elif keyValue == 83:
            print("right")
        
        _, image = camera.read()
        image = cv2.flip(image,-1)
        cv2.imshow('Original', image)
        
        height, _, _ = image.shape
        save_image = image[int(height/2):,:,:]
        save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2YUV)
        save_image = cv2.GaussianBlur(save_image, (3,3), 0)
        save_image = cv2.resize(save_image, (200,66))
        cv2.imshow('Save', save_image)
        
            
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
    GPIO.cleanup()