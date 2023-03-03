import rospy
import math
from dsor_msgs.msg import Measurement
from std_msgs.msg import Float64

class Cntrl():
    def __init__(self):
        self.yaw_pub=rospy.Publisher("/bluerov/ref/yaw", Float64, queue_size=10)
        self.surge_pub=rospy.Publisher("/bluerov/ref/surge", Float64, queue_size=10)
        self.tolerance=2
        self.pos_sub=rospy.Subscriber("/bluerov/measurement/position", Measurement, self.utm_callback)
        #self.surge_pub.publish(1.0)
        print()

    def utm_callback(self,msg):
        if msg.header.frame_id=="bluerov_gnss":
            self.x=msg.value[0]
            self.y=msg.value[1]
            print(self.x,self.y)
        """
        with open("waypoint.txt","r") as f:
            for coordinates in f:
                wp=coordinates.strip().split()
                self.x_des=float(wp[0])
                self.y_des=float(wp[1])
                while True:
                    if msg.header.frame_id=="bluerov_gnss":
                        self.x=msg.value[0]
                        self.y=msg.value[1]
                        self.x=math.floor(self.x)
                        self.y=math.floor(self.y)
                        print(self.x_des,self.y_des)
                        psi_r = math.atan2(self.y_des-self.y,self.x_des-self.x)
                        self.psi_d= math.degrees(psi_r)
                        self.psi_d=math.floor(self.psi_d)
                        self.yaw_pub.publish(self.psi_d)
                        self.dist=math.sqrt((self.y_des-self.y)**2+(self.x_des-self.x)**2)
                        print(self.dist)
                        if self.dist>=self.tolerance:
                            self.surge_pub.publish(1.0)
                        else:
                            print("Waypoint achieved! Moving to next Waypoint")
                            self.surge_pub.publish(0.0)
                            break
        """            
        return 0

if __name__=="__main__":
    rospy.init_node("cntrl")
    rate =rospy.Rate(10)
    c=Cntrl()
    while not rospy.is_shutdown():
        rate.sleep()
        rospy.spin()