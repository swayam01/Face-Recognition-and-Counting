#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 Swayam Mittal (swayammittal65.blogspot.com)
Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""

import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
roc=cv2.createLBPHFaceRecognizer()
roc.load('recognizer\\trainData.yml')
id = 0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,3,1,0,2)
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=roc.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            cv2.cv.PutText(cv2.cv.fromarray(img),str('unkown'),(x,y+h+30),font,255)
        else:
            if(id==1):
                id='Swayam'
            elif(id==2):
                id='Suniel'
            
                
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id)+','+str(conf),(x,y+h),font,255)
    cv2.imshow('face',img)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
