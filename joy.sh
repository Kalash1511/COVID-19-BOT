#!/bin/bash

sudo apt-get install libusb-dev 
sudo apt-get install ros-melodic-joy

ls /dev/input/js*

echo ""
echo "If you having multiple joystick name, then try with first if that not work for you then again run script with other joystick name"
echo " "
echo "provide The Name of JoyStick like js0 or js1"

read NAME
JOY="/dev/input/$NAME"

sudo chmod a+rw $JOY
echo ""
echo "Start ROSCORE in another terminal then press Enter"
read

PARAM='rosparam set joy_node/dev "'$JOY'"'
$PARAM

echo ""
echo 'Open another terminal and execute "'rostopic echo joy'"'
rosrun joy joy_node


