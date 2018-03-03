from binascii import hexlify, unhexlify
from ecc import PrivateKey, Signature, S256Point
from helper import decode_base58, p2pkh_script, SIGHASH_ALL, encode_base58
from script import Script
from tx import TxIn, TxOut, Tx
import ardubridge

import base58

from btctools import wiftonum, validwif, Key

#privatekey = 1337
privatekey = 'cQqRbFo7TCTxQ5hNUeh9uBai4VCBK6YL9JRnujmM95hDFA8bqwNX'
privatekey2 = b'cTeJE6qL8FUP6RGfKiS8Ji61ncMPJzdFtuv9s5TkpYyHbZ8EisSX'
privatekey3 = b'91sSDyirZWESRWzaooVpxNr29ci1Fi53SZLJq1BGBP2kq8UVekj'

#test address: n2A6fCimAFPzC3SektLU4FnNd1qtbQjqZe
taddr1 = 'n2A6fCimAFPzC3SektLU4FnNd1qtbQjqZe'
#test address2: mr2wLxerAQbHRDSL1sgdXLjdB21hCTMPm3
taddr2 = 'mr2wLxerAQbHRDSL1sgdXLjdB21hCTMPm3'
#test address3: mya7sDff3K4ma39tebBKtjD8UTnCxtWPV9

#transid = 'a213e9d57bc96c2b289dc7217b2eec8ba2aec49749f11dd36ad1a12d9677c451'
transid = '1b4c79d48515ec83b23b0696711f397afa619df51f199f10eeb7341ae5fd4a31'
# Transaction Construction Example

'''
converts two arrays (the transaction id and the UTXO index in the transaction)
to an array of TxIn objects
'''
def buildinputs(transidsarr, transindexarr):
    tx_ins = []
    for i in range(len(transidsarr)):
        tx_ins.append(TxIn(
            prev_tx = unhexlify(transidsarr[i]),
            prev_index = transindexarr[i],
            script_sig = b'',
            sequence = 0xffffffff,
        ))
    return tx_ins

'''
converts two arrays (the bitcoin addresses and the amounts to be sent to
those addresses) to an array of TxOut objects
'''
def buildoutputs(pubkeysarr, amountsarr):
    tx_outs = []
    for i in range(len(pubkeysarr)):
        tx_outs.append(TxOut(
            amount = int(amountsarr[i]),
            script_pubkey = p2pkh_script(decode_base58(pubkeysarr[i])),
        ))
    return tx_outs

def build_transaction(transidsarr, transindexarr, pubeysarr, amountsarr, privatekey):
    tx_ins = buildinputs(transidsarr, transindexarr)
    tx_outs = buildoutputs(pubkeysarr, amountsarr)
    tx_obj = Tx(version=1, tx_ins=tx_ins, tx_outs=tx_outs, locktime=0, testnet=True)
    hash_type = SIGHASH_ALL
    z = tx_obj.sig_hash(0, hash_type)
    pk = PrivateKey(secret=privatekey)
    sighash = SIGHASH_ALL
    z = tx_obj.sig_hash(0, sighash)
    #print(z)
    der = pk.sign(z).der()
    sig = der + bytes([sighash])
    sec = pk.point.sec()
    tx_obj.tx_ins[0].script_sig = Script([sig, sec])
    #print("serialized:")
    #print(hexlify(Script([sig,sec]).serialize()))
    #print("----------")
    return hexlify(tx_obj.serialize())

def build_transaction2(transidsarr, transindexarr, pubeysarr, amountsarr):
    tx_ins = buildinputs(transidsarr, transindexarr)
    tx_outs = buildoutputs(pubkeysarr, amountsarr)
    tx_obj = Tx(version=1, tx_ins=tx_ins, tx_outs=tx_outs, locktime=0, testnet=True)
    hash_type = SIGHASH_ALL
    z = tx_obj.sig_hash(0, hash_type)
    #pk = PrivateKey(secret=privatekey)
    sighash = SIGHASH_ALL
    z = tx_obj.sig_hash(0, sighash)
    r,s = ardubridge.sign(z)
    sig = Signature(int(r), int(s))
    der = sig.der()
    sig = der + bytes([sighash])
    #sec = pk.point.sec()
    #print("public point:")
    #print(int(pk.point.x.hex(), 16))
    #print(int(pk.point.y.hex(), 16))
    x,y = ardubridge.getpubkey()
    #pub = S256Point(53237820045986896539096637357322002537362350769420441605069248472301971758546, 49407176618187043960559197373734381057571970898731550795341045595301080938882)
    pub = S256Point(int(x), int(y))
    sec2 = pub.sec()
    tx_obj.tx_ins[0].script_sig = Script([sig, sec2])
    return hexlify(tx_obj.serialize())

total = int(2.56*100000000)
fee = 10000000

unspent = total-fee

transidsarr = [transid]
transindexarr = [0]

pubkeysarr = [taddr1, taddr2]
amountsarr = [.9*unspent, .1*unspent]

def debug1():
    z = 82736482736928392039492837498273984692387492
    pk = PrivateKey(secret = privatekey)
    r,s = ardubridge.sign(z)
    sig = pk.sign(z)
    print("r1: ")
    print(r)
    print("s1: ")
    print(s)
    print("r2: ")
    print(sig.r)
    print("s2: ")
    print(sig.s)

def debug2():
    a=1

#debug1()
#print(build_transaction(transidsarr, transindexarr, pubkeysarr, amountsarr, privatekey))
print(build_transaction2(transidsarr, transindexarr, pubkeysarr, amountsarr))
