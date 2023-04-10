import RPi.GPIO as gpio
import sys
from time import sleep

gpio.setmode(gpio.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)


def ToBin(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]


def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2 ** i
        gpio.output(dac, ToBin(k))
        sleep(0.01)
        if gpio.input(comp) == 0:
            k -= 2 ** i
    return k


def func(k, n):
    x = round(k / n * 8)
    ans = [0 for i in range(8)]
    for i in range(x):
        ans[i] = 1
    return ans


try:
    while True:
        k = adc()
        if k != 0:
            gpio.output(leds, func(k, 65))
            print(k, '{:.2f}v'.format(3.3 * k / 256))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()