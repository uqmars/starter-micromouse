from machine import Pin, PWM
import time

# Constants
MOTOR_FREQ = 2000

# Setting up LEDs 
LED_RED = Pin(9, Pin.OUT)
LED_GREEN = Pin(10, Pin.OUT)

# Setting up sensors
BUTTON = Pin(11, Pin.IN)
IR_1 = Pin(12, Pin.IN)
IR_2 = Pin(13, Pin.IN)
IR_3 = Pin(14, Pin.IN)

# Setting up motor pins
MOTOR_1_A = PWM(Pin(21), freq=MOTOR_FREQ)
MOTOR_1_B = PWM(Pin(20), freq=MOTOR_FREQ)
MOTOR_2_A = PWM(Pin(18), freq=MOTOR_FREQ)
MOTOR_2_B = PWM(Pin(17), freq=MOTOR_FREQ)
MOTOR_1_INVERT = False
MOTOR_2_INVERT = True

# Setting up the motor encoders
ENCODER_1_A = Pin(19, Pin.IN, )
ENCODER_1_B = Pin(22, Pin.IN)
ENCODER_2_A = Pin(14, Pin.IN)
ENCODER_2_B = Pin(13, Pin.IN)

encoder_1_counter = 0
def handler(p):
    print("hi")
    global encoder_1_counter
    if ENCODER_1_A.value():
        encoder_1_counter -= 1
    else:
        encoder_1_counter += 1
    print("Encoder counter:", encoder_1_counter)

ENCODER_1_B.irq(handler, Pin.IRQ_FALLING)

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def drive_motor(motor, power):
    # Power calculations
    limited_power = constrain(power, -255, 255)
    channel_A_power = 0
    channel_B_power = abs(limited_power)
    if (limited_power > 0):
        channel_A_power = limited_power
        channel_B_power = 0
    # Motor selection
    if motor not in range(1,3):
        return -1
    if motor == 1:
        if not MOTOR_1_INVERT:
            MOTOR_1_A.duty_u16(channel_A_power * 257)
            MOTOR_1_B.duty_u16(channel_B_power * 257)
        else:
            MOTOR_1_A.duty_u16(channel_B_power * 257)
            MOTOR_1_B.duty_u16(channel_A_power * 257)
    else:
        if not MOTOR_2_INVERT:
            MOTOR_2_A.duty_u16(channel_A_power * 257)
            MOTOR_2_B.duty_u16(channel_B_power * 257)
        else:
            MOTOR_2_A.duty_u16(channel_B_power * 257)
            MOTOR_2_B.duty_u16(channel_A_power * 257)
        
LED_RED.on()
drive_motor(1,-255)
time.sleep(1)
drive_motor(1,0)
LED_RED.off()
time.sleep(1)
while(1):
    print(encoder_1_counter)