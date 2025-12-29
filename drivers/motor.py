"""
Filename: motor.py
Author: Quinn Horton, UQ Mechatronics and Robotics Society
Date: 29/12/2025
Version: 0.1
Description: Provides a software abstraction for the system motors.
License: MIT License
"""
from machine import Pin, Timer


class Motor():
    """
    Represents the physical GA12-N20 motors in code.
    """

    def __init__(self, m1_pin, m2_pin):
        """
        Initialises the member variables upon first creation.
        """
        self.m1 = Pin(m1_pin, Pin.OUT)
        self.m2 = Pin(m2_pin, Pin.OUT)

    def spin_forward(self):
        self.m1.on()
        self.m2.off()

    def spin_backward(self):
        self.m2.on()
        self.m1.off()

    def spin_stop(self):
        self.m1.off()
        self.m2.off()
