import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class DetectionViewer(Node):
    def __init__(self):
        super().__init__('detection_viewer')
        self.bridge = CvBridge()
        self.create_subscription(Image, '/compete/detections', self.image_cb, 10)
        self.get_logger().info("Viewing /compete/detections -- press 'q' in the image window to quit.")

    def image_cb(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        cv2.imshow('Detections', cv_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            rclpy.shutdown()


def main():
    rclpy.init()
    node = DetectionViewer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()


if __name__ == '__main__':
    main()