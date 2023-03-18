import cv2
import RPi.GPIO as GPIO
import time

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3, 640)
    camera.set(4, 480)
    filepath = "/home/pi/AI_CAR/video/train"
    i = 0
    carState = "stop"
    while( camera.isOpened() ):
        
        keyValue = cv2.waitKey(10)
        
        if keyValue == ord('q'):
            break
        elif keyValue == 82:
            print("go")
            carState = "go"
        elif keyValue == 84:
            print("stop")
            carState = "stop"
        elif keyValue == 81:
            print("left")
            carState = "left"
        elif keyValue == 83:
            print("right")
            carState = "right"
        
        _, image = camera.read()
        image = cv2.flip(image,-1)
        cv2.imshow('Original', image)
        
        height, _, _ = image.shape
        save_image = image[int(height/2):,:,:]
        save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2YUV)
        save_image = cv2.GaussianBlur(save_image, (3,3), 0)
        save_image = cv2.resize(save_image, (200,66))
        cv2.imshow('Save', save_image)
        
        if carState == "left":
            cv2.imwrite("%s_%05d_%03d.png" % (filepath, i, 45), save_image)
            i += 1
        elif carState == "right":
            cv2.imwrite("%s_%05d_%03d.png" % (filepath, i, 135), save_image)
            i += 1
        elif carState == "go":
            cv2.imwrite("%s_%05d_%03d.png" % (filepath, i, 90), save_image)
            i += 1
        
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
    GPIO.cleanup()