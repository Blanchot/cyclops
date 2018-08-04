# First experiments with infrared Lisiparoi flash

import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.LOW)

def flashon():
  time.sleep(5)
  GPIO.output(4, GPIO.HIGH)
  print('Flash on')
  time.sleep(10)
  GPIO.output(4, GPIO.LOW)
  print('Flash off')


def tidyup():
  GPIO.cleanup()


