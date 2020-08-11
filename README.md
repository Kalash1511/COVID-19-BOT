# Bot_Setup

First of all git clone this repository by folllowing cmd.

$ sudo apt-get update \
$ sudo apt-get install git-core \
$ git clone https://github.com/SachinVekariya/Bot_Setup.git 

Note : If you are working with Raspberry Pi, then follow the documention given above for necessary setup.

### Step1 -->> ROS Installation

If you have already Installed ROS Melodic, then you can skip the 1st step.
Open the terminal by Ctrl+Alt+T and 

$ cd Bot_Setup \
$ bash ros_install.sh 

Note : In process, sometime you need to provide permission and your system password.
For any difficulty visit the link given below.

http://wiki.ros.org/melodic/Installation/Ubuntu

### Step 2 -->> Create workspace

$ cd Bot_Setup \
$ bash workspace_setup.bash 

It will create workspace named catkin_ws.

### Step 3 -->> Configure Joy_Stick

Connect the joystick to your device and ensure that power light in joystick is glowing.

$ cd Bot_Setup
$ bash joy.sh

After running this script, run "$ rostopic echo joy" and press the buttons to check it's working or not.
If it's not working then run this script again by selecting another "jsX" device in process.

For any difficulty visit the link given below. \
http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick

### Step 4 -->> Driving Package Setup

$ cd Bot_Setup \
$ bash packages.sh  

### Step 5 -->> Working with Arduino

If you not installed Arduino IDE in your device, then install form Ubuntu store by searching "Arduino IDE".
Conect arduino to your device.

Provide the permission to arduino.

$ sudo chmod 666 /dev/ttyACM   
press Tab key two times to autocomplete and you will get port name similar "ACM0"

Open the Arduino IDE and select the Port and Board in Tools in Menubar. \
Then open the arduino file situate at "catkin_ws/src/driving/arduino_driving_cytron.ino" and make some changes according to pin connections to the arduino and then Upload code by pressing "CTRL+U".


## Finally Setup and completed and you can drive bot.

For that,
Connect the Joystick and arduino to device and run all this cmds in seperate terminals.

To take joystick data \
$ rosrun joy joy_node 

To map the buttons, To see button configuration follow the picture given above \
$ cd ~/catkin_ws/src/driving/src \
$ python driving_control.py 

To send data on the arduino serial. \
$ python arduino_driving.py  

