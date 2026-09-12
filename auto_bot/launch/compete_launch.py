from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        
        Node(
            package='auto_bot',
            executable='compete',
            name='compete',
            output='screen',
        ),
         Node(
                    package='auto_bot',
                    executable='manual',
                    name='manual',
                    output='screen',
                ),
        Node(
                            package='auto_bot',
                            executable='camera_node',
                            name='camera_node',
                            output='screen',
                        )
    ])