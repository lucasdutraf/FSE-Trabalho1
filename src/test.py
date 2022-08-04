import RPi.GPIO as GPIO
from time import sleep
from utils import get_traffic_lights_set

GPIO.setmode(GPIO.BCM)

test = get_traffic_lights_set("C_2", "1")

# pins = [17, 27, 22]

GPIO.setup(test, GPIO.OUT)

GPIO.output(test, 0)

# Exercicio 1-A
for pin in test:
 GPIO.output(pin, 1)
 sleep(1)
 GPIO.output(pin, 0)

# Exercicio 1-B

# 1:1
# for pin in pins:
#  GPIO.output(pin, 1)
#  sleep(1)
#  GPIO.output(pin, 0)

# sleep(1)

# # 2:2
# for _ in range(0, 1):
#  GPIO.output(pins[_], 1)
#  GPIO.output(pins[_ + 1], 1)
#  sleep(1)
#  GPIO.output(pins[_], 0)
#  GPIO.output(pins[_ + 1], 0)

# sleep(1)

# # 3:3
# GPIO.output(pins, 1)
# sleep(1)
# GPIO.output(pins, 0)


GPIO.cleanup()