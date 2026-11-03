from bitstring import BitArray
from machine import Pin
import time
# a file  for 5 pin communication

def send(data: BitArray, clock_speed: int, data_pin: Pin, clock_pin: Pin) -> bool:
    """send a message over specified pin returns sucess"""
    return True

def recive(data_pin: Pin, clock_pin: Pin) -> tuple:
    """recive a message over specified pin returns message, clock_speed, sucess"""
    return (data, clock_speed, True)