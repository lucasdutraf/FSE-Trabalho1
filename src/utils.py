from datetime import datetime, timedelta
import RPi.GPIO as GPIO
from time import sleep
from typing import Tuple

from constants import TRAFFIC_LIGHTS, LIGHTS_TIME_COUNT

def get_traffic_lights_set_list(cross: str, traffic_flow: str) -> list:
    lights_gpio = TRAFFIC_LIGHTS[cross][traffic_flow]
    lights_list = []
    for lights in lights_gpio:
        lights_list.append(lights_gpio[lights])

    return lights_list

def get_traffic_lights_set(cross: str, traffic_flow: str) -> list:
    lights_gpio = TRAFFIC_LIGHTS[cross][traffic_flow]

    return lights_gpio

def get_traffic_lights_max_time(cross: str, traffic_flow: str) -> int:
    lights_gpio = get_traffic_lights_set(cross, traffic_flow)

def get_traffic_lights_active_time(color: str, traffic_flow: str) -> Tuple[datetime, datetime]:
    active_time = LIGHTS_TIME_COUNT[color][traffic_flow]
    min_time = datetime.now() + timedelta(seconds=active_time["min"])
    max_time = datetime.now() + timedelta(seconds=active_time["max"])

    return min_time, max_time

def turn_on_emergency_mode() -> None:
    execution_time_min, _ = get_traffic_lights_active_time("green", "1")
    c_1_green_light_pin = TRAFFIC_LIGHTS["C_1"]["1"]["green"]
    c_2_green_light_pin = TRAFFIC_LIGHTS["C_2"]["1"]["green"]
    while True:
        if datetime.now() >= execution_time_min:
            break
        GPIO.output(c_1_green_light_pin, 1)
        GPIO.output(c_2_green_light_pin, 1)
    GPIO.output(c_1_green_light_pin, 0)
    GPIO.output(c_2_green_light_pin, 0)

def turn_on_night_mode() -> None:
    execution_time_min, _ = get_traffic_lights_active_time("yellow", "1")
    c_1_main_yellow_light_pin = TRAFFIC_LIGHTS["C_1"]["1"]["yellow"]
    c_1_aux_yellow_light_pin = TRAFFIC_LIGHTS["C_1"]["2"]["yellow"]
    c_2_main_yellow_light_pin = TRAFFIC_LIGHTS["C_2"]["1"]["yellow"]
    c_2_aux_yellow_light_pin = TRAFFIC_LIGHTS["C_2"]["2"]["yellow"]
    while True:
        if datetime.now() >= execution_time_min:
            break
        GPIO.output(c_1_main_yellow_light_pin, 1)
        GPIO.output(c_1_aux_yellow_light_pin, 1)
        GPIO.output(c_2_main_yellow_light_pin, 1)
        GPIO.output(c_2_aux_yellow_light_pin, 1)
        sleep(1)
        GPIO.output(c_1_main_yellow_light_pin, 0)
        GPIO.output(c_1_aux_yellow_light_pin, 0)
        GPIO.output(c_2_main_yellow_light_pin, 0)
        GPIO.output(c_2_aux_yellow_light_pin, 0)