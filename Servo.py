import RPi.GPIO as GPIO
import time 

btnarti=8
btneksi=10
btnorta=12
servo = 11
deger=2.5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(btnarti, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(btneksi, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(btnorta, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
p = GPIO.PWM(servo, 50)
p.start(deger) 
try:
  while True:
    artideger=GPIO.input(btnarti)  
    eksideger=GPIO.input(btneksi)  
    ortadeger=GPIO.input(btnorta) 
    if artideger==False:
        deger+=0.2  
        time.sleep(0.3)
    elif eksideger ==False:
        deger-=0.2
        time.sleep(0.3)
    elif ortadeger == False:
        deger=7.7
    if deger>12.5:
        deger=12.5
    elif deger<2.5:
        deger=2.5
    p.ChangeDutyCycle(deger)
    print(deger)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

