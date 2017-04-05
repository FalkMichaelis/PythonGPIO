import RPi.GPIO as GPIO


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN) #Knopf links
GPIO.setup(12, GPIO.IN) #Knopf rechts
GPIO.setup(40, GPIO.OUT) #rote led
GPIO.setup(37, GPIO.OUT) #gruene led

while True:
  if not GPIO.input(16):
	GPIO.output(37, GPIO.HIGH) #gruen aus
    GPIO.output(40, GPIO.LOW) #rot an
  if not GPIO.input(40)
	GPIO.output(40, GPIO.HIGH) #rot aus
	GPIO.output(37, GPIO.LOW) #gruen an

GPIO.cleanup() 
