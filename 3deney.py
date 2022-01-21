import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 16
ECHO = 18
led_sol = 29
led_orta = 31
led_sag  = 33
buzzer  = 37

GPIO.setup(led_sol,GPIO.OUT)
GPIO.setup(led_orta,GPIO.OUT)
GPIO.setup(led_sag,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:

  GPIO.output(TRIG, False)
  print ("Olculuyor...")
  time.sleep(0.5)
     
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150
  distance = round(distance, 2)
#   print("Mesafe:",distance - 0.5,"cm")
  
  if distance < 11:
      
    
     GPIO.output(buzzer,1)
     GPIO.output(led_sol,1)
     GPIO.output(led_orta,1)
     GPIO.output(led_sag,1)
     time.sleep(0.5)
     GPIO.output(buzzer,0)
     GPIO.output(led_sol,0)
     GPIO.output(led_orta,0)
     GPIO.output(led_sag,0)
     time.sleep(0.5)
     print("Mesafe:",distance - 0.5,"cm")
     
  elif distance > 10 and distance < 21:
      
     GPIO.output(buzzer,1)
     GPIO.output(led_sol,1)
     GPIO.output(led_orta,1)
     GPIO.output(led_sag,0)
     time.sleep(0.5)
     GPIO.output(buzzer,0)
     GPIO.output(led_sol,0)
     GPIO.output(led_orta,0)
     time.sleep(0.5)
     print("Mesafe:",distance - 0.5,"cm")
     
  elif distance > 20 and distance < 30:
      
     GPIO.output(buzzer,1)
     GPIO.output(led_sol,1)
     GPIO.output(led_orta,0)
     GPIO.output(led_sag,0)
     time.sleep(0.5)
     GPIO.output(buzzer,0)
     GPIO.output(led_sol,0)
     time.sleep(0.2)
     print("Mesafe:",distance - 0.5,"cm")

  else:
     GPIO.output(buzzer,0)
     GPIO.output(led_sol,0)
     GPIO.output(led_orta,0)
     GPIO.output(led_sag,0)
     print ("Menzil asildi")
