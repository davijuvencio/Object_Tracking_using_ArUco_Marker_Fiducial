# Object Tracking using ArUco Marker Fiducial and Calibration using Chessboard
This is a project for object tracking using the Raspberry Pi V2 camera, Raspberry Pi 4, and the ArUco Marker Fiducial method. The goal of the project is to detect and track objects using ArUco fiducial markers in real-time.

## Installation
This project requires the installation of some libraries, including OpenCV. You can install OpenCV by following the instructions at https://opencv.org/.

## Calibration
Before starting object tracking, it is necessary to calibrate the camera using a chessboard. Calibration is necessary to correct image distortion, which can affect the accuracy of tracking.

A chessboard is used because it has a regular and known structure, which can be easily detected by the camera. During calibration, the camera is moved to capture multiple images of the chessboard in different positions and orientations. Based on these images, the camera can be calibrated to correct image distortion.

## Tracking
After calibrating the camera, object tracking can be initiated using the ArUco fiducial markers. The ArUco fiducial markers are flat images that are detected by the camera and used as reference points for tracking objects.

The tracking algorithm uses the information from the ArUco fiducial markers to determine the position and orientation of the objects relative to the camera. This allows the objects to be tracked in real-time as they move in the scene.

## Contributing
Feel free to contribute to this project by creating new features or fixing existing issues. Please submit a pull request for review.


## To install OpenCV on Raspberry Pi 4, follow the steps below:
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev python3-pip python3-numpy python3-matplotlib python3-scipy python3-sklearn python3-skimage python3-pil python3-pandas python3-opencv
```

## To perform camera calibration, follow the steps below:

1. Acquire a checkerboard pattern for reference. You can download and print a calibration pattern online.

2. Position a strong light source behind the camera, ensuring that the checkerboard pattern is well illuminated.

3. Stand in front of the camera, showing the checkerboard pattern.

4. Run the Python code
```bash
python3 capture_images_for_calibration.py. 
```
This code will capture several camera images at different angles and positions.

5. Move the camera in a counterclockwise and clockwise motion, tilting it to the sides and up and down. Be sure to capture images in all positions to obtain the best calibration possible.

6. Select a photo with the checkerboard pattern facing the camera, a photo with the pattern turned sideways, a photo at the transition of the rotation, and a photo with each tilt. Delete the remaining photos.

Now you have enough images to perform camera calibration. With this information, you can proceed with the calibration process using libraries such as OpenCV.

## To calibrate
run the Python program:
```bash
python3 calibration.py 
```
This code performs camera calibration using images of a chessboard and generates a calibration matrix and distortion coefficients. To use the code, it is necessary to pass as arguments the path of the directory containing the images of the chessboard, the width and height of the chessboard, and the size of the square in meters. The user can also choose to visualize each image of the chessboard during the calibration process.

The code reads the images from the specified directory, converts each image to grayscale, and detects the corners of the chessboard using the "cv2.findChessboardCorners" function. It then adds the object coordinates (points in 3D in real space) and the image coordinates (points in 2D in the image plane) to two different lists. After all images have been read, the code uses the object and image points lists to generate a calibration matrix and distortion coefficients, using the "cv2.calibrateCamera" function. Finally, it saves the calibration matrix and distortion coefficients in two .npy files.