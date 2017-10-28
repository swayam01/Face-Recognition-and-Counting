import cv2
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

import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

id=raw_input('enter user id')
sampleNum=0

while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite('dataSet/user.'+str(id)+'.'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(100)
    cv2.imshow('face',img)
    #cv2.waitKey(1)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif sampleNum>20:
        break

cam.release()
cv2.destroyAllWindows()
