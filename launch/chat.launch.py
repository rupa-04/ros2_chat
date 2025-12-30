#!/usr/bin/python3
#SPDX-FileCopyrightText: 2025 rupa-04
#SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_chat',
            executable='chat_listener',
            name='chat_listener',
            output='screen'
        ),
        Node(
            package='ros2_chat',
            executable='chat_talker',
            name='chat_talker',
            output='screen'
        ),
    ])
