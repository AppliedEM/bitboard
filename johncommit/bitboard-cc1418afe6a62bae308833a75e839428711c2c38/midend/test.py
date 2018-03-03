import serial

delim = b'|'
sername = '/dev/ttyUSB0';
testhash = b's120|107303582290733097924842193972465022053148211775194373671539518313500194639752|31263864094075372764364165952345735120266142355350224183303394048209903603471|'

ser = serial.Serial(sername);
ser.baudrate = 115200

def gettoken():
    out = ''
    s = ser.read()
    while s != delim:
        out = out + s.decode("utf-8")
        s = ser.read()
    return out

ser.write(testhash)
s1 = gettoken()
s2 = gettoken()
print(s1)
print(s2)
