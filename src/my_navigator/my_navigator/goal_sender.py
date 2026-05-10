import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator

class GoalSender(Node):
    def __init__(self):
        super().__init__('goal_sender')
        self.navigator = BasicNavigator()
        self.navigator.waitUntilNav2Active()

    def send_waypoints(self):
        waypoints = [(1.0, 0.5), (-1.0, 1.0), (0.0, 0.0)]
        for i, (x, y) in enumerate(waypoints):
            goal = PoseStamped()
            goal.header.frame_id = 'map'
            goal.header.stamp = self.get_clock().now().to_msg()
            goal.pose.position.x = x
            goal.pose.position.y = y
            goal.pose.orientation.w = 1.0
            self.get_logger().info(f'Going to waypoint {i+1}: ({x}, {y})')
            self.navigator.goToPose(goal)
            while not self.navigator.isTaskComplete():
                pass
            self.get_logger().info(f'Waypoint {i+1} reached!')

def main():
    rclpy.init()
    node = GoalSender()
    node.send_waypoints()
    rclpy.shutdown()
