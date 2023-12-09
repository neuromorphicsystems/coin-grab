import actuator

grabber = actuator.Grabber(port="/dev/cu.usbmodem14201")

print("press o to open, c to close, q to quit")
while True:
    command = input()
    if command == "c":
        grabber.close()
    elif command == "o":
        grabber.open()
    elif command == "q":
        grabber.open()
        break
    else:
        print("press o to open, c to close, q to quit")
