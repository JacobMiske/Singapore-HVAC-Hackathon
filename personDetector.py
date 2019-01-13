# There will be some mutiple detections as
# this is not the best way to do this 
# the best way would be implemeting deep learning but
# for application this will do
# This will only detect humans if you give full body. So test that way


from __future__ import print_function
import cv2
import numpy as np

person_detector = cv2.HOGDescriptor()
person_detector.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(640,360)) # Downscale to improve frame rateframe
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        rects, weights = person_detector.detectMultiScale(gray_frame)
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        print(len(rects)) #len(rects) gives the number of people detected. 
        cv2.imshow('Human Detection',frame) # comment this line to stop the display
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        pass
        
cap.release()
cv2.destroyAllWindows()
