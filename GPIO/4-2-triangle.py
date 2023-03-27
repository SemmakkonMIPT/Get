import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


def ToBin(a, n):
    return [int(elem) for elem in bin(a)[2:].zfill(n)]


T = float(input("input time "))

try:
    while (True):
        for i in range(256):
            GPIO.output(dac, ToBin(i, 8))
            sleep(T / 256)

except ValueError:
    print('input number 0-255 ')
except KeyboardInterrupt:
    print('done')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()