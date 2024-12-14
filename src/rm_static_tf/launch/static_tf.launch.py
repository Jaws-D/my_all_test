import os
import sys
import yaml
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
from math import pi
sys.path.append(os.path.join(get_package_share_directory('rm_static_tf'), 'launch'))


def generate_launch_description():

    from launch_ros.descriptions import ComposableNode
    from launch_ros.actions import ComposableNodeContainer, Node,SetParameter
    from launch.actions import TimerAction, Shutdown
    from launch import LaunchDescription

    base_link_to_livox_frame= Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        arguments=['0','0','0','0','0','0','base_link','camera_init'],
        name="base_link_to_livox_frame"
    )

    base_link_to_laser_link = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        arguments=['0','0','0','0','0','0','base_link','laser_link'],
        name="base_link_to_laser_link"
    )
    return LaunchDescription([
            base_link_to_laser_link, 
            base_link_to_livox_frame,    
        ])
