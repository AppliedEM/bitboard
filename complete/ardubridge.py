import serial
from binascii import hexlify, unhexlify
from io import BytesIO
from random import randint
from unittest import TestCase
from ecc import G
import time

delim = b'|'
sername = '/dev/ttyUSB0';
signchar = b's'
pubkeychar = b'p'
walletchar = b'w'
pubkeywritechar = b'l'
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
'''
def gettoken():
    out = ''
    s = ser.read().decode("utf-8")
    print(s)
    while s != delim:
        out = out + s
        s = ser.read().decode("utf-8")
    return out
'''
def signwvars(z, r, k_inv):
    outp = signchar + bytearray(str(z), 'UTF-8') + delim + bytearray(str(r), 'UTF-8') + delim + bytearray(str(k_inv), 'UTF-8') + delim
    print("hash:")
    print(outp)
    ser.write(outp)
    s1 = ser.readline().strip()#gettoken().strip()
    print(s1)
    s2 = ser.readline().strip()#gettoken().strip()
    print(s2)
    return s1, s2

def sign(z):
    r,k_inv = getsiginputs()
    return signwvars(z, r, k_inv)

def getpubkey():
    ser.write(pubkeychar)
    x = ser.readline().strip()
    print(x)
    y = ser.readline().strip()
    print(y)
    return x,y

def writewallet(privkey):
    ser.write(walletchar + bytearray(privkey, 'UTF-8') + delim)

def writepubkey(pubkeyx, pubkeyy):
    ser.write(pubkeywritechar + bytearray(pubkeyx, 'UTF-8') + delim + bytearray(pubkeyy, 'UTF-8') + delim)

#verify(z, r, k_inv)
