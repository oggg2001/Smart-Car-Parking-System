from machine import Pin
import utime 
red = Pin(13, Pin.OUT,0)
green = Pin(11, Pin.OUT,0)
red.value(0)
green.value(0)
leds = [red, green]
def toggleRed(led_index):
    leds[led_index].value(1)
    if(led_index==0):
        utime.sleep(0.5)
    else:
        utime.sleep(1.5)
    leds[led_index].value(0)
    