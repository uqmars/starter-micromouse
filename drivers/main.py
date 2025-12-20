"""
This file is provided as a sample of basic initialisation and working for
"plug-and-play" of the drivers, but is expected to be altered to implement
system control algorithms.
"""
from micromouse import Micromouse

mm = Micromouse()
state = 0


def strobing(t):
    global mm, state
    mm.green_led.value((state & 1))
    mm.red_led.value((state >> 1) & 1)
    state = (state + 1) % 4


if __name__ == "__main__":
    mm.tim.init(freq=1, callback=strobing)
