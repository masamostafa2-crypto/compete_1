import rclpy
from rclpy.node import Node

from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge

import cv2 as cv


class MonoCamera(Node):

    def __init__(self):
        super().__init__('mono_camera')

        self.bridge = CvBridge()

        self.subscription = self.create_subscription(
            CompressedImage,
            '/mono/image',
            self.image_callback,
            10
        )

        self.get_logger().info(
            'Mono camera subscriber started'
        )

    def image_callback(self, msg):

        # Convert ROS Image → OpenCV image
        frame = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding='passthrough'
        )

        # Display the video
        cv.imshow('Mono Camera', frame)

        cv.waitKey(1)


def main(args=None):

    rclpy.init(args=args)

    node = MonoCamera()

    rclpy.spin(node)

    node.destroy_node()

    cv.destroyAllWindows()

    rclpy.shutdown()


if __name__ == '__main__':
    main()