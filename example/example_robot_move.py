import time
from GripperSocketControl.gripper import Gripper

# CONSTANTS INIT
HOST = "192.168.0.96"
PORT = 30002

my_gripper = Gripper(HOST, PORT)
time.sleep(5)
my_gripper.move_j(
    [-52.47, -97.79, -24.55, -140.20, 86.42, 333.11])
time.sleep(10)
my_gripper.move_l([0.025, -0.265, 0.197], [1.973, -2.401, 0.092], 0.1, 0.1)
