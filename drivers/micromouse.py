"""
Filename: micromouse.py
Author: Quinn Horton, UQ Mechatronics and Robotics Society
Date: 20/12/2025
Version: 0.1
Description: Provides a software abstraction for the Micromouse robot.
License: MIT License
"""
from machine import Pin, Timer


class Micromouse():
    """
    Represents the physical Micromouse device in code.
    Implemented as a singleton class, as the code should only know of the
    device it is running on.
    """
    def __new__(cls):
        """
        Creates instances of the class. Used here to ensure the object is a
        singleton.

        Parameters:
            cls (type): The class itself.

        Returns:
            Micromouse: The single instance of the class.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Micromouse, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        """
        Initialises the member variables upon first creation.
        """
        if hasattr(self, 'exists'):
            return
        self.exists = True
        self.green_led = Pin(10, Pin.OUT)
        self.red_led = Pin(9, Pin.OUT)
        self.tim = Timer()

    def toggle_leds(self):
        self.green_led.toggle()
        self.red_led.toggle()

    def start_led_toggle(self):
        self.tim.init(mode=Timer.PERIODIC, freq=10,
                      callback=lambda t: self.toggle_leds())

    def stop_led_toggle(self):
        self.tim.deinit()
