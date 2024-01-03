import RPi.GPIO as GPIO
from gpiozero import Motor 
import time

# Servo motor setting 
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

# DC motor setting 
motor_R = Motor(16,19)
motor_L = Motor(21,20)

while True:
    try:
        # Servo motor control
        angle = float(input("Enter angle (0 to 90): "))
        if 0 <= angle <= 90:
            duty = angle / 18.0 + 2.5
            p.ChangeDutyCycle(duty)
        else:
            print("Angle out of range.")

        # DC motor control
        dc1 = float(input("Enter speed for DC Motor 1 (-1 to 1): "))
        dc2 = float(input("Enter speed for DC Motor 2 (-1 to 1): "))

        # DC1 control
        if -1 <= dc1 <= 1:
            if dc1 > 0:
                motor_R.forward(dc1)
            elif dc1 < 0:
                motor_R.backward(abs(dc1))
            else:
                motor_R.stop()
        else:
            print("Speed for Motor 1 out of range.")

        # DC2 control
        if -1 <= dc2 <= 1:
            if dc2 > 0:
                motor_L.forward(dc2)
            elif dc2 < 0:
                motor_L.backward(abs(dc2))
            else:
                motor_L.stop()
        else:
            print("Speed for Motor 2 out of range.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
