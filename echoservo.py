# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 19:39:28 2021

@author: alper-aktas
"""

# -- coding: utf-8 --
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def echoservo():
    servo = 17
    deger=2.5
    p = GPIO.PWM(servo, 50)
    p.start(deger)
    GPIO.setup(servo, GPIO.OUT) 
    while True:
        
        if distance < 11:
             deger=2.5
             deger+=0.2
             GPIO.output(buzzer,1)
             GPIO.output(led_sol,1)
             GPIO.output(led_orta,1)
             GPIO.output(led_sag,1)
             time.sleep(0.05)
             GPIO.output(buzzer,0)
             GPIO.output(led_sol,0)
             GPIO.output(led_orta,0)
             GPIO.output(led_sag,0)
             time.sleep(0.03)
             print("Mesafe:",distance - 0.5,"cm değer: "+str(deger))
         
        elif  10>distance < 21:
             deger-=0.2 
             GPIO.output(buzzer,1)
             GPIO.output(led_sol,1)
             GPIO.output(led_orta,1)
             GPIO.output(led_sag,0)
             time.sleep(0.05)
             GPIO.output(buzzer,0)
             GPIO.output(led_sol,0)
             GPIO.output(led_orta,0)
             time.sleep(0.1)
         
         
             print("Mesafe:",distance - 0.5,"cm değer: "+str(deger))
        elif 20> distance < 30:
             deger+=0.2
             GPIO.output(buzzer,1)
             GPIO.output(led_sol,1)
             GPIO.output(led_orta,0)
             GPIO.output(led_sag,0)
             time.sleep(0.05)
             GPIO.output(buzzer,0)
             GPIO.output(led_sol,0)
             time.sleep(0.2)
        elif 29>distance<50:
             deger=7.5
             GPIO.output(buzzer,1)
             GPIO.output(led_sol,1)
             GPIO.output(led_orta,0)
             GPIO.output(led_sag,0)
             time.sleep(0.05)
             GPIO.output(buzzer,0)
             GPIO.output(led_sol,0)
             time.sleep(0.2)
          
         
             print("Mesafe:",distance - 0.5,"cm değer: "+str(deger))
    
        if deger<2.5:
            deger=2.5
        elif deger>12.5:
            deger=12.5
        
    
TRIG = 24
ECHO = 23
led_sol = 5
led_orta = 6
led_sag  = 13
buzzer  = 26
GPIO.setup(led_sol,GPIO.OUT)
GPIO.setup(led_orta,GPIO.OUT)
GPIO.setup(led_sag,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
 


while True:

  GPIO.output(TRIG, False)
  print ("Olculuyor...")
  time.sleep(0.3)
     
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
  echoservo()
#   print("Mesafe:",distance - 0.5,"cm")
  
  