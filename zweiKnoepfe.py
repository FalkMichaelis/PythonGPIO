import RPi.GPIO as GPIO


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN)
GPIO.setup(40, GPIO.IN)

while True:
  if not GPIO.input(11):
    print "Links wurde gedrueckt"
  if not GPIO.input(40)
	print "Rechts wurde gedrueckt"

GPIO.cleanup() 

