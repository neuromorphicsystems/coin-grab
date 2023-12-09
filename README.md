# coin-grab

## Setup

```sh
git clone https://github.com/neuromorphicsystems/coin-grab
python3 -m venv .venv
source .venv/bin/activate # .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Linux users must run the extra command: `neuromorphic-drivers-install-udev-rules`.

Windows users install libusb drivers with https://zadig.akeo.ie.

macOS users do not need to run any extra commands.

## Hardware

The motor's brown cable muust be connected to the Arduino ground, and the orange cable to pin 52.

## Test the actuator

```sh
python test_actuator.py
```

## Implement a coin detection algorithm

Edit *coin_grab.py* (line 17).

```sh
python test_actuator.py
```

## Arduino

Only required to re-flash the Arduino firmware.

Install the Arduino CLI (https://github.com/arduino/arduino-cli).

```sh
cd arduino
arduino-cli core install arduino:avr
arduino-cli compile --fqbn arduino:avr:mega
arduino-cli board list # find the port of Arduino Mega
arduino-cli upload --port /dev/cu.usbmodem14101 --fqbn arduino:avr:mega
```
