import threading
import time
import cv2
import RPi.GPIO as GPIO
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

PWMA = 18
AIN1   =  22
AIN2   =  27

PWMB = 23
BIN1   = 25
BIN2  =  24

def motor_back(speed):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2,False)#AIN2
    GPIO.output(AIN1,True) #AIN1
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2,False)#BIN2
    GPIO.output(BIN1,True) #BIN1
    
def motor_go(speed):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2,True)#AIN2
    GPIO.output(AIN1,False) #AIN1
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2,True)#BIN2
    GPIO.output(BIN1,False) #BIN1

def motor_stop():
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN2,False)#AIN2
    GPIO.output(AIN1,False) #AIN1
    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN2,False)#BIN2
    GPIO.output(BIN1,False) #BIN1
    
def motor_right(speed):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2,True)#AIN2
    GPIO.output(AIN1,False) #AIN1
    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN2,False)#BIN2
    GPIO.output(BIN1,True) #BIN1
    
def motor_left(speed):
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN2,False)#AIN2
    GPIO.output(AIN1,True) #AIN1
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2,True)#BIN2
    GPIO.output(BIN1,False) #BIN1
        
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(PWMA,GPIO.OUT)

GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)

L_Motor= GPIO.PWM(PWMA,100)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB,100)
R_Motor.start(0)

speedSet = 40

# Pretrained classes in the model
classNames = {0: 'background',
              1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
              7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
              13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
              18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
              24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
              32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
              37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
              41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
              46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
              51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
              56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
              61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
              67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
              75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
              80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
              86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}


def id_class_name(class_id, classes):
    for key, value in classes.items():
        if class_id == key:
            return value
        
def img_preprocess(image):
    height, _, _ = image.shape
    image = image[int(height/2):,:,:]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    image = cv2.resize(image, (200,66))
    image = cv2.GaussianBlur(image,(5,5),0)
    _,image = cv2.threshold(image,160,255,cv2.THRESH_BINARY_INV)
    image = image / 255
    return image

camera = cv2.VideoCapture(-1)
camera.set(3, 640)
camera.set(4, 480)

_, image = camera.read()
image_ok = 0

box_size = 0
carState = "stop"

def opencvdnn_thread():
    global image
    global image_ok
    global box_size
    global carState
    model = cv2.dnn.readNetFromTensorflow('/home/pi/AI_CAR/OpencvDnn/models/frozen_inference_graph.pb',
                                      '/home/pi/AI_CAR/OpencvDnn/models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
    while True:
        if image_ok == 1:
            imagednn = image
            image_height, image_width, _ = imagednn.shape
            
            model.setInput(cv2.dnn.blobFromImage(imagednn, size=(250, 250), swapRB=True))
            output = model.forward()
            # print(output[0,0,:,:].shape)
            for detection in output[0, 0, :, :]:
                confidence = detection[2]
                if confidence > .5:
                    class_id = detection[1]
                    class_name=id_class_name(class_id,classNames)
                    if class_name is "person":
                        print(str(str(class_id) + " " + str(detection[2])  + " " + class_name))
                        box_x = detection[3] * image_width
                        box_y = detection[4] * image_height
                        box_width = detection[5] * image_width
                        box_height = detection[6] * image_height
                        box_size = box_width * box_height
                        print("box_size:",box_size)
                        
                        carState = "stop"
                        print("auto stop")
                
                        cv2.rectangle(imagednn, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=1)
                        cv2.putText(imagednn,class_name ,(int(box_x), int(box_y+.05*image_height)),cv2.FONT_HERSHEY_SIMPLEX,(.005*image_width),(0, 0, 255))
            
            cv2.imshow('imagednn', imagednn)
            image_ok = 0
        

def main():
    global image
    global image_ok
    global carState
    
    model_path = '/home/pi/AI_CAR/model/lane_navigation_final.h5'
    model = load_model(model_path)
    
    try:
        while True:
            keyValue = cv2.waitKey(1)
        
            if keyValue == ord('q') :
                break
            elif keyValue == 82 :
                print("go")
                carState = "go"
            elif keyValue == 84 :
                print("stop")
                carState = "stop"
            
            image_ok = 0
            _, image = camera.read()
            image = cv2.flip(image,-1)
            image_ok = 1
            
            preprocessed = img_preprocess(image)
            cv2.imshow('pre', preprocessed)
            
            X = np.asarray([preprocessed])
            steering_angle = int(model.predict(X)[0])
            print("predict angle:",steering_angle)
                
            if carState == "go":
                if steering_angle >= 70 and steering_angle <= 110:
                    print("go")
                    motor_go(speedSet)
                elif steering_angle > 111:
                    print("right")
                    motor_right(speedSet)
                elif steering_angle < 71:
                    print("left")
                    motor_left(speedSet)
            elif carState == "stop":
                motor_stop()
            
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    task1 = threading.Thread(target = opencvdnn_thread)
    task1.start()
    main()
    cv2.destroyAllWindows()