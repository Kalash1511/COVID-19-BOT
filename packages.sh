#!/bin/bash

sudo apt-get update
sudo apt-get install git-core
sudo apt-get install ros-melodic-rosserial-arduino ros-melodic-rosserial-python ros-melodic-rosserial-server ros-melodic-rosserial-client ros-melodic-rosserial-msgs

cd ~/catkin_ws/src
git clone https://github.com/SachinVekariya/driving.git

cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
source ~/.bashrc
