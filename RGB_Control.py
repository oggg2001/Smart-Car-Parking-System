from machine import Pin
from mfrc522 import MFRC522
import utime
       
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
            
            if card == 501583777:
                print("Card ID: "+ str(card)+" PASS: Green Light Activated")
                red.value(0)
                green.value(1)
                
    #utime.sleep(5)
            
            elif card == 855703208:
                print("Card ID: "+ str(card)+" PASS: Blue Light Activated")
                red.value(0)
                green.value(1)
                
    #utime.sleep(5)
            
            else:
                print("Card ID: "+ str(card)+" UNKNOWN CARD! Red Light Activated")
                red.value(1)
                green.value(0)