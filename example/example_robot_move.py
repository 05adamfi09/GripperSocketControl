import time
from GripperSocketControl.gripper import Gripper

# CONSTANTS INIT
HOST = "192.168.0.96"
PORT = 30002

my_gripper = Gripper(HOST, PORT)
time.sleep(1)
my_gripper.move_j(
    [0.0, -90.0, 0.0, -90.0, 0.0, 0.0])
