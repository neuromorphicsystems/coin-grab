import serial
import time


class Grabber:
    def __init__(self, port: str) -> None:
        self.serial = serial.Serial(port, baudrate=115200, timeout=1.0)
        time.sleep(1.0)

    def move(self, position: int):
        assert position >= 0 and position <= 3000
        self.serial.write(bytes([position & 0xFF, (position >> 8) & 0xFF]))

    def open(self, position=1500):
        self.move(position=position)

    def close(self, position=1200):
        self.move(position=position)
