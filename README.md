设置环境变量：
source install/setup.bash
启动雷达驱动：
ros2 launch livox_ros_driver2 msg_MID360_launch.py
启动静态tf数据发布：
ros2 launch rm_static_tf static_tf.launch.py

ros2 run rm_dy_tf rm_dy_tf
启动点云数据转化为激光雷达扫描数据节点：
ros2 launch pointcloud_to_laserscan pointcloud_to_laserscan_launch.py
启动cartographer主要提供里程计数据：
ros2 launch fast_lio mapping.py
启动cartographer的rviz可视化：
ros2 launch rm_cartographer cartographer.launch.py
输出tf树：
ros2 run tf2_tools view_frames

ros2 launch rm_navigation2 rm_nav.launch.py

ros2 run nav2_map_server map_saver_cli **-t** map **-f** room_map

```
# 先将地图保存到src/fishbot_cartographer/map目录下
cd src/fishbot_cartographer/ && mkdir map && cd map
ros2 run nav2_map_server map_saver_cli -t map -f room_map
```
