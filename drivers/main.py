"""
This file is provided as a sample of basic initialisation and working for
"plug-and-play" of the drivers, but is expected to be altered to implement
system control algorithms.
"""
from micromouse import Micromouse
from machine import Pin

mm = Micromouse()


def left_light(t):
    mm.led_red_set(t.value())


def mid_light(t):
    mm.led_green_set(t.value())


def right_light(t):
    mm.led_debug_set(t.value())


if __name__ == "__main__":
    mm.left_ir.irq(handler=left_light,
                   trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
    mm.mid_ir.irq(handler=mid_light,
                  trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
    mm.right_ir.irq(handler=right_light,
                    trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
    while True:
        if mm.button.value() > 0:
            mm.drive_stop()
        else:
            mm.drive_forward()
