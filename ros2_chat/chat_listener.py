import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Chatlistener(Node):
    def __init__(self):
        super().__init__('chat_listener')
        self.subscription = self.create_subscription(
                String,
                'chat',
                self.listener_callback,
                10
        )

    def listener_callback(self, msg):
        self.get_logger().info(msg.data)

def main():
    rclpy.init()
    node = Chatlistener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
