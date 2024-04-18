import utime as time
now=time.time()
tm=time.localtime(now)
drn=tm[:3]
y = int(drn[0])
mo = int(drn[1])
d = int(drn[2])
tm1=tm[3:-2]
h = str(tm1[0])
m = str(tm1[1])
s = str(tm1[2])

def check_date(date):
    date  = date.split('.')
    print(date)
    if(y < int(date[0])):
        return True
    elif(y > int(date[0])):
        return False
    elif(mo < int(date[1])):
        return True
    elif(mo > int(date[1])):
        return False
    elif(d < int(date[2])):
        return True      
    return False
def check_time(hour,minute,second):

    if (h == hour and m == minute):
        if (second == s):
            return "e"
        elif (second > s):
            return "g"
        elif (second < s):
            return "s"
    return "g"


def get_time():
    tm=time.localtime(now)
    tm1=tm[3:-2]
    h = str(tm1[0])
    m = str(tm1[1])
    s = str(tm1[2])
    return tm1
def get_timeStr():
    return h+"."+m+"."+s
check_date("2030.09.07")

