# pragya_perception

ROS Perception Package for 2D Object Detection

## Description
This package implements real-time 2D object detection using 
find_object_2d with custom modifications including ORB detector.

## Dependencies
- ROS Noetic
- find_object_2d
- image_publisher

## Installation
```bash
cd ~/your_ws/src
git clone https://github.com/yourusername/pragya_perception.git
cd ~/your_ws
catkin_make
```

## Usage
```bash
roscore
roslaunch pragya_perception pragya_object_detection.launch
rosrun image_publisher image_publisher /path/to/image.jpg __name:=my_camera
rosrun find_object_2d find_object_2d image:=/my_camera/image_raw
rosrun pragya_perception detection_monitor.py
```

## Modifications
1. Changed detector from SURF to ORB
2. Changed homography_min_inliers to 8
3. Changed max_objects to 5
4. Added custom detection_monitor.py node
