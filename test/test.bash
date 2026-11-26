#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log
cat /tmp/mypkg.log | grep 'Listen: 10'
