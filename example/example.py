import time
from GripperSocketControl import Gripper


# CONSTANTS INIT
HOST = "192.168.0.96"
PORT = 30002

# INIT GRIPPER
my_gripper = Gripper(HOST, PORT)

# RUN PROGRAM
time.sleep(1)

my_gripper.acivate_and_wait()  # Activate gripper
my_gripper.gripper_led_on()  # Turn LED on
my_gripper.move_and_wait_mm(distance=10)  # Open gripper to 10 mm
my_gripper.gripper_led_off()  # Turn LED off
my_gripper.close_connection()  # Close connection with robot

time.sleep(1)
