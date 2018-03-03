import serial
import ardubridge

delim = b'|'
sername = '/dev/ttyUSB0';
signchar = b's'

z = b'120'
#r = b'107303582290733097924842193972465022053148211775194373671539518313500194639752'
#k_inv = b'31263864094075372764364165952345735120266142355350224183303394048209903603471'

ser = serial.Serial(sername);
ser.baudrate = 115200

def gettoken():
    out = ''
    s = ser.read()
    while s != delim:
        out = out + s.decode("utf-8")
        s = ser.read()
    return out

def verify(z, r, k_inv):
    outp = signchar + z + delim + r + delim + k_inv + delim
    print("hash")
    print(outp)
    ser.write(outp)
    s1 = gettoken().strip()
    s2 = gettoken().strip()
    print(s1)
    print(s2)

z = tx_obj.sig_hash(0, sighash)
s1,s2 = ardubridge.sign(z)

print(s1)
print(s2)
#verify(z, r, k_inv)
