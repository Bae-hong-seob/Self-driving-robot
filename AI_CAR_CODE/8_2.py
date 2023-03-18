import cv2
import RPi.GPIO as GPIO
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

def img_preprocess(image):
    height, _, _ = image.shape
    image = image[int(height/2):,:,:]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    image = cv2.GaussianBlur(image, (3,3), 0)
    image = cv2.resize(image, (200,66)) 
    image = image / 255
    return image

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3, 640)
    camera.set(4, 480)
    model_path = '/home/pi/AI_CAR/model/lane_navigation_final.h5'
    model = load_model(model_path)
    
    carState = "stop"
    
    while( camera.isOpened()):
        
        keValue = cv2.waitKey(1)
        
        if keValue == ord('q') :
            break
        
        _, image = camera.read()
        image = cv2.flip(image,-1)
        cv2.imshow('Original', image)
        
        preprocessed = img_preprocess(image)
        cv2.imshow('pre', preprocessed)
        
        X = np.asarray([preprocessed])
        steering_angle = int(model.predict(X)[0])
        print("predict angle:",steering_angle)
        
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
    GPIO.cleanup()