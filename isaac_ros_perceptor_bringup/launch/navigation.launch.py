import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import isaac_ros_launch_utils as lu
from isaac_ros_launch_utils.all_types import *

def generate_launch_description():
    config_dir = os.path.join(get_package_share_directory('isaac_ros_perceptor_bringup'),'params')
    param_file = os.path.join(config_dir,'lavobot_params.yaml')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'),'/launch','/navigation_launch.py']),
            launch_arguments={
            'use_sim_time':'false',
            # 'container_name': "nova_container",
            # 'use_composition': 'True',
            'params_file': param_file}.items(),

        ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='map_odom_broadcaster',
        #     output='screen',
        #     arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom']
        # )
    ])