from binascii import hexlify, unhexlify
from ecc import PrivateKey
from helper import decode_base58, p2pkh_script, SIGHASH_ALL, encode_base58
from script import Script
from tx import TxIn, TxOut, Tx

import base58

from btctools import wiftonum, validwif, Key

privatekey = 'cQqRbFo7TCTxQ5hNUeh9uBai4VCBK6YL9JRnujmM95hDFA8bqwNX'
privatekey2 = b'cTeJE6qL8FUP6RGfKiS8Ji61ncMPJzdFtuv9s5TkpYyHbZ8EisSX'
privatekey3 = b'91sSDyirZWESRWzaooVpxNr29ci1Fi53SZLJq1BGBP2kq8UVekj'

#test address: n2A6fCimAFPzC3SektLU4FnNd1qtbQjqZe
taddr1 = 'n2A6fCimAFPzC3SektLU4FnNd1qtbQjqZe'
#test address2: mr2wLxerAQbHRDSL1sgdXLjdB21hCTMPm3
taddr2 = 'mr2wLxerAQbHRDSL1sgdXLjdB21hCTMPm3'
#test address3: mya7sDff3K4ma39tebBKtjD8UTnCxtWPV9

paymentdest = 'mr2wLxerAQbHRDSL1sgdXLjdB21hCTMPm3'

transid = 'a213e9d57bc96c2b289dc7217b2eec8ba2aec49749f11dd36ad1a12d9677c451'
# Transaction Construction Example

total = 1.3*100000000
fee = 100000

t2 = total-fee
# Step 1
tx_ins = []
prev_tx = unhexlify(transid)
print('ptx')
print(prev_tx)
tx_ins.append(TxIn(
            prev_tx=prev_tx,
            prev_index=0,
            script_sig=b'',
            sequence=0xffffffff,
        ))

# Step 2
tx_outs = []
h160 = decode_base58(taddr1)
print("t1")
print(len(h160))
print(hexlify(h160))
tx_outs.append(TxOut(
    amount=int(t2*.97),
    script_pubkey=p2pkh_script(h160),
))
h160 = decode_base58(taddr2)
tx_outs.append(TxOut(
    amount=int(t2*.03),
    script_pubkey=p2pkh_script(h160),
))
tx_obj = Tx(version=1, tx_ins=tx_ins, tx_outs=tx_outs, locktime=0, testnet=True)

# Step 3
hash_type = SIGHASH_ALL
z = tx_obj.sig_hash(0, hash_type)

pk = PrivateKey(secret=privatekey)

# sign with SIGHASH_ALL
sighash = SIGHASH_ALL
# get the sighash
z = tx_obj.sig_hash(0, sighash)
# sign with priv to get der
der = pk.sign(z).der()
# add the sighash as a single byte bytes([sighash])
sig = der + bytes([sighash])
# get the sec from priv
sec = pk.point.sec()
# create a new script that has sig and sec as the new input sig
tx_obj.tx_ins[0].script_sig = Script([sig, sec])
print(hexlify(tx_obj.serialize()))

'''der = pk.sign(z).der()
sig = der + bytes([hash_type])
sec = pk.point.sec()
script_sig = bytes([len(sig)]) + sig + bytes([len(sec)]) + sec
script_sig = bytes([len(script_sig)]) + script_sig
tx_obj.tx_ins[0].script_sig = Script.parse(script_sig)
print(hexlify(tx_obj.serialize()))
'''
