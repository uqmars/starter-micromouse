"""
Filename: micromouse.py
Author: Quinn Horton, UQ Mechatronics and Robotics Society
Date: 03/01/2025
Version: 0.5
Description: Provides a software abstraction for the Micromouse robot.
License: MIT License
"""
from machine import Pin, Timer
from motor import Motor


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

        # Inputs
        self.button = Pin(11, Pin.IN)
        self.left_ir = Pin(12, Pin.IN)
        self.mid_ir = Pin(13, Pin.IN)
        self.right_ir = Pin(14, Pin.IN)

        # Outputs
        self.green_led = Pin(10, Pin.OUT)
        self.red_led = Pin(9, Pin.OUT)
        self.debug_led = Pin(25, Pin.OUT)
        self.left_motor = Motor(17, 18, 15, 16)
        self.right_motor = Motor(21, 20, 19, 22)

        # Other
        self.blink_timer = Timer()

    def led_set(self, red_val, green_val):
        """
        Set both red and green LEDs to provided values.

        Parameters:
            red_val (bool): The desired state of the red led.
            green_val (bool): The desired state of the green led.
        """
        self.green_led.value(green_val)
        self.red_led.value(red_val)

    def led_green_set(self, value):
        """
        Set the green LED to the provided value.

        Parameters:
            value (bool): The desired state of the green led.
        """
        self.green_led.value(value)

    def led_red_set(self, value):
        """
        Set the red LED to the provided value.

        Parameters:
            value (bool): The desired state of the red led.
        """
        self.red_led.value(value)

    def led_debug_set(self, value):
        """
        Set the debug LED to the provided value.

        Parameters:
            value (bool): The desired state of the debug led.
        """
        self.debug_led.value(value)

    def led_toggle(self):
        """
        Toggle both red and green LEDs when called.
        """
        self.green_led.toggle()
        self.red_led.toggle()

    def led_toggle_start(self, frequency=1):
        """
        Initialise an LED blinking timer for the red and green LEDs.

        Parameters:
            frequency (int, optional): The frequency at which the LEDs should
            blink.
        """
        self.blink_timer.init(mode=Timer.PERIODIC, freq=frequency,
                              callback=lambda t: self.led_toggle())

    def led_toggle_stop(self):
        """
        Stop the blinking of the onboard red and green LEDs and turn them off.
        """
        self.blink_timer.deinit()
        self.red_led.off()
        self.green_led.off()

    def drive_forward(self):
        """
        Turn both motors on to drive forward at full speed.
        """
        self.left_motor.spin_forward()
        self.right_motor.spin_forward()

    def drive_backward(self):
        """
        Turn both motors on to drive backward at full speed.
        """
        self.left_motor.spin_backward()
        self.right_motor.spin_backward()

    def drive_stop(self):
        """
        Turn off both motors.
        """
        self.left_motor.spin_stop()
        self.right_motor.spin_stop()

    def encoders_get(self):
        """
        Get the rotational frequency of both motor encoders, signed for
            direction.

        Returns:
            (int, int): The left and right encoder readings respectively.
        """
        left_enc = self.left_motor.encoder_read()
        right_enc = self.right_motor.encoder_read()
        return (left_enc, right_enc)
