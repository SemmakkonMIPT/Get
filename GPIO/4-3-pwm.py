import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
if input() == '0':
        pwm=GPIO.PWM(24, 1000)
else:
        pwm=GPIO.PWM(2, 1000)
pwm.start(0)

try:
        while True:
                DutyCicle=int(input("input dutycycle "))
                pwm.ChangeDutyCycle(DutyCicle)
                print("{:.2f}".format(DutyCicle*3.3/100))
except KeyboardInterrupt:
    print('done')
finally:
    GPIO.output(24, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()