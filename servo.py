import machine
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


def openGate():
    for _ in range(1):
        for angle in range(0, 110, 10):
            set_servo_angle(angle)
            utime.sleep(0.05)
    pwm.deinit()

            
def colseGate():
    for _ in range(1):
        for angle in range(110, 0, -10):
            set_servo_angle(angle)
            utime.sleep(0.05)
    pwm.deinit()

def openAndClose():
    openGate()
    utime.sleep(2)
    colseGate()
# Number of sweeps to perform
#num_sweeps = 1

# Main loop to sweep the servo back and forth
#for _ in range(num_sweeps):
 #   for angle in range(0, 110, 10):
  #      set_servo_angle(angle)
   #     utime.sleep(0.05)
    #utime.sleep(2)
    #for angle in range(110, 0, -10):
     #   set_servo_angle(angle)
      #  utime.sleep(0.05)

# Stop the servo motor by turning off PWM
pwm.deinit()
