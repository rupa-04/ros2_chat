import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Chattalker(Node):
    def __init__(self):
        super().__init__('chat_talker')
        self.publisher_ = self.create_publisher(string, 'chat', 10)
        self.username = input('Enter your name: ')

        self.get_logger().info("Type messages and press Enter to send.")

        while rclpy.ok():
            msg = String()
            text = input()
            msg.data = f"{self.username}: {text}"
            self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = Chattalker()
    rcply.shutdown()
