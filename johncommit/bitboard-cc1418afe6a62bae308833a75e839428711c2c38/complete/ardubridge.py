import serial
from binascii import hexlify, unhexlify
from io import BytesIO
from random import randint
from unittest import TestCase
from ecc import G

delim = b'|'
sername = '/dev/ttyUSB0';
signchar = b's'
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

#z = b'120'
#r = b'107303582290733097924842193972465022053148211775194373671539518313500194639752'
#k_inv = b'31263864094075372764364165952345735120266142355350224183303394048209903603471'

ser = serial.Serial(sername);
ser.baudrate = 115200

def getsiginputs():
    k = randint(0, 2**256)
    r = (k*G).x.num
    k_inv = pow(k, N-2, N)
    return r,k_inv

def gettoken():
    out = ''
    s = ser.read()
    while s != delim:
        out = out + s.decode("utf-8")
        s = ser.read()
    return out

def signwvars(z, r, k_inv):
    outp = signchar + bytearray(str(z), 'UTF-8') + delim + bytearray(str(r), 'UTF-8') + delim + bytearray(str(k_inv), 'UTF-8') + delim
    ser.write(outp)
    s1 = gettoken().strip()
    s2 = gettoken().strip()
    return s1, s2

def sign(z):
    r,k_inv = getsiginputs()
    return signwvars(z, r, k_inv)

#verify(z, r, k_inv)
