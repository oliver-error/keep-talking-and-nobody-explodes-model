from bitstring import BitArray
import machine
from machine import Pin
import time
import math

# a file for 5 pin communication
ON = 1
OFF = 0

def send(data: BitArray, clock_speed: int, data_pin: Pin, clock_pin: Pin) -> bool:
    """send a message over specified pin returns sucess"""
    for bit in data:
        clock_pin.value(ON)
        data_pin.value(bit)
        machine.lightsleep(clock_speed/2)
        clock_pin.value(OFF)
        machine.lightsleep(clock_speed/2)
    return True

def recive(data_pin: Pin, clock_pin: Pin) -> tuple:
    """recive a message over specified pin returns message, clock_speed, sucess"""
    data = BitArray()
    clock_speed = 0
    last_time = 0
    while not clock_pin.value():
        machine.lightsleep(10)
        last_time = math.floor(time.time() * 1000)

    for i in range(5):
        current_time = math.floor(time.time() * 1000)
        clock_speed = current_time - last_time
        data.append(data_pin.value())
        while clock_pin.value():
            machine.lightsleep(10)
        while not clock_pin.value():
            machine.lightsleep(10)
        last_time = current_time
    
    return (data, clock_speed, True)