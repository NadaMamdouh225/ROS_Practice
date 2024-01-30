#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64 

class Number_Node(Node):
    def __init__(self):
        super().__init__("number_publisher")
        
        self.publisher_=self.create_publisher(Int64,"number",10)
        self.timer = self.create_timer(0.7,self.Publish_number)
        self.get_logger().info("Here we gooooo!")

    def Publish_number(self):
        msg = Int64()
        msg.data = 2
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Number_Node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
