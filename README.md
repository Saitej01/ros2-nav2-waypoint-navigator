# ROS2 Nav2 Waypoint Navigator

Autonomous multi-goal navigation system built with ROS2 Humble, Nav2, and Turtlebot3 in Gazebo simulation. A custom Python node sends sequential waypoint goals to the Nav2 stack, enabling fully autonomous mission planning.

---

## Demo
[Uploading Screencast from 05-10-2026 09:17:37 PM.webm…]()


---

## Features

- Autonomous waypoint navigation using Nav2 `BasicNavigator`
- Multi-goal mission planning via custom Python ROS2 node
- Simulated environment with Turtlebot3 Burger in Gazebo
- SLAM-based map generation using Cartographer
- Real-time visualization in RViz2

---

## Tech Stack

| Tool | Purpose |
|---|---|
| ROS2 Humble | Robot middleware |
| Nav2 | Autonomous navigation stack |
| Turtlebot3 (Burger) | Robot model |
| Gazebo Classic | Physics simulation |
| RViz2 | Visualization |
| SLAM Toolbox / Cartographer | Map generation |

---

## Prerequisites

- Ubuntu 22.04
- ROS2 Humble ([install guide](https://docs.ros.org/en/humble/Installation.html))

```bash
sudo apt install ros-humble-turtlebot3* \
                 ros-humble-turtlebot3-simulations \
                 ros-humble-navigation2 \
                 ros-humble-nav2-bringup \
                 ros-humble-turtlebot3-cartographer
```

---

## Setup

```bash
# Clone the repo
git clone https://github.com/Saitej01/ros2-nav2-waypoint-navigator.git
cd ros2-nav2-waypoint-navigator

# Set robot model
echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
source ~/.bashrc

# Build
cd ~/ros2_ws
colcon build
source install/setup.bash
```

---

## Usage

### Step 1 — Launch Gazebo simulation
```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### Step 2 — Launch Nav2 with map
```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  use_sim_time:=True \
  map:=/opt/ros/humble/share/turtlebot3_navigation2/map/map.yaml
```

### Step 3 — Run the waypoint navigator
```bash
ros2 run my_navigator goal_sender
```

The robot will autonomously navigate through all defined waypoints and log progress to the terminal.

---

## How It Works

The `goal_sender.py` node uses Nav2's `BasicNavigator` API to send a sequence of `PoseStamped` goal messages to the navigation stack. Nav2 handles path planning (NavFn), obstacle avoidance (DWB controller), and localization (AMCL) internally.

```
goal_sender node
      │
      ▼ PoseStamped goals
   Nav2 Stack
      ├── AMCL (localization)
      ├── NavFn (global planner)
      └── DWB (local controller)
            │
            ▼ /cmd_vel
         Turtlebot3 (Gazebo)
```

---

## Waypoints (customizable)

Edit `goal_sender.py` to change waypoints:

```python
waypoints = [
    (1.0,  0.5),   # waypoint 1
    (-1.0, 1.0),   # waypoint 2
    (0.0,  0.0),   # home
]
```

---

## Project Structure

```
ros2_ws/
└── src/
    └── my_navigator/
        ├── my_navigator/
        │   └── goal_sender.py   # main node
        ├── package.xml
        └── setup.py
```

---

## Author

**Saitej** — [github.com/Saitej01](https://github.com/Saitej01)
