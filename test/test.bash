#!/bin/bash -xv
#SPDX-FileCopyrightText: 2025 rupa-04
#SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws || exit 1

colcon build
source $dir/.bashrc

timeout 10 ros2 launch ros2_chat chat.launch.py > /tmp/ros2_chat.log 2>&1

grep 'chat_listener' /tmp/ros2_chat.log || exit 1

grep 'chat_talker' /tmp/ros2_chat.log || exit 1
