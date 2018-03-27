import serial.tools.list_ports
import esptool
import subprocess

def guessarduport():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if('USB' in p.description and ('SERIAL' in p.description or 'Serial' in p.description)):
            return p.device

def listports():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        p

p = guessarduport()
print("Guessed arduino port. Is this correct? (y/n): " + p)
resp = input()
if resp == 'n':
    print("-------List of ports---------")
    listports()
    print("-----------------------------")
    print("Please locate port manually and input: ")
    p = input()

subprocess.call([
    'esptool.py',
    '--port',
    p,
    'write_flash',
    '0x00000',
    'arduclient.ino.nodemcu.bin'
    ])
