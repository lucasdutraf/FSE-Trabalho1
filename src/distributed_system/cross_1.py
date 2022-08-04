import socket

from src.constants import CROSS_1_PORT, LOCAL_IP
from src.distributed_system.utils import turn_on_night_mode, turn_on_emergency_mode

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((LOCAL_IP, CROSS_1_PORT))
    server.listen(3)

    while True:
        client, address = server.accept()

        print(f"Connection Established - {address[0]}:{address[1]}")
        string = client.recv(1024)
        string = string.decode("utf-8")

        print(f"Received {string}")
        if string == "1":
            turn_on_night_mode()
        elif string == "2":
            turn_on_emergency_mode()
