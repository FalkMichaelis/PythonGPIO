import time
import RPi.GPIO as GPIO

# Pin-Nummern wie auf dem Raspberry Board verwenden
GPIO.setmode(GPIO.BOARD)

# setzt Pin 2 als Output
GPIO.setup(2, GPIO.OUT)

# Dauersschleife 
while 1:
  # LED aus
  GPIO.output(2, GPIO.LOW)
  # eine Sekunde warten
  time.sleep(1)
  # LED an
  GPIO.output(2, GPIO.HIGH)
  # eine Sekunde warten
  time.sleep(1)
