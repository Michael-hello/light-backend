import pigpio
import time

#See following for log brightness
#https://electromotiveforces.blogspot.com/2011/10/led-fading-using-exponentially-changing.html

pi = pigpio.pi()
max = 255
interval = 200
r = interval/8


def get_duty_cycle(x, r):
    cycle = 2**(x/r) - 1
    print(cycle, x)
    return cycle


def leds_fade(duration):
#    duration in seconds
#    fades lights from 0 to 255 brightness with logarithmic staging
    x = 0
    while(get_duty_cycle(x, r) <= max):  

        val = get_duty_cycle(x, r)
        pi.set_PWM_dutycycle(17, val) #blue
        pi.set_PWM_dutycycle(22, val) #green
        pi.set_PWM_dutycycle(24, val) #red
        
        time.sleep(duration/interval)
        x = x + 1
    

def leds_off():
    
    pi.set_PWM_dutycycle(17, 0)
    pi.set_PWM_dutycycle(22, 0)
    pi.set_PWM_dutycycle(24, 0)    
    pi.stop()
    

def leds_on():
    
    pi.set_PWM_dutycycle(17, 255)
    pi.set_PWM_dutycycle(22, 255)
    pi.set_PWM_dutycycle(24, 255)
    

def leds_on_rgb(r, g, b):

    pi.set_PWM_dutycycle(17, r)
    pi.set_PWM_dutycycle(22, g)
    pi.set_PWM_dutycycle(24, b) 




    




