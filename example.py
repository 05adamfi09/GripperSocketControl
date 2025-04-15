import socket
import time
from gripper_methods import *

# CONSTANTS INIT

HOST = "192.168.0.96"
PORT = 30002

# INIT SOCKET
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# RUN PROGRAM

time.sleep(1)
open_and_wait(s=s)
close_and_wait(s=s)
current_pos_mm(s=s)
time.sleep(1)
s.close()
