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

import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()
path = 'dataSet'

def getImagesWithiD(path):
     imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
     faces = []
     id = []
     for imagePath in imagePaths:
         faceImg=Image.open(imagePath).convert('L')
         faceNp=np.array(faceImg,'uint8')
         ID=int(os.path.split(imagePath)[-1].split('.')[1])

         faces.append(faceNp)
         id.append(ID)
         cv2.imshow('training',faceNp)
         cv2.waitKey(10)

     return np.array(id),faces

id,faces = getImagesWithiD(path)
recognizer.train(faces,id)
recognizer.save('recognizer/trainData.yml')
cv2.destroyAllWindows()

         
