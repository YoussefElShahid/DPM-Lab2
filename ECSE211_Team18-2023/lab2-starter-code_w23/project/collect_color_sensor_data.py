#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor,reset_brick
from time import sleep


COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"

# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(2)
TOUCH_SENSOR = TouchSensor(1)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    "Collect color sensor data."
    try:
        output_file=open(COLOR_SENSOR_DATA_FILE,'w')
        while True:
            col_data=COLOR_SENSOR.get_value()
            if TOUCH_SENSOR.is_pressed():
                while col_data==None:
                    col_data=COLOR_SENSOR.get_value()
                for i in range (1):
                    print(col_data)
                    output_file.write(f"{col_data}\n")
                    sleep(0.75)
                    
                        
    except BaseException:
        pass  
    finally:
        print('done')
        output_file.close()
        reset_brick()
        exit()


if __name__ == "__main__":
    collect_color_sensor_data()
