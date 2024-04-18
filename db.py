from  firebase import get_data, set_data,update_value_in_parks
from collections import OrderedDict



def getById(id):
    data = get_data("Users")
    return data[id]

def getNumberOfFreePark():
    return getdata("park")["free_park"]


def getNumberOfBussyPark():
    return getdata("park")["bussy_park"]


def getNumberOfMaxPark():
    return getdata("park")["max_cars"]

def isfull():
    return getdata("Parks")["isfull"]

def getFreePark():
    parks = get_data("Parks")
    parks = OrderedDict(sorted(parks.items()))
    parks.popitem()
    for park in parks.items():
        #print(parks)
        if not(park[1]):
            update_value_in_parks(park[0],True)
            return park[0]
    update_value_in_parks("isfull",True)
    return None
            

        
        
        
        
    

