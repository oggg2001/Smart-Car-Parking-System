from machine import Pin
from mfrc522 import MFRC522
import utime

 
 
 # Set the servo motor pin
servo_pin = machine.Pin(15)

# Create a PWM object with a frequency of 50Hz (standard for servos)
pwm = machine.PWM(servo_pin)
pwm.freq(50)

# Function to set the servo angle
def set_servo_angle(angle):
    # Map the angle to the PWM duty cycle (500-2500 microseconds)
    duty_cycle = int(500 + (angle / 180) * 2000)
    pwm.duty_ns(duty_cycle * 1000)

# Number of sweeps to perform
num_sweeps = 1

reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
 
red = Pin(0, Pin.OUT)
green = Pin(1, Pin.OUT)
 
print("Bring RFID TAG Closer...")
print("")
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            
            
            utime.sleep(1) #To make delay between the card's reader
            
           
            if card == 855703208:
                print("Card ID: "+ str(card)+" PASS: Green Light Activated")
                red.value(0)
                green.value(1)
                
                for _ in range(num_sweeps):
                   for angle in range(0, 110, 10):
                       set_servo_angle(angle)
                       utime.sleep(0.05)
                   utime.sleep(2)
                   
                   for angle in range(110, 0, -10):
                       set_servo_angle(angle)
                       utime.sleep(0.05)

# Stop the servo motor by turning off PWM
                pwm.deinit()
            
            else:
                print("Card ID: "+ str(card)+" UNKNOWN CARD! Red Light Activated")
                red.value(1)
                green.value(0)
                                                                           