import btccore
import ardubridge
import time

#tests the wif-import function
def importtest():
    privatekey2 = 'cTeJE6qL8FUP6RGfKiS8Ji61ncMPJzdFtuv9s5TkpYyHbZ8EisSX'
    btccore.changewallet(privatekey2)
    x,y = ardubridge.getpubkey()
    print('x-coord')
    print(x)
    print('y-coord')
    print(y)
    if x == b'69450585114360778982578047439232137453781038709951231527714375955216555119475' and y == b'114780863257592259610368907099699416869271222059464727485966622335048955651600':
        print('import test passed')
        return True
    print('import test failed')
    return False

def erasetest():
    if not importtest():
        print('could not import')
        return False
    else:
        ardubridge.erase()
        x,y = ardubridge.getpubkey()
        if x != '-1' and y != '-1':
            print('did not erase')
            print('x:')
            print(x)
            print('y:')
            print(y)
            return False
        else:
            print('erase test passed')
            return True
    return False

#checks the x and y coord of the public key
def checkpubkey():
    x,y = ardubridge.getpubkey()
    print('x-coord')
    print(x)
    print('y-coord')
    print(y)

print(erasetest())
