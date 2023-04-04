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
