
# Online Python - IDE, Editor, Compiler, Interpreter

import time 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BM)
motorForward = 13
motorReverse = 19
GPIO.setup(motorForward, GPIO.OUT)
GPIO.setup(motorReverse, GPIO.OUT)
def motorDrive(Dir)
    if Dir == 'F'
        GPIO.output(motorForward, True)
        GPIO.output(motorReverse, False)
        
    if Dir == 'R'
        GPIO.output(motorForward, False)
        GPIO.output(motorReverse, True)
        
    if Dir == 'S'
        GPIO.output(motorForward, False)
        GPIO.output(motorReverse, False)
        
while True:
    
    motorDrive('F')
    sleep(5)
    motorDrive('S')
    sleep(5)
    motorDrive('R')
    sleep(5)
    motorDrive('S')

