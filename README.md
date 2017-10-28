First, install OpenCV dependencies. Compiling OpenCV on Raspberry Pi may take about five hours (depending on your system and network speed).
Power on Raspberry Pi, open the terminal, set up Wi-Fi and execute the following commands:
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install build-essential
cmake pkg-config python-dev libgtk2.0-
dev libgtk2.0 zlib1g-dev libpng-dev
libjpeg-dev libtiff-dev libjasper-dev
libavcodec-dev swig unzip
Now, unzip OpenCV directory by executing the following commands:
$ wget http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.9/opencv-2.4.9.zip
$ unzip opencv-2.4.9.zip
Change the directory and execute cmake command as given below to build the makefile:
$ cd opencv-2.4.9
$ cmake -DCMAKE_BUILD_TYPE=RELEASE
-DCMAKE_INSTALL_PREFIX=/usr/local
-DBUILD_PERF_TESTS=OFF -DBUILD_opencv_
gpu=OFF -DBUILD_opencv_ocl=OFF
Compile the project by executing the command given below:
$ make
It may take about five hours for compilation.
Install the compiled OpenCV libraries by executing the following command:
$ sudo make install
The latest version of OpenCV is now installed on your Raspberry Pi.
Face-recognition code is written in Python, so some dependencies have to be installed using the following commands:
$ sudo apt-get install python-pip
$ sudo apt-get install python-dev
$ sudo pip install picamera
$ sudo pip install rpio
After OpenCV and Python dependencies are installed, the project can be tested in three major steps as explained below.
Software testing
This project uses LPBH ALGORITHM IN OPENCV to perform face recognition. To use this algorithm, create a set of training data with pictures of faces that are allowed to trigger the relay.
Follow the steps given below:
Execute the following command to run capture-positives script to find a single face image:
$ sudo python DataCreate.py
Wait for some time and observe the terminal until you see  capturing your face image. If the script detects a single face, it will crop and save the training image in dataSet sub-directory.
If the script cannot detect a face, or detects multiple faces, error message ‘Could not detect single face! Check the image in capture.pgm’ will be displayed. It is recommended to maintain a distance of about 0.5 metres from the camera while taking a picture.
Press Ctrl+C to stop the script. 
Check the face in the database and train the face recogniser by running trainer.py code:
$ sudo python trainer.py
Training the face-recognition model on Raspberry Pi will take about ten minutes. Once training is complete, you will see yml files with the train data of the model.
Now, test the face recogniser to recognise the face trained earlier. Execute the following command:
$ sudo python detector.py
Observe the terminal, Aim the camera at your face . You should see a your face detected with the recognised name and confidence level

