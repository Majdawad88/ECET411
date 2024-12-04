import RPi.GPIO as GPIO
from time import sleep
#GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)
Button = 26
LED = 21
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)
pi_pwm = GPIO.PWM(LED,100)
pi_pwm.start(0)
while True:
        button_state = GPIO.input(Button)
#       print('button_state = ',button_state)
        if button_state == 0:
                print(button_state)
                pi_pwm.ChangeDutyCycle(100)
                print('100%')
                sleep(1)
                pi_pwm.ChangeDutyCycle(75)
                print('75%')
                sleep(1)
                pi_pwm.ChangeDutyCycle(50)
                print('50%')
                sleep(1)
                pi_pwm.ChangeDutyCycle(25)
                print('25%')
                sleep(1)
                pi_pwm.ChangeDutyCycle(0)
                print('0%')
                sleep(1)
        if button_state == 1:
                print('button_state = ',button_state)
                GPIO.output(LED,False)
                print('LED OFF')
                sleep(1)
