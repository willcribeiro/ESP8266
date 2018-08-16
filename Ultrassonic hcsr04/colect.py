from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=16, echo_pin=0)
i = 0
#Leitura em 180 graus
while i<6: 
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    i = i + 1 
    time.sleep(1)
