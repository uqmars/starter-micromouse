"""
Filename: motor.py
Author: Quinn Horton, UQ Mechatronics and Robotics Society
Date: 03/01/2025
Version: 0.5
Description: Provides a software abstraction for the system motors.
License: MIT License
"""
from machine import Pin


class Motor():
    """
    Represents the physical GA12-N20 motors in code.

    Parameters:
        m1_pin (int): The pin number used to drive the motor forward.
        m2_pin (int): The pin number used to drive the motor backward.
        e1_pin (int): The pin number used for the forward leading encoder
            signal.
        e1_pin (int): The pin number used for the forward lagging encoder
            signal.
    """

    def __init__(self, m1_pin, m2_pin, e1_pin, e2_pin):
        """
        Initialises the member variables upon first creation.
        """
        self.m1 = Pin(m1_pin, Pin.OUT)
        self.m2 = Pin(m2_pin, Pin.OUT)
        self.e1 = Pin(e1_pin, Pin.IN)
        self.e2 = Pin(e2_pin, Pin.IN)

    def spin_forward(self):
        """
        Turns on the motor to spin in the forward direction.
        """
        self.m1.on()
        self.m2.off()

    def spin_backward(self):
        """
        Turns on the motor to spin in the reverse direction.
        """
        self.m2.on()
        self.m1.off()

    def spin_stop(self):
        """
        Turns off the motor.
        """
        self.m1.off()
        self.m2.off()

    def encoder_read(self):
        """
        Reads the current encoder value.

        Returns:
            int: The rotational frequency of the motor (signed for direction).
        """
        return 0
