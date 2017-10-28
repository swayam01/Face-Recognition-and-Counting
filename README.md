First, install OpenCV dependencies. Compiling OpenCV on Raspberry Pi may take about five hours (depending on your system and network speed).<br />

Power on Raspberry Pi, open the terminal, set up Wi-Fi and execute the following commands:<br />

$ sudo apt-get update<br />
$ sudo apt-get upgrade<br />
$ sudo apt-get install build-essential<br />
cmake pkg-config python-dev libgtk2.0-<br />
dev libgtk2.0 zlib1g-dev libpng-dev<br />
libjpeg-dev libtiff-dev libjasper-dev<br />
libavcodec-dev swig unzip<br />

Now, unzip OpenCV directory by executing the following commands:<br />
$ wget http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.9/opencv-2.4.9.zip<br />
$ unzip opencv-2.4.9.zip<br />

Change the directory and execute cmake command as given below to build the makefile:<br />
$ cd opencv-2.4.9<br />
$ cmake -DCMAKE_BUILD_TYPE=RELEASE<br />
-DCMAKE_INSTALL_PREFIX=/usr/local<br />
-DBUILD_PERF_TESTS=OFF -DBUILD_opencv_<br />
gpu=OFF -DBUILD_opencv_ocl=OFF<br />
Compile the project by executing the command given below:<br />
$ make<br />
It may take about five hours for compilation.<br />

Install the compiled OpenCV libraries by executing the following command:<br />
$ sudo make install<br />

The latest version of OpenCV is now installed on your Raspberry Pi.<br />

Face-recognition code is written in Python, so some dependencies have to be installed using the following commands:<br />
$ sudo apt-get install python-pip<br />
$ sudo apt-get install python-dev<br />
$ sudo pip install picamera<br />
$ sudo pip install rpio<br />

After OpenCV and Python dependencies are installed, the project can be tested in three major steps as explained below.<br />
Software testing<br />

This project uses LPBH ALGORITHM IN OPENCV to perform face recognition. To use this algorithm, create a set of training data with pictures of faces that are allowed to trigger the relay.<br />

Execute the following command to run capture-positives script to find a single face image:<br />

$ sudo python DataCreate.py<br />

Wait for some time and observe the terminal until you see  capturing your face image. If the script detects a single face, it will crop and save the training image in dataSet sub-directory.<br />

If the script cannot detect a face, or detects multiple faces, error message ‘Could not detect single face! Check the image in capture.pgm’ will be displayed. It is recommended to maintain a distance of about 0.5 metres from the camera while taking a picture.<br />

Press Ctrl+C to stop the script. <br />

Check the face in the database and train the face recogniser by running trainer.py code:<br />
$ sudo python trainer.py<br />

Training the face-recognition model on Raspberry Pi will take about ten minutes. Once training is complete, you will see yml files with the train data of the model.<br />

Now, test the face recogniser to recognise the face trained earlier. Execute the following command:<br />
$ sudo python detector.py<br />

Observe the terminal, Aim the camera at your face . You should see a your face detected with the recognised name and confidence level<br />

