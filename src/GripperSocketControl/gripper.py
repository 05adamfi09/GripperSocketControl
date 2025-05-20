from typing import List
import math
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
        self._connected = False

        try:
            self.socket = socket(AF_INET, SOCK_STREAM)

            print(
                f"🌐 Connecting {self._ip_address}:{self._port}")
            self.socket.connect((self._ip_address, self._port))
            print(f"✅ Succesfully connected!")
            self._connected = True

        except socket_error as e:
            print(f"❎ Connecting error - {e}")

        except Exception as e:
            print(
                f"❎ Unexpected error during connecting to socket - {e}")

    def connect(self) -> None:
        """
        Open connection with robot.
        """
        if not self._connected:
            try:
                self.socket = socket(AF_INET, SOCK_STREAM)

                print(
                    f"🌐 Connecting {self._ip_address}:{self._port}")
                self.socket.connect((self._ip_address, self._port))
                print("✅ Succesfully coneted!")
                self._connected = True

            except socket_error as e:
                print(
                    f"❎ Connecting error - {e}")

            except Exception as e:
                print(
                    f"❎ Unexpected error during connecting to socket - {e}")

    def close_connection(self) -> None:
        """
        Close connection with robot.
        """
        if self.socket:
            print("🛑 Closing socket")
            self.socket.close()
            self._connected = False

    def open_and_wait(self) -> None:
        """
        Open gripper.
        """
        print("✋ Openning gripper")
        self.socket.send(create_command(
            '$ 3 "rq_open_and_wait()"\n   rq_open_and_wait()').encode("utf8"))

    def close_and_wait(self) -> None:
        """
        Close gripper.
        """
        print("✊ Closing gripper")
        self.socket.send(create_command(
            '$ 3 "rq_close_and_wait()"\n   rq_close_and_wait()').encode("utf8"))

    def activate_and_wait(self) -> None:
        """
        Activate gripper.
        """
        print("⬆️ Activating gripper")
        self.socket.send(create_command(
            '$ 3 "rq_activate_and_wait()"\n   rq_activate_and_wait()').encode("utf8"))

    def gripper_led_on(self) -> None:
        """
        Turn on gripper LED.
        """
        print("💡 Turning gripper LED on")
        self.socket.send(create_command(
            '$ 3 "rq_gripper_led_on()"\n   rq_gripper_led_on()').encode("utf8"))

    def gripper_led_off(self) -> None:
        """
        Turn off gripper LED.
        """
        print("💡 Turning gripper LED off")
        self.socket.send(create_command(
            '$ 3 "rq_gripper_led_off()"\n   rq_gripper_led_off()').encode("utf8"))

    def move_and_wait_mm(self, distance: float) -> None:
        """
        Open gripper by position parameter in milimeters.
        :param distance: distance between gripper fingers
        """
        if 0 <= distance:
            print(f"🚀 Oppening gripper to {distance} mm")
            self.socket.send(create_command(
                '  $ 3 "rq_move_and_wait_mm(' + str(distance) + ')"\n   rq_move_and_wait_mm(' + str(distance) + ')').encode("utf8"))
        else:
            raise ValueError("Position is out of range.")

    def reset(self) -> None:
        """
        Reset gripper.
        """
        print("🔄 Resetting gripper")
        self.socket.send(create_command(
            '$ 3 "rq_reset()"\n   rq_reset()').encode("utf8"))

    def get_socket(self) -> socket:
        """
        Return socket instance.
        """
        return self.socket

    def move_j(self, joints_angles_degrees: List[float], acceleration: float = 1.0, speed: float = 1.0) -> None:
        """
        Move robot with J move.
        :param joints_angles: float list of size 6 with joints angles in degrees
        :param acceleration: acceleration of the robotic arm in radians per second
        :param speed: speed of the robotic arm in radians per second
        """
        if len(joints_angles_degrees) == 6:
            joints_angles_radians: List[float] = []

            for angle in joints_angles_degrees:
                joints_angles_radians.append(math.radians(angle))

            print("🦾 Moving robot with J move")
            self.socket.send(create_command(
                f'  movej({str(joints_angles_radians)}, a={str(acceleration)}, v={str(speed)})').encode("utf8"))
        else:
            raise ValueError("Move J parameter must be float list of size 6!")

    def move_l(self, coordinates: List[float], rotation_vector: List[float], acceleration: float = 0.5, speed: float = 0.5) -> None:
        """
        Move robot with L move
        :param coordinates: float list of size 3 with BASE coordinates in meters [x, y, z]
        :param rotation_vector: float list of size 3 with rotation vector in radians [rx, ry, rz]
        :param acceleration: acceleration of the robotic arm in radians per second
        :param speed: speed of the robotic arm in radians per second
        """

        if len(coordinates) == 3 and len(rotation_vector) == 3:
            coordinates_with_rotation_vector = coordinates + rotation_vector

            print("🦾 Moving robot with L move")
            self.socket.send(create_command(
                f'  movel(p{str(coordinates_with_rotation_vector)}, a={str(acceleration)}, v={str(speed)})').encode("utf8"))
        else:
            raise ValueError(
                "Move L parameters must be two float lists of size 3!")
