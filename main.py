# Sofia Seppälä
# Three-point turn assignment
# 13.10.2026

# import pin from machine module
from machine import Pin, PWM
from time import sleep

# Motor A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Set PWM frequency to 1000 Hz
e1.freq(1000)
e2.freq(1000)

# 5 second timeout
sleep(5)

m1.value(1)
m2.value(1)

# move forward approx. 1 meter
e1.duty_u16(32767)
e2.duty_u16(32767)
sleep(2)
    

# reverse left, to horizontal position
m1.value(0)
m2.value(0)
e2.duty_u16(10000)
e1.duty_u16(30000)
sleep(2)


# move forward, and turn 90 degrees to the right
m1.value(1)
m2.value(1)

# Turn right 90 degrees
e1.duty_u16(0)
e2.duty_u16(30000)
sleep(1.8)


# move forward approx. 1 meter
e1.duty_u16(32767)
e2.duty_u16(32767)
sleep(2)

#stop motors
e1.duty_u16(0)
e2.duty_u16(0)