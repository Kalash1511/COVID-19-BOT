# Make Workspace
mkdir -p ~/catkin_ws/src

# Intialize Workspace
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws
catkin_make

# Source
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
