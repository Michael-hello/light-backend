import pigpio
import time

pi = pigpio.pi()
#pi.set_PWM_dutycycle(17, 255)
#pi.set_PWM_dutycycle(22, 0)
#pi.set_PWM_dutycycle(24, 0)
#print('17')
#time.sleep(2)
#
#pi.set_PWM_dutycycle(17, 0)
#pi.set_PWM_dutycycle(22, 255)
#pi.set_PWM_dutycycle(24, 0)
#print('22')
#time.sleep(2)
#
#pi.set_PWM_dutycycle(17, 0)
#pi.set_PWM_dutycycle(22, 0)
#pi.set_PWM_dutycycle(24, 255)
#print('24')
#time.sleep(2)
for x in range(0,5):  
#    pi.set_PWM_dutycycle(17, 255) #blue
#    pi.set_PWM_dutycycle(22, 255) #green
#    pi.set_PWM_dutycycle(24, 255) #red
#    time.sleep(0.5)
    pi.set_PWM_dutycycle(17, 124) #blue
    pi.set_PWM_dutycycle(22, 124) #green
    pi.set_PWM_dutycycle(24, 124) #red
    time.sleep(0.5)
    pi.set_PWM_dutycycle(17, 62) #blue
    pi.set_PWM_dutycycle(22, 62) #green
    pi.set_PWM_dutycycle(24, 62) #red
    time.sleep(0.5)
    
print('24')
time.sleep(5)

pi.set_PWM_dutycycle(17, 0)
pi.set_PWM_dutycycle(22, 0)
pi.set_PWM_dutycycle(24, 0)

pi.stop()