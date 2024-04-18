from rfid import read_rfid
import utime 
from  firebase import get_data, set_data,update_value_in_parks, update_value_in_users
from wifi import connect_to_wifi
from db import getById, getNumberOfFreePark, getNumberOfBussyPark,getNumberOfMaxPark,isfull,getFreePark
from led import toggleRed
from servo import openGate, colseGate, openAndClose
from time import check_date, check_time,get_time,get_timeStr
import random

import machine
led = machine.Pin("LED", machine.Pin.OUT)
led.on()

wifi_ssid = "ssid name"
wifi_password = "wifi password"
max_cars = 4
        
def exit_Car(user,card_id):
    update_value_in_parks(user["parking_index"],"")
    update_value_in_users(card_id,"isParking",False)
    update_value_in_users(card_id,"parking_index","")
    toggleRed(1)
    openAndClose()
    print("Car Exit successfully")
    
if __name__ == '__main__':
    connect_to_wifi(wifi_ssid,wifi_password)
    while True :
        try:
            print("#####Bring Your ID Card##### (:")
            card_id = read_rfid()
            user = getById(card_id)
            
            print("The ID:", card_id)
            print("The user:", user["Name"],"\n")
            print(user)
            #toggleRed(1)
            
            if(user["isParking"]):
                if(get_data("Parks")["isfull"]):
                    update_value_in_parks("isfull",False)

                user_time_stamp = user["time_stamp"].split(".")
                entey_hours,entey_minutes,entey_second = user_time_stamp
                
                entey_hours = int(entey_hours)
                entey_minutes = int(entey_minutes)
                entey_second = int(entey_second)
                time_limit = int(user["time_of_subscribe"])
                entey_second = entey_second + time_limit
                T = check_time(str(entey_hours),str(entey_minutes),str(entey_second))
                print(T)
                if (T != "g"):
                    exit_Car(user,card_id)
                else:
                    print("you have billing")
                    bill = (user["bill"])
                    print(bill)
                    min_f = False

                    h,m,s = get_time()
                    dif_h = h - entey_hours
                    dif_m = m - entey_minutes
                    dif_s = s - entey_second
                    if(dif_m<0):
                        dif_m = 60 - entey_minutes +  m
                        min_f = True
                    if(dif_h<0 and min_f == False):
                        print("gg")
                        dif_h = abs(dif_h)+24
                

                    if(min_f == True and dif_h == 1):
                        dif_h = 0
                    
                    if(dif_s<0):
                        dif_s = 60 - entey_second +  s
                  
                    # hf = uh == h
                    # mf = um == m
                    # h = (h -uh)
                    
                    # m = (m -um)
                    # s = (s -us)
                    
                    dif_m = dif_m * 60
                    dif_h = dif_h*3600
                    
                    # if (hf):
                    #     h = m + s 
                    # elif (mf):
                    #     h = abs(s)
                    # else:
                    #     h = h+m+s
                    
                    h = (dif_h+dif_m+dif_s) * 0.1
                    
                    # print(bill+h)
                    print(h)
                    bill = bill + h
                    print(bill)
                    update_value_in_users(card_id,"bill",bill)
                    exit_Car(user,card_id)


            else:
                if(not check_date(user["expire_date"])):
                    print("Your Subscription is EXPIRED!!!!")
                    for i in range (5):
                        utime.sleep(0.25)
                        toggleRed(0)
                    continue
                time_stamp = get_timeStr()
                index_of_free_park = getFreePark()
                print(index_of_free_park)
                if (index_of_free_park == None):
                    print("the park is full")
                    for i in range (2):
                        utime.sleep(0.25)
                        toggleRed(0)
                    continue    
                update_value_in_users(card_id,"isParking",True)
                update_value_in_users(card_id,"parking_index",index_of_free_park)
                update_value_in_users(card_id,"time_stamp",time_stamp)
                toggleRed(1)
                openAndClose()
                print("Car Parked successfully")

        except Exception as e:
            print(e)
            toggleRed(0)
            print("You Are Not Registered Please Register!\n")
        utime.sleep(2)       
