#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircle(Node):
    def __init__(self):
        super().__init__("draw_node")
        #create publisher
        self.cmd_vel_pub = self.create_publisher(Twist,"/turtle1/cmd_vel",10) # 10 represents queue size
        #use timer
        self.timer = self.create_timer(0.5,self.send_vel_cmd_CB)
        #self.get_logger().info("Drawing a circle has been started")
        self.get_logger().info("drawing square")
    
    def send_vel_cmd_CB(self):
        # first create a msg object from the class twist
        msg = Twist()  
        #######################
        # for drawing circle
        #msg.linear.x = 2.0
        #msg.angular.z = 1.0
        #######################
        #my trial
        for i in range(4):
            msg.linear.x = 2.0
            msg.angular.z = 1.0
        
        # publish the msg
        self.cmd_vel_pub.publish(msg)




def main(args = None):
    #start communication
    rclpy.init(args = args)
    #####################
    #write your code here
    node = DrawCircle()
    rclpy.spin(node)
    #####################
    #end communication
    rclpy.shutdown()


if __name__ == '__main__':
    main()