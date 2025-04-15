import re
import socket
from gripper_methods_def import create_command


def open_and_wait(s: socket.socket):
    """
    Open gripper.
    """
    s.send(create_command(
        '$ 3 "rq_open_and_wait()"\n   rq_open_and_wait()').encode("utf8"))


def close_and_wait(s: socket.socket):
    """
    Close gripper.
    """
    s.send(create_command(
        '$ 3 "rq_close_and_wait()"\n   rq_close_and_wait()').encode("utf8"))


def acivate_and_wait(s: socket.socket):
    """
    Activate gripper.
    """
    s.send(create_command(
        '$ 3 "rq_activate_and_close()"\n   rq_activate_and_close()').encode("utf8"))


def gripper_led_on(s: socket.socket):
    """
    Turn on gripper LED.
    """
    s.send(create_command(
        '$ 3 "rq_gripper_led_on()"\n   rq_gripper_led_on()').encode("utf8"))


def gripper_led_off(s: socket.socket):
    """
    Turn off gripper LED.
    """
    s.send(create_command(
        '$ 3 "rq_gripper_led_off()"\n   rq_gripper_led_off()').encode("utf8"))

def move_and_wait_mm(s:socket, position:float):
    """
    Open gripper by position parameter in milimeters.
    """
    if 0 <= position <= 100:
        s.send(create_command(
        '$ 3 "rq_move_and_wait_mm('+ str(position) + ')"\n   rq_move_and_wait_mm(' + str(position) + ')').encode("utf8"))
    else:
        raise ValueError("Position is out of range.")
    
def reset(s:socket.socket):
    """
    Reset gripper.
    """
    s.send(create_command(
        '$ 3 "rq_reset()"\n   rq_reset()').encode("utf8"))
    
