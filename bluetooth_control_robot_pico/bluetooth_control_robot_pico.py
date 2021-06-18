from machine import Pin,PWM,UART #importing PIN and PWM
import time #importing time

#Defining UART channel and Baud Rate
uart= UART(0,9600)

# Defining motor pins
motor1=Pin(10,Pin.OUT)
motor2=Pin(11,Pin.OUT)
motor3=Pin(12,Pin.OUT)
motor4=Pin(13,Pin.OUT)
# Defining enable pins and PWM object
enable1=PWM(Pin(6))
enable2=PWM(Pin(7))

# Defining frequency for enable pins
enable1.freq(1000)
enable2.freq(1000)

# Setting maximum duty cycle for maximum speed (0 to 65025)
enable1.duty_u16(65025)
enable2.duty_u16(65025)

# Forward
def move_forward():
    motor1.high()
    motor2.low()
    motor3.low()
    motor4.high()
    
# Backward
def move_backward():
    motor1.low()
    motor2.high()
    motor3.high()
    motor4.low()
    
#Turn Right
def turn_right():
    motor1.low()
    motor2.high()
    motor3.low()
    motor4.high()
    
#Turn Left
def turn_left():
    motor1.high()
    motor2.low()
    motor3.high()
    motor4.low()
    
#Stop
def stop():
    motor1.low()
    motor2.low()
    motor3.low()
    motor4.low()

while True:
    if uart.any(): #Checking if data available
        data=uart.read() #Getting data
        data=str(data) #Converting bytes to str type
        print(data)
        if('F' in data):
            move_forward() #Forward
        elif('B' in data):
            move_backward() #Backward
        elif('R' in data):
            turn_right() #Turn Right
        elif('L' in data):
            turn_left() #Turn Left
        elif('S' in data):
            stop() #Stop
        elif('E' in data):
            speed=data.split("|")
            print(speed[1])
            enable1.duty_u16(int(speed[1])) #Setting Duty Cycle
            enable2.duty_u16(int(speed[1])) #Setting Duty Cycle
        else:
            stop() #Stop
    