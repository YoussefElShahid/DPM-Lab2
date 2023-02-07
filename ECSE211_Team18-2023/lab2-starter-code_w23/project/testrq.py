from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor,reset_brick

try:
    while True:
        print(EV3ColorSensor(2).get_value())
            
except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    exit()