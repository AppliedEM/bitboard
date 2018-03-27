import serial.tools.list_ports

def guessarduport():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if(('USB' in p.description and ('SERIAL' in p.description or 'Serial' in p.description)) or 'CP2102' in p.description):
            return p.device

def listports():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)

listports()
print(guessarduport())
