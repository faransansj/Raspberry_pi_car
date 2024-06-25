import RPi.GPIO as GPIO
from time import sleep
import math
'''
\\\\\\\\\\\\\\\\\\\\\\\\\
\\ PID control setting \\
\\\\\\\\\\\\\\\\\\\\\\\\\
'''
# PID parameter
Kp = 0.4      # Proportional
Ki = 0.0      # Integral
Kd = Kp*0.65  # Derivative

# PID value
integral = 0
last_error = 0

# calculate pid
def calculate_pid(setpoint, measured_value):
    global integral, last_error
    # Calculate error
    error = setpoint - measured_value
    
    P_out = Kp * error

    integral += error
    I_out = Ki * integral

    derivative = error - last_error
    D_out = Kd * derivative

    # Total output
    output = P_out + I_out + D_out
    # Save error for next loop
    last_error = error

    return output
    
# motor state
STOP = 0
FORWARD = 1
BACKWARD = 2

# motor channel state
CH1 = 0
CH2 = 1

# Define pin (BCM)
# DC motor driver pin
ENA = 26
ENB = 0

IN1 = 19
IN2 = 13
IN3 = 6
IN4 = 5
# servo motor pin
servoPIN = 17

# motor value collection 
# motor_A_value 
# motor_B_value 

#pin setting function 
def setPinConfig(EN, INA, INB):
    #set DC motor pinconfig
             
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # 100khz activate 
    pwm = GPIO.PWM(EN, 100) 
    # stop PWM    
    pwm.start(0) 
    return pwm

    #set Servo motor pinconfig
    GPIO.setup(servoPIN,GPIO.OUT)
    # GPIO 17 for PWM with 50Hz
    servo = GPIO.PWM(servoPIN, 50) 
    # Initialization
    servo.start(2.5) 

# motor control function
def setMotorContorl(pwm, INA, INB, speed, stat):

    #motor  PWM
    pwm.ChangeDutyCycle(speed)  
    
    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
        
    elif stat == BACKWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)
        
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)

def setMotor(ch, speed, stat):
    if ch == CH1:
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        setMotorContorl(pwmB, IN3, IN4, speed, stat)
  

# set gpio mode 
GPIO.setmode(GPIO.BCM)
      
# set motor pin 
# get pwm handdle  
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

# 앞으로 80프로 속도로
setMotor(CH1, 80, FORWARD)
setMotor(CH2, 80, FORWARD)
#5초 대기
sleep(5)

# 뒤로 40프로 속도로
setMotor(CH1, 40, BACKWARD)
setMotor(CH2, 40, BACKWARD)
sleep(5)

# 뒤로 100프로 속도로
setMotor(CH1, 100, BACKWARD)
setMotor(CH2, 100, BACKWARD)
sleep(5)

#정지 
setMotor(CH1, 80, STOP)
setMotor(CH2, 80, STOP)

# 종료
GPIO.cleanup()
