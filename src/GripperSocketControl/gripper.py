import emoji
from socket import socket, AF_INET, SOCK_STREAM
from socket import error as socket_error
from .gripper_methods_def import create_command


class Gripper:
    """
    Class that symbolise Robotiq Hand-E gripper.

    methods:
        connect()
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
        self._ip_address = ip_address
        self._port = port

        try:
            self.socket = socket(AF_INET, SOCK_STREAM)

            print(
                f"{emoji.emojize(':globe_with_meridians:')} Connecting {ip_address}:{port}")
            self.socket.connect((self._ip_address, self._port))
            print(f"{emoji.emojize(':check_mark_button:')} Succesfully coneted!")

        except socket_error as e:
            print(f"{emoji.emojize(':cross_mark_button:')} Connecting error - {e}")

        except Exception as e:
            print(
                f"{emoji.emojize(':cross_mark_button:')} Unexpected error during connecting to socket - {e}")

    def connect(self) -> None:
        """
        Open connection with robot.
        """
        if self.socket:
            self.socket.connect((self._ip_address, self._port))
        else:
            try:
                self.socket = socket(AF_INET, SOCK_STREAM)

                print(
                    f"{emoji.emojize(':globe_with_meridians:')} Connecting {self._ip_address}:{self._port}")
                self.socket.connect((self._ip_address, self._port))
                print(f"{emoji.emojize(':check_mark_button:')} Succesfully coneted!")

            except socket_error as e:
                print(
                    f"{emoji.emojize(':cross_mark_button:')} Connecting error - {e}")

            except Exception as e:
                print(
                    f"{emoji.emojize(':cross_mark_button:')} Unexpected error during connecting to socket - {e}")

    def close_connection(self) -> None:
        """
        Close connection with robot.
        """
        if self.socket:
            print(f"{emoji.emojize(':stop_sign:')} Closing socket")
            self.socket.close()

    def open_and_wait(self) -> None:
        """
        Open gripper.
        """
        print(f"{emoji.emojize(':hand_with_fingers_splayed:')}  Openning gripper")
        self.socket.send(create_command(
            '$ 3 "rq_open_and_wait()"\n   rq_open_and_wait()').encode("utf8"))

    def close_and_wait(self) -> None:
        """
        Close gripper.
        """
        print(f"{emoji.emojize(':raised_fist:')} Closing gripper")
        self.socket.send(create_command(
            '$ 3 "rq_close_and_wait()"\n   rq_close_and_wait()').encode("utf8"))

    def activate_and_wait(self) -> None:
        """
        Activate gripper.
        """
        print(f"{emoji.emojize(':upwards_button:')} Activating gripper")
        self.socket.send(create_command(
            '$ 3 "rq_activate_and_wait()"\n   rq_activate_and_wait()').encode("utf8"))

    def gripper_led_on(self) -> None:
        """
        Turn on gripper LED.
        """
        print(f"{emoji.emojize(':light_bulb:')} Turning gripper LED on")
        self.socket.send(create_command(
            '$ 3 "rq_gripper_led_on()"\n   rq_gripper_led_on()').encode("utf8"))

    def gripper_led_off(self) -> None:
        """
        Turn off gripper LED.
        """
        print(f"{emoji.emojize(':light_bulb:')} Turning gripper LED off")
        self.socket.send(create_command(
            '$ 3 "rq_gripper_led_off()"\n   rq_gripper_led_off()').encode("utf8"))

    def move_and_wait_mm(self, distance: float) -> None:
        """
        Open gripper by position parameter in milimeters.
        :param distance: distance between gripper fingers
        """
        if 0 <= distance:
            print(f"{emoji.emojize(':rocket:')} Oppening gripper to {distance} mm")
            self.socket.send(create_command(
                '  $ 3 "rq_move_and_wait_mm(' + str(distance) + ')"\n   rq_move_and_wait_mm(' + str(distance) + ')').encode("utf8"))
        else:
            raise ValueError("Position is out of range.")

    def reset(self) -> None:
        """
        Reset gripper.
        """
        print(f"{emoji.emojize(':counterclockwise_arrows_button:')} Resetting gripper")
        self.socket.send(create_command(
            '$ 3 "rq_reset()"\n   rq_reset()').encode("utf8"))
