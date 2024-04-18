from mfrc522 import MFRC522
import utime
 
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
reader.init()
#print("Bring TAG closer...")
#print("")
 
def read_rfid():
    
    while True:
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card = int.from_bytes(bytes(uid),"little",False)
                #print("CARD ID: "+str(card))
                return str(card)

