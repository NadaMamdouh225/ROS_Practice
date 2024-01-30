#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64 

class Number_CountNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter = 0
        self.publisher_=self.create_publisher(Int64,"number_count",10)
        self.subscriber_=self.create_subscription(Int64, "number", self.GetData, 10)
        self.get_logger().info("let's see your progress,dude")
    
    def GetData(self,msg):
        self.counter += msg.data
        new_msg =Int64()
        new_msg.data = self.counter
        self.publisher_.publish(new_msg)               #publish data once you receive it
           

def main(args=None):
    rclpy.init(args=args)
    node = Number_CountNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()