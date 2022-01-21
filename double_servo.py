# -- coding: utf-8 --
import RPi.GPIO as GPIO
import os
import glob
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()
led_red = 5
led_green = 10
buzzer  = 26
motorileri=18
motorgeri=16
motordur=22
motorileri2=11
motorgeri2=13
motordur2=15
btileri=40
btgeri=38
btdur=36

GPIO.setup(btileri, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(btgeri, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btdur, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

GPIO.setup(led_red,GPIO.OUT)
GPIO.setup(led_green,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(motorileri,GPIO.OUT)
GPIO.setup(motorgeri,GPIO.OUT)
GPIO.setup(motordur,GPIO.OUT)
GPIO.setup(motorileri2,GPIO.OUT)
GPIO.setup(motorgeri2,GPIO.OUT)
GPIO.setup(motordur2,GPIO.OUT)
ileridön=GPIO.input(btileri)
geridön=GPIO.input(btgeri)
dur=GPIO.input(btdur)
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def motorsarti(temperature):

    if temperature>=40:
        if ileridön==False: 
            GPIO.output(motorileri,GPIO.HIGH)
            GPIO.output(motorgeri,GPIO.LOW)           						 
            GPIO.output(motordur,GPIO.HIGH)
            GPIO.output(motorileri2,GPIO.HIGH)
            GPIO.output(motorgeri2,GPIO.LOW)
            GPIO.output(motordur2,GPIO.HIGH)
            time.sleep(2)
            print ("Motor Ileri Harekete Başladı.")
            
        elif geridön ==False:
            GPIO.output(motorileri,GPIO.LOW)
            GPIO.output(motorgeri,GPIO.HIGH)
            GPIO.output(motordur,GPIO.HIGH)
            GPIO.output(motorileri2,GPIO.LOW)
            GPIO.output(motorgeri2,GPIO.HIGH)
            GPIO.output(motordur2,GPIO.HIGH)
            print ("Motor Geri Hareket Başladı.")
        elif dur == False:

            GPIO.output(motordur,GPIO.LOW)  
            GPIO.output(motordur2,GPIO.LOW)
            print ("Motor Durdu.")
            GPIO.cleanup()
        
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def TriggerLightAndBuzzer(temperature):

    if temperature>= 40 and temperature<70:
        GPIO.output(buzzer,0) # Buzzer On
        GPIO.output(led_green, 0) # Yeşil led Off
        GPIO.output(led_red,1) # Kırmızı led On
    elif temperature < 40: 
        GPIO.output(buzzer, 0) # Buzzer Off
        GPIO.output(led_green,1) # Yeşil led On
        GPIO.output(led_red, 0) # Kırmızı led Off
    elif temperature>=70:
        GPIO.output(buzzer, 1)
        GPIO.output(led_green, 0) # Yeşil led Off
        GPIO.output(led_red,1)
                
    print(temperature) # Mevcut sıcaklık


while True:
    currentTempAsCelcius, currentTempAsFahrenait = read_temp()
    TriggerLightAndBuzzer(currentTempAsCelcius)
    motorsarti(currentTempAsCelcius)
    time.sleep(2)
    
    


