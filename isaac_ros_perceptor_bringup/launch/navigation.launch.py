import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    config_dir = os.path.join(get_package_share_directory('isaac_ros_perceptor_bringup'),'params')
    param_file = os.path.join(config_dir,'lavobot_nav2.yaml')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'),'/launch','/bringup_launch.py']),
            launch_arguments={
            'use_sim_time':'false',
            'use_localization':'False',
            'use_composition':'True',
            'container_name':'nav_container',
            'slam':'False',
            'map':"",
            'params_file': param_file}.items(),
        ),
    ])