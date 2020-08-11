
#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from msg_pkg.msg import Driving_msg
import serial


class driver:
    def __init__(self):
        # init ros
        rospy.init_node('rover_driver', anonymous=True)
        rospy.Subscriber('cmd_vel',Driving_msg,self.get_cmd_vel)
        self.serial = serial.Serial('/dev/ttyACM0', 9600)
        self.get_arduino_message()

    # get cmd_vel message, and get linear velocity and angular velocity
    def get_cmd_vel(self, data):
        x = data.twist.linear.x
        angular = data.twist.angular.z
	reset_flag = data.reset
	mo1 = data.m1
	mo2 = data.m2
        self.send_cmd_to_arduino(x, angular,reset_flag,mo1,mo2)

    # translate x, and angular velocity to PWM signal of each wheels, and send to arduino
    def send_cmd_to_arduino(self,x,angular,reset_flag,mo1,mo2):
        # calculate right and left wheels signal
    
        right = int((x + angular) * 25)
        left = int((x - angular) * 25)
	flag = int(reset_flag)
	motor1 = int(mo1)
	motor2 = int(mo2)
        # format for arduino
        message = "{},{},{},{},{}*".format(left, right, flag,motor1,motor2)
        
        # send by serial 
        self.serial.write(message)
        print message

    # receive serial text from arduino and publish it to '/arduino' message
    def get_arduino_message(self):
        pub = rospy.Publisher('arduino', String, queue_size=100)
        r = rospy.Rate(100)
        while not rospy.is_shutdown():
            message = self.serial.readline()
            pub.publish(message)
            #r.sleep()

if __name__ == '__main__':
    try:
        d = driver()
    except rospy.ROSInterruptException: 
        pass


