#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node): 
    def __init__(self):
        super().__init__("robot_news_station")

        self.robot_name = "Alpha"
        self.publisher_ = self.create_publisher(String,"robot_news_topic",10)
        self.timer_= self.create_timer(1.0,self.Publish_news)
        self.get_logger().info("Robot News Station has been started")


    def Publish_news(self):
        msg = String()
        #msg.field
        msg.data = "Hello,baby "+str(self.robot_name) + " from robot news station"
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()