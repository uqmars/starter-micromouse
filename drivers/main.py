"""
This file is provided as a sample of basic initialisation and working for
"plug-and-play" of the drivers, but is expected to be altered to implement
system control algorithms.
"""
from micromouse import Micromouse

mm = Micromouse()


if __name__ == "__main__":
    while True:
        if mm.button.value() > 0:
            mm.drive_stop()
        else:
            mm.drive_forward()
