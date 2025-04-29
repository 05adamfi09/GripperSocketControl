import time
from GripperSocketControl.gripper import Gripper


# CONSTANTS INIT
HOST = "192.168.0.96"
PORT = 30002

# INIT GRIPPER
my_gripper = Gripper(HOST, PORT)

# RUN PROGRAM
time.sleep(1)

my_gripper.reset()  # Reset gripper

time.sleep(3)

my_gripper.activate_and_wait()  # Activate gripper

time.sleep(3)

my_gripper.gripper_led_on()  # Turn LED on

time.sleep(2)

my_gripper.move_and_wait_mm(distance=10)  # Open gripper to 10 mm

time.sleep(2)

my_gripper.gripper_led_off()  # Turn LED off

time.sleep(1)

my_gripper.open_and_wait()  # Open gripper

time.sleep(2)

my_gripper.close_and_wait()  # Close gripper

time.sleep(2)

my_gripper.close_connection()  # Close connection with robot

time.sleep(1)
