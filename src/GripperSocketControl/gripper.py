from socket import socket, AF_INET, SOCK_STREAM
from .gripper_methods_def import create_command


class Gripper:
    """
    Class that symbolise Robotiq Hand-E gripper.

    methods:
        close_connection()
        open_and_wait()
        close_and_wait()
        activate_and_wait()
        reset()
        gripper_led_on()
        gripper_led_off()
        move_and_wait_mm(distance: float)
    """

    def __init__(self, ip_address: str, port: int = 30002):
        """
        Gripper initializer.

        :param ip_address: Universal Robots arm IP address
        :param port: gripper port, usualy 30002
        """
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((ip_address, port))

    def close_connection(self) -> None:
        """
        Close connection with robot.
        """
        self.socket.close()

    def open_and_wait(self) -> None:
        """
        Open gripper.
        """
        self.socket.send(create_command(
            '$ 3 "rq_open_and_wait()"\n   rq_open_and_wait()').encode("utf8"))

    def close_and_wait(self) -> None:
        """
        Close gripper.
        """
        self.socket.send(create_command(
            '$ 3 "rq_close_and_wait()"\n   rq_close_and_wait()').encode("utf8"))

    def acivate_and_wait(self) -> None:
        """
        Activate gripper.
        """
        self.socket.send(create_command(
            '$ 3 "rq_activate_and_close()"\n   rq_activate_and_close()').encode("utf8"))

    def gripper_led_on(self) -> None:
        """
        Turn on gripper LED.
        """
        self.socket.send(create_command(
            '$ 3 "rq_gripper_led_on()"\n   rq_gripper_led_on()').encode("utf8"))

    def gripper_led_off(self) -> None:
        """
        Turn off gripper LED.
        """
        self.socket.send(create_command(
            '$ 3 "rq_gripper_led_off()"\n   rq_gripper_led_off()').encode("utf8"))

    def move_and_wait_mm(self, distance: float) -> None:
        """
        Open gripper by position parameter in milimeters.
        :param distance: distance between gripper fingers
        """
        if 0 <= distance:
            print(create_command(
                '$ 3 "rq_move_and_wait_mm(' + str(distance) + ')"\n   rq_move_and_wait_mm(' + str(distance) + ')').encode("utf8"))
            self.socket.send(create_command(
                '  $ 3 "rq_move_and_wait_mm(' + str(distance) + ')"\n   rq_move_and_wait_mm(' + str(distance) + ')').encode("utf8"))
        else:
            raise ValueError("Position is out of range.")

    def reset(self) -> None:
        """
        Reset gripper.
        """
        self.socket.send(create_command(
            '$ 3 "rq_reset()"\n   rq_reset()').encode("utf8"))
