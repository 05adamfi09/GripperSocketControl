# Gripper Socket Control

This package enables user to control Robotiq Hand-E gripper via Python.

## About package

Package was created as part of a school project, where we wanted to control Universal Robots UR3e with Robotiq Hand-E gripper via Python. For unknown reason we weren't able to control gripper via Robotiq library, so we decide to create are own simple library.

## Principle

When you are using this package, you must be in same network as a UR robot. The package main class `Gripper` contains socket connection with UR robot. `Gripper` functions sends Universal Robots `.script` file via socket connection.

## Installation 

```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple GripperSocketControl
```

## Example

``` python
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
```